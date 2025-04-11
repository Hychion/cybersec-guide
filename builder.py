import os

# Base directory
base_dir = "cybersec-guide"

# Dossiers et fichiers à créer
structure = {
    "": ["README.md"],
    "docs": ["index.md"],
    "docs/cours/reseaux": [
        "modeles-osi-tcpip.md", "protocoles-essentiels.md", "sniffing-analyse.md"
    ],
    "docs/cours/pentest": [
        "recon.md", "scan-et-enum.md", "exploitation.md", "post-exploitation.md"
    ],
    "docs/cours/forensic": [
        "introduction.md", "outils.md", "analyse-disque.md", "memoire-reseau.md"
    ],
    "docs/cours/privilege-escalation": [
        "linux.md", "windows.md", "macos.md"
    ],
    "docs/cours/wifi": [
        "theorie.md", "attaques.md", "defences.md"
    ],
    "docs/cours/anonymat": [
        "vpn-vs-proxy.md", "tor-tails.md", "opsec.md", "metadata-cleaning.md"
    ],
    "docs/cours/outils": [
        "nmap.md", "wireshark.md", "metasploit.md", "johnhydra.md",
        "aircrack-ng.md", "volatility.md"
    ],
    "docs/cheatsheets": [
        "commandes-bash.md", "enumeration.md", "post-exploitation.md",
        "privesc-linux.md", "privesc-windows.md", "wifi-hack.md"
    ],
    "docs/ressources": [
        "livres.md", "CTFs.md", "chaines-youtube.md", "labs.md", "sites-utiles.md"
    ],
    "assets": [],
    ".github": [],
    ".github/workflows": []
}

# Fonction de création
def create_structure(base_path, structure):
    for folder, files in structure.items():
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        for file in files:
            file_path = os.path.join(path, file)
            with open(file_path, "w") as f:
                f.write(f"# {file.replace('.md', '').replace('-', ' ').title()}\n")

# Lancement
if __name__ == "__main__":
    create_structure(base_dir, structure)
    print(f"Structure du projet '{base_dir}' générée avec succès.")
