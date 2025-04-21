# Modified Havoc C2 PCAP parser script with broader TCP support and user extraction
import os
import argparse
import struct
import binascii
import re
from binascii import unhexlify
from uuid import uuid4

try:
    import pyshark
except ImportError:
    print("[-] Pyshark not installed, please install with 'pip install pyshark'")
    exit(0)

try:
    from Crypto.Cipher import AES
    from Crypto.Util import Counter
except ImportError:
    print("[-] PyCryptodome not installed, please install with 'pip install pycryptodome'")
    exit(0)

sessions = {}
found_users = set()

def tsharkbody_to_bytes(hex_string):
    if not hex_string:
        return b''
    hex_string = hex_string.replace(':', '')
    try:
        return unhexlify(hex_string)
    except Exception as e:
        print(f"[!] Error converting hex string to bytes: {e}")
        return b''

def aes_decrypt_ctr(aes_key, aes_iv, encrypted_payload):
    try:
        ctr = Counter.new(128, initial_value=int.from_bytes(aes_iv, byteorder='big'))
        cipher = AES.new(aes_key, AES.MODE_CTR, counter=ctr)
        return cipher.decrypt(encrypted_payload)
    except Exception as e:
        print(f"[!] Error decrypting payload: {e}")
        return b''

def check_magic_bytes(header_bytes, magic_bytes):
    if len(header_bytes) < 20:
        return False, None
    try:
        _, magic, agent_id, _, _ = struct.unpack('>I4s4sI4s', header_bytes)
        magic_str = binascii.hexlify(magic).decode('ascii')
        agent_id_str = binascii.hexlify(agent_id).decode('ascii')
        return magic_str == magic_bytes, agent_id_str
    except Exception as e:
        print(f"[!] Error checking magic bytes: {e}")
        return False, None

def parse_request(http_pair, magic_bytes, save_path):
    request = http_pair['request']
    response = http_pair['response']
    unique_id = uuid4()

    print("[+] Parsing Request")
    request_body = tsharkbody_to_bytes(request.get('file_data', ''))
    if not request_body:
        print("[!] No request body found")
        return

    has_magic, agent_id = check_magic_bytes(request_body[:20], magic_bytes)
    if not has_magic and agent_id not in sessions:
        print(f"[!] No valid magic bytes or known agent ID")
        return

    if has_magic and len(request_body) >= 68:
        magic = request_body[4:8]
        magic_str = binascii.hexlify(magic).decode('ascii')
        if magic_str == magic_bytes and agent_id not in sessions:
            print("[+] Found Havoc C2 Initial Packet")
            print(f"  [-] Agent ID: {agent_id}")
            print(f"  [-] Magic Bytes: {magic_str}")
            print(f"  [-] C2 Address: {request.get('uri')}")
            aes_key = request_body[20:52]
            aes_iv = request_body[52:68]
            print(f"  [+] Found AES Key")
            print(f"    [-] Key: {binascii.hexlify(aes_key).decode('ascii')}")
            print(f"    [-] IV: {binascii.hexlify(aes_iv).decode('ascii')}")
            sessions[agent_id] = {"aes_key": aes_key, "aes_iv": aes_iv}
            return

    aes_keys = sessions.get(agent_id, None)
    if not aes_keys:
        print(f"[!] No AES keys for Agent ID {agent_id}")
        return

    request_payload = request_body[20:] if has_magic else request_body
    if request_payload:
        print("  [+] Decrypting Client-to-Server Payload")
        decrypted_request = aes_decrypt_ctr(aes_keys['aes_key'], aes_keys['aes_iv'], request_payload)
        if decrypted_request:
            decoded = decrypted_request.decode('utf-8', errors='ignore')
            print(f"  [-] Decrypted Request Payload: {decoded}")
            user_matches = re.findall(r'[A-Za-z0-9\\._-]{3,}\\[A-Za-z0-9._-]{3,}', decoded)
            for match in user_matches:
                print(f"    [*] Found potential user: {match}")
                found_users.add(match)
            if save_path:
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                save_file = f'{save_path}/{unique_id}-request-{agent_id}.bin'
                with open(save_file, 'wb') as output_file:
                    output_file.write(decrypted_request)
                print(f"  [-] Saved decrypted request to {save_file}")

    response_body = tsharkbody_to_bytes(response.get('file_data', ''))
    if response_body and len(response_body) > 12:
        print("  [+] Processing Server-to-Client Response")
        response_payload = response_body[12:]
        if response_payload:
            print("  [+] Decrypting Server-to-Client Payload")
            decrypted_response = aes_decrypt_ctr(aes_keys['aes_key'], aes_keys['aes_iv'], response_payload)
            if decrypted_response:
                decoded = decrypted_response.decode('utf-8', errors='ignore')
                print(f"  [-] Decrypted Response Payload: {decoded}")
                user_matches = re.findall(r'[A-Za-z0-9\\._-]{3,}\\[A-Za-z0-9._-]{3,}', decoded)
                for match in user_matches:
                    print(f"    [*] Found potential user: {match}")
                    found_users.add(match)
                if save_path:
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
                    save_file = f'{save_path}/{unique_id}-response-{agent_id}.bin'
                    with open(save_file, 'wb') as output_file:
                        output_file.write(decrypted_response)
                    print(f"  [-] Saved decrypted response to {save_file}")
    else:
        print("[!] No valid response body found")

def read_pcap_and_get_tcp_payloads(pcap_file, magic_bytes, save_path):
    try:
        capture = pyshark.FileCapture(pcap_file, use_json=True)
    except Exception as e:
        print(f"[!] Error reading PCAP file: {e}")
        return

    print("[+] Parsing Packets")

    for packet in capture:
        try:
            if 'TCP' in packet:
                if hasattr(packet.tcp, 'payload'):
                    payload_hex = packet.tcp.payload.replace(':', '')
                    payload_bytes = tsharkbody_to_bytes(payload_hex)
                    if payload_bytes and len(payload_bytes) > 20:
                        has_magic, agent_id = check_magic_bytes(payload_bytes[:20], magic_bytes)
                        if has_magic or agent_id in sessions:
                            http_pair = {
                                'request': {
                                    'uri': packet.ip.dst,
                                    'file_data': payload_hex
                                },
                                'response': {
                                    'file_data': None
                                }
                            }
                            parse_request(http_pair, magic_bytes, save_path)
        except Exception as e:
            print(f"[!] Packet processing error: {e}")

    capture.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decrypt Havoc C2 Traffic from a PCAP')
    parser.add_argument('--pcap', help='Path to pcap file', required=True)
    parser.add_argument('--aes-key', help='AES key (hex)', required=False)
    parser.add_argument('--aes-iv', help='AES initialization vector (hex)', required=False)
    parser.add_argument('--agent-id', help='Agent ID (hex)', required=False)
    parser.add_argument('--save', help='Directory to save decrypted payloads', required=False)
    parser.add_argument('--magic', help='Magic bytes marker for Havoc C2 traffic', default='deadbeef', required=False)
    args = parser.parse_args()

    if any([args.aes_key, args.aes_iv, args.agent_id]) and not all([args.aes_key, args.aes_iv, args.agent_id]):
        parser.error("[!] If you provide one of 'aes-key', 'aes-iv', or 'agent-id', you must provide all three.")

    if args.agent_id and args.aes_key and args.aes_iv:
        try:
            sessions[args.agent_id] = {
                "aes_key": unhexlify(args.aes_key),
                "aes_iv": unhexlify(args.aes_iv)
            }
            print(f"[+] Added session keys for Agent ID {args.agent_id}")
        except Exception as e:
            print(f"[!] Error processing provided AES key/IV: {e}")
            exit(1)

    read_pcap_and_get_tcp_payloads(args.pcap, args.magic, args.save)

    if found_users:
        print("\n[+] All Potential Found Users:")
        for user in sorted(found_users):
            print(f"  - {user}")
    else:
        print("[!] No users found in decrypted payloads.")

