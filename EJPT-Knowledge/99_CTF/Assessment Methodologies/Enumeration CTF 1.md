# Rappel Démarche CTF Labs INE pour l'EJPT

## 📋 Méthodologie Générale

### Phase 1: Reconnaissance & Collecte d'Informations

#### 🔍 **Reconnaissance Passive**
- **Fichiers standards à vérifier en premier:**
  - `robots.txt` - Indique aux moteurs de recherche quoi éviter
  - `sitemap.xml` - Structure du site
  - `.well-known/` - Répertoire de métadonnées

#### 🛠️ **Énumération Active**
1. **Scan de ports et services:**
   ```bash
   # Scan complet avec détection de services et vulnérabilités
   nmap target.ine.local -sC -sV
   
   # Scan plus agressif avec détection d'OS
   nmap -sVC -sS -O target.ine.local
   
   # Scan avec scripts de vulnérabilité
   nmap -sC -sV target.ine.local --script vuln --min-rate 1000
   ```
   - Identifier les services et leurs versions
   - Noter les technologies utilisées
   - **Analyser les headers HTTP personnalisés**

2. **Services spécifiques découverts:**
   ```bash
   # FTP (Port 21) - Tester connexion anonyme
   ftp target.ine.local
   # User: anonymous, Password: [vide ou anonymous]
   
   # FTP sur port non-standard (ex: 5554)
   ftp target.ine.local 5554
   
   # HTTP (Port 80) - Analyser robots.txt
   curl http://target.ine.local/robots.txt
   
   # SSH (Port 22) - Vérifier bannière
   ssh target.ine.local
   
   # SMB/CIFS (Ports 139/445) - Énumération complète
   enum4linux -a target.ine.local
   
   # MySQL (Port 3306) - Utiliser credentials trouvés
   mysql -u [username] -p -h target.ine.local
   ```

3. **Énumération SMB/CIFS:**
   ```bash
   # Énumération générale
   enum4linux -a target.ine.local
   
   # Test de connexion anonyme aux shares
   smbclient -L //target.ine.local -N
   
   # Connexion à un share spécifique
   smbclient //target.ine.local/[share] -N
   smbclient //target.ine.local/[share] -U [username]
   ```

4. **Attaques par brute-force:**
   ```bash
   # SMB avec Metasploit
   use scanner/smb/smb_login
   set RHOSTS target.ine.local
   set USER_FILE users.txt
   set PASS_FILE passwords.txt
   
   # FTP avec Hydra
   hydra -L users.txt -P passwords.txt ftp://target.ine.local:5554
   
   # SSH avec Hydra
   hydra -L users.txt -P passwords.txt ssh://target.ine.local
   ```

2. **Brute-force de répertoires:**
   ```bash
   # Scan basique
   dirb http://target.ine.local
   
   # Avec extensions spécifiques pour les backups
   dirb http://target.ine.local -w /usr/share/dirb/wordlists/big.txt -X .bak,.tar.gz,.zip,.sql,.bak.zip
   ```

3. **Recherche de fichiers de sauvegarde sensibles:**
   - `.bak`, `.tar.gz`, `.zip`, `.sql`, `.bak.zip`
   - `wp-config.bak`, `config.bak`
   - Fichiers de configuration exposés

### Phase 2: Analyse et Exploitation

#### 📁 **Exploration des Répertoires Découverts**
- **WordPress:** Vérifier `wp-content/uploads/`
- **Répertoires sensibles:** `/admin`, `/backup`, `/config`
- **Fichiers cachés:** Utiliser `ls -la` en local

#### 🔄 **Mirror du Site Web**
```bash
httrack http://target.ine.local -O target.html
```
- Permet de découvrir des fichiers cachés ou des liens internes
- Analyser les fichiers téléchargés localement

### Phase 3: Analyse des Résultats

#### 📖 **Lecture des Fichiers Trouvés**
```bash
# Lire le contenu des fichiers suspects
curl http://target.ine.local/wp-config.bak
cat fichier_suspect.php
```

## 🎯 Questions et Emplacements des Flags

### **CTF 1: Assessment Methodologies - Information Gathering**

#### **Question 1:** *"This tells search engines what to and what not to avoid."*
- **Action:** Vérifier le fichier `robots.txt`
- **Commande:** `curl http://target.ine.local/robots.txt`
- **Emplacement:** Racine du site web
- **🏁 Flag:** `f2ee2d09e076462eadce8807895a4461`

#### **Question 2:** *"What website is running on the target, and what is its version?"*
- **Action:** Identifier la version du serveur web
- **Commande:** `nmap target.ine.local -sC -sV`
- **Emplacement:** Dans les headers de réponse HTTP
- **🏁 Flag:** `3395843029c743ddb00c9adac8b2c7cc`

#### **Question 3:** *"Directory browsing might reveal where files are stored."*
- **Action:** Brute-force des répertoires
- **Commande:** `dirb http://target.ine.local`
- **Emplacement:** Répertoire `wp-content/uploads/`
- **🏁 Flag:** `ccca869e58f54c02b0fa4f9b5a1ee84f`

#### **Question 4:** *"An overlooked backup file in the webroot can be problematic if it reveals sensitive configuration details."*
- **Action:** Rechercher les fichiers de sauvegarde
- **Commande:** `dirb http://target.ine.local -w /usr/share/dirb/wordlists/big.txt -X .bak,.tar.gz,.zip,.sql,.bak.zip`
- **Lecture:** `curl http://target.ine.local/wp-config.bak`
- **Emplacement:** Fichier `wp-config.bak`
- **🏁 Flag:** `de9e6050a6de44daa74e91e87b3112f3`

### **CTF 2: Assessment Methodologies - Footprinting and Scanning**

#### **Flag 1:** *"The server proudly announces its identity in every response. Look closely; you might find something unusual."*
- **Action:** Analyser les headers HTTP du serveur
- **Commande:** `nmap -sVC -sS -O target.ine.local`
- **Emplacement:** Header HTTP personnalisé "Server"
- **🏁 Flag:** `FLAG1_6d7c98b29df248b2849d756708b270ea`

#### **Flag 2:** *"The gatekeeper's instructions often reveal what should remain unseen. Don't forget to read between the lines."*
- **Action:** Vérifier robots.txt et explorer les répertoires interdits
- **Navigation:** `http://target.ine.local/robots.txt` → `http://target.ine.local/secret-info/flag.txt`
- **Emplacement:** Répertoire `/secret-info/flag.txt`
- **🏁 Flag:** `FLAG2_[hash]`

#### **Flag 3:** *"Anonymous access sometimes leads to forgotten treasures. Connect and explore the directory; you might stumble upon something valuable."*
- **Action:** Connexion FTP anonyme
- **Commandes:** 
  ```bash
  ftp target.ine.local
  # User: anonymous (password vide)
  ls
  get flag.txt
  ```
- **Emplacement:** Fichier `flag.txt` sur le serveur FTP
- **🏁 Flag:** `FLAG3_557062aaacb3418e858496ef0b5aa6e0`

### **CTF 3: Assessment Methodologies - Vulnerability Assessment**

#### **Flag 1:** *"Explore hidden directories for version control artifacts that might reveal valuable information."*
- **Action:** Scanner avec scripts de vulnérabilité et chercher répertoire `.git`
- **Commande:** `nmap -sC -sV target.ine.local --script vuln --min-rate 1000`
- **Navigation:** `http://target.ine.local/.git/` → explorer les fichiers
- **Emplacement:** Fichier `flag.txt` dans le répertoire `.git`
- **🏁 Flag:** `4b23c461f2f84bde8ad05679a29f3cb7`

#### **Flag 2:** *"The data storage has some loose security measures. Can you find the flag hidden within it?"*
- **Action:** Accéder à PhpMyAdmin et explorer les bases de données
- **Navigation:** `http://target.ine.local/phpmyadmin/`
- **Exploration:** Base de données `mysql` → table `secret_info`
- **Emplacement:** Table `secret_info` dans la base `mysql`
- **🏁 Flag:** `d60c78c764f74c09b038f6576e7226f5`

#### **Flag 3:** *"A PHP file that displays server information might be worth examining. What could be hidden in plain sight?"*
- **Action:** Vérifier le fichier phpinfo.php découvert par nmap
- **Navigation:** `http://target.ine.local/phpinfo.php`
- **Emplacement:** Contenu du fichier phpinfo.php
- **🏁 Flag:** `fd1f16c3ba634f98a7ce43ca5ee0d3b2`

### **CTF 4: Assessment Methodologies - Enumeration**

#### **Flag 1:** *"There is a samba share that allows anonymous access. Wonder what's in there!"*
- **Action:** Énumérer les shares SMB et identifier accès anonyme
- **Commandes:** 
  ```bash
  enum4linux -a target.ine.local
  # Script de brute-force des shares
  smbclient //target.ine.local/pubfiles -N
  ```
- **Emplacement:** Share `pubfiles` avec accès anonyme
- **🏁 Flag:** `ec16bc35f93d4e93a9b48ca747e331d4`

#### **Flag 2:** *"One of the samba users have a bad password. Their private share with the same name as their username is at risk!"*
- **Action:** Brute-force des comptes SMB avec Metasploit
- **Module Metasploit:** `scanner/smb/smb_login`
- **Utilisateurs découverts:** josh, bob, nancy, alice
- **Connexion:** `smbclient //target.ine.local/josh -U josh`
- **🏁 Flag:** `2ea59c892e6343b78273aba7ce4140ec`

#### **Flag 3:** *"Follow the hint given in the previous flag to uncover this one."*
- **Action:** Suivre l'indice FTP du flag précédent
- **Découverte:** Service FTP sur port 5554
- **Brute-force:** `hydra -L users.txt -P /root/Desktop/wordlists/unix_passwords.txt ftp://target.ine.local:5554`
- **Utilisateurs faibles:** ashley, alice, amanda
- **🏁 Flag:** `dc6ea4029bfd42548c2bf19be77d8498`

#### **Flag 4:** *"This is a warning meant to deter unauthorized users from logging in."*
- **Action:** Se connecter au service SSH
- **Observation:** Banner/message d'avertissement SSH
- **Emplacement:** Message de bannière SSH lors de la connexion
- **🏁 Flag:** `4a03de945ffb4bc0947c3dfe5d4e507b`

### **Assessment Methodologies - Information Gathering**

| Question | Challenge Type | Action | Commande/Méthode | Flag Attendu |
|----------|---------------|--------|------------------|--------------|
| Q1 | Robots.txt | Vérifier fichier standard | `curl http://target.ine.local/robots.txt` | `f2ee2d09e076462eadce8807895a4461` |
| Q2 | Version identification | Scanner les services | `nmap -sC -sV target` | `3395843029c743ddb00c9adac8b2c7cc` |
| Q3 | Directory browsing | Brute-force répertoires | `dirb http://target.ine.local` | `ccca869e58f54c02b0fa4f9b5a1ee84f` |
| Q4 | Backup files | Scanner avec extensions | `dirb [...] -X .bak,.sql,.zip` | `de9e6050a6de44daa74e91e87b3112f3` |
| Q5 | Mirror analysis | Copie locale complète | `httrack http://target.ine.local` | `e79d9c81cc384cdd91bbc563fd61b7ee` |

### **Assessment Methodologies - Enumeration**

| Flag | Challenge Type | Action | Commande/Méthode | Flag Attendu |
|------|---------------|--------|------------------|--------------|
| Flag 1 | SMB Enumeration | Énumération shares SMB | `enum4linux -a` → `smbclient //target/pubfiles -N` | `ec16bc35f93d4e93a9b48ca747e331d4` |
| Flag 2 | SMB Password Attack | Brute-force SMB avec Metasploit | `scanner/smb/smb_login` → connexion josh | `2ea59c892e6343b78273aba7ce4140ec` |
| Flag 3 | FTP Enumeration | Brute-force FTP avec Hydra | `hydra ftp://target:5554` → connexion | `dc6ea4029bfd42548c2bf19be77d8498` |
| Flag 4 | SSH Banner | Connexion SSH et lecture banner | Connexion SSH → message d'avertissement | `4a03de945ffb4bc0947c3dfe5d4e507b` |

### **Checklist de Sécurité Web**

#### ✅ **Toujours Vérifier:**
- [ ] `robots.txt`
- [ ] Scan Nmap complet (`-sC -sV` ou `-sVC -sS -O`)
- [ ] **Scan de vulnérabilités** (`--script vuln`)
- [ ] **Headers HTTP personnalisés** (chercher des flags dans les réponses)
- [ ] **Répertoires de contrôle de version** (`.git/`, `.svn/`)
- [ ] **Connexion FTP anonyme** (si port 21 ouvert)
- [ ] **Services FTP non-standards** (ports 5554, etc.)
- [ ] **Énumération SMB complète** (`enum4linux -a`)
- [ ] **Shares SMB anonymes** (`smbclient -L` puis test des shares)
- [ ] **Brute-force des comptes SMB** (Metasploit scanner/smb/smb_login)
- [ ] **Brute-force FTP/SSH** (Hydra avec wordlists)
- [ ] **Bannières des services** (SSH, FTP, etc.)
- [ ] **Interfaces d'administration** (`/phpmyadmin/`, `/admin/`)
- [ ] **Fichiers d'information système** (`phpinfo.php`, `info.php`)
- [ ] **Répertoires sensibles** (`/passwords/`, `/config/`, `/backup/`)
- [ ] **Fichiers de credentials** téléchargés (creds.txt, etc.)
- [ ] **Bases de données** avec credentials trouvés
- [ ] Brute-force de répertoires avec `dirb`
- [ ] Recherche de fichiers de backup
- [ ] Mirror du site avec `httrack`
- [ ] Analyse des fichiers de configuration exposés

#### 🚨 **Fichiers Sensibles Courants:**
- `wp-config.php` / `wp-config.bak`
- `config.php` / `config.bak`
- `database.sql`
- `.env`
- `backup.zip` / `backup.tar.gz`

## 🛠️ Outils Essentiels

### **Reconnaissance:**
- `nmap` - Scan de ports et services (`-sVC -sS -O` pour scan complet, `--script vuln` pour vulnérabilités)
- `enum4linux` - Énumération complète SMB/CIFS
- `smbclient` - Client SMB pour connexions et exploration
- `dirb` / `gobuster` - Brute-force de répertoires
- `httrack` - Mirror de site web
- `curl` / `wget` - Récupération de fichiers
- `ftp` - Client FTP pour connexions anonymes
- `ssh` - Client SSH (vérification bannières)
- `mysql` / `mysqladmin` - Clients base de données
- **Navigateur web** - Exploration des interfaces d'administration

### **Attaque et Brute-force:**
- `hydra` - Brute-force multi-protocoles (FTP, SSH, HTTP, etc.)
- `metasploit` - Framework avec modules de brute-force (scanner/smb/smb_login)
- `medusa` - Alternative à Hydra pour brute-force
- `crackmapexec` - Outil spécialisé pour SMB/WinRM

### **Analyse:**
- `cat` / `less` - Lecture de fichiers
- `grep` - Recherche dans les fichiers
- `find` - Localisation de fichiers

## 📝 Bonnes Pratiques

### **Organisation:**
1. **Créer un répertoire de travail** pour chaque CTF
2. **Noter tous les flags trouvés** avec leur emplacement
3. **Documenter chaque étape** pour les révisions

### **Efficacité:**
1. **Commencer par les vérifications standards** (robots.txt, nmap)
2. **Paralléliser les scans** quand possible
3. **Analyser méthodiquement** chaque résultat avant de passer au suivant

### **Résolution de Problèmes:**
1. **Si un outil ne fonctionne pas**, essayer des alternatives
2. **Vérifier les permissions** et les chemins d'accès
3. **Regarder les détails** - les flags peuvent être dans les métadonnées

## 🎲 Format et Emplacements des Flags

### **Types de Flags Rencontrés dans ce CTF:**
- **Format:** Hash MD5 (32 caractères hexadécimaux)
- **Exemple:** `f2ee2d09e076462eadce8807895a4461`

### **Emplacements Typiques des Flags:**
| Type de Challenge | Emplacement du Flag | Méthode d'Accès |
|-------------------|--------------------|--------------------|
| **Robots.txt** | Contenu du fichier robots.txt | Lecture directe du fichier |
| **Version Web** | Headers HTTP du serveur | Scan Nmap avec `-sV` |
| **HTTP Headers** | Headers personnalisés (ex: "Server: FLAG1_...") | Scan Nmap ou curl |
| **Directory Browsing** | Répertoire `wp-content/uploads/` | Brute-force puis navigation |
| **Répertoires cachés** | `/secret-info/flag.txt` | Via robots.txt puis navigation |
| **FTP Anonymous** | Fichiers `flag.txt` sur serveur FTP | Connexion anonyme |
| **Backup Files** | Fichier `wp-config.bak` | Scan avec extensions + curl |
| **Fichiers de config** | `creds.txt` avec identifiants | Téléchargement FTP |
| **Base de données** | Nom de base de données contenant le flag | Connexion MySQL |
| **Mirror Analysis** | Fichier `xmlrpc0db0.php` | Analyse du mirror local |
| **Version Control** | Répertoire `.git/flag.txt` | Scripts vuln Nmap |
| **PhpMyAdmin** | Table `mysql.secret_info` | Interface web |
| **Fichiers système** | `phpinfo.php` | Navigation directe |
| **Répertoires sensibles** | `/passwords/flag.txt` | Énumération http-enum |
| **SMB Shares** | Share `pubfiles` avec accès anonyme | `smbclient //target/share -N` |
| **SMB User Shares** | Share personnel (ex: `/josh`) | Brute-force puis connexion |
| **Services FTP non-standards** | Port 5554 avec comptes faibles | Hydra + connexion FTP |
| **Bannières SSH** | Message d'avertissement SSH | Connexion SSH simple |

### **Conseils de Recherche:**
- **Dans les fichiers texte:** Les flags apparaissent souvent en clair
- **Dans les réponses HTTP:** Vérifier les headers et le contenu (headers personnalisés)
- **Dans les connexions FTP:** Toujours tester "anonymous" comme login
- **Dans les répertoires uploads:** Chercher des fichiers cachés ou renommés  
- **Dans les fichiers de config:** Chercher des credentials pour d'autres services
- **Dans les bases de données:** Les flags peuvent être des noms de DB ou dans les tables
- **Dans les mirrors:** Analyser tous les fichiers PHP/XML téléchargés
- **Dans les répertoires de contrôle de version:** Explorer `.git/`, `.svn/` 
- **Dans les interfaces d'administration:** PhpMyAdmin, panels d'admin
- **Dans les fichiers d'info système:** phpinfo.php révèle des configurations
- **Dans les répertoires sensibles:** `/passwords/`, `/admin/`, `/config/`
- **Dans les shares SMB:** Tester accès anonyme puis brute-force des comptes
- **Dans les services sur ports non-standards:** FTP sur 5554, etc.
- **Dans les bannières de services:** SSH, FTP peuvent contenir des flags
- **Suivre les indices:** Les flags précédents donnent souvent des indices pour les suivants

---

💡 **Conseil Final:** Restez méthodique, documentez tout, et n'hésitez pas à revenir aux bases si vous êtes bloqué. La patience et la persévérance sont clés dans les CTF !