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
   # Scan complet avec détection de services
   nmap target.ine.local -sC -sV
   
   # Scan plus agressif avec détection d'OS
   nmap -sVC -sS -O target.ine.local
   ```
   - Identifier les services et leurs versions
   - Noter les technologies utilisées
   - **Analyser les headers HTTP personnalisés**

2. **Services spécifiques découverts:**
   ```bash
   # FTP (Port 21) - Tester connexion anonyme
   ftp target.ine.local
   # User: anonymous, Password: [vide ou anonymous]
   
   # HTTP (Port 80) - Analyser robots.txt
   curl http://target.ine.local/robots.txt
   
   # MySQL (Port 3306) - Utiliser credentials trouvés
   mysql -u [username] -p -h target.ine.local
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

#### **Flag 4:** *"A well-named database can be quite revealing. Peek at the configurations to discover the hidden treasure."*
- **Action:** Utiliser les credentials trouvés en FTP pour accéder à MySQL
- **Commandes:**
  ```bash
  cat creds.txt  # Récupérer les credentials
  mysql -u db_admin -p -h target.ine.local
  SHOW DATABASES;
  ```
- **Emplacement:** Nom de base de données
- **🏁 Flag:** `FLAG4_bbf0089c312a41f884b457878c190195`

### **Assessment Methodologies - Information Gathering**

| Question | Challenge Type | Action | Commande/Méthode | Flag Attendu |
|----------|---------------|--------|------------------|--------------|
| Q1 | Robots.txt | Vérifier fichier standard | `curl http://target.ine.local/robots.txt` | `f2ee2d09e076462eadce8807895a4461` |
| Q2 | Version identification | Scanner les services | `nmap -sC -sV target` | `3395843029c743ddb00c9adac8b2c7cc` |
| Q3 | Directory browsing | Brute-force répertoires | `dirb http://target.ine.local` | `ccca869e58f54c02b0fa4f9b5a1ee84f` |
| Q4 | Backup files | Scanner avec extensions | `dirb [...] -X .bak,.sql,.zip` | `de9e6050a6de44daa74e91e87b3112f3` |
| Q5 | Mirror analysis | Copie locale complète | `httrack http://target.ine.local` | `e79d9c81cc384cdd91bbc563fd61b7ee` |

### **Assessment Methodologies - Footprinting and Scanning**

| Flag | Challenge Type | Action | Commande/Méthode | Flag Attendu |
|------|---------------|--------|------------------|--------------|
| Flag 1 | HTTP Headers | Analyser headers serveur | `nmap -sVC -sS -O target.ine.local` | `FLAG1_6d7c98b29df248b2849d756708b270ea` |
| Flag 2 | Robots.txt + Directory | Explorer répertoires interdits | Robots.txt → `/secret-info/flag.txt` | `FLAG2_[hash]` |
| Flag 3 | FTP Anonymous | Connexion FTP anonyme | `ftp target.ine.local` (anonymous) | `FLAG3_557062aaacb3418e858496ef0b5aa6e0` |
| Flag 4 | Database enumeration | Connexion MySQL avec creds | `mysql -u db_admin -p -h target.ine.local` | `FLAG4_bbf0089c312a41f884b457878c190195` |

### **Checklist de Sécurité Web**

#### ✅ **Toujours Vérifier:**
- [ ] `robots.txt`
- [ ] Scan Nmap complet (`-sC -sV` ou `-sVC -sS -O`)
- [ ] **Headers HTTP personnalisés** (chercher des flags dans les réponses)
- [ ] **Connexion FTP anonyme** (si port 21 ouvert)
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
- `nmap` - Scan de ports et services (`-sVC -sS -O` pour scan complet)
- `dirb` / `gobuster` - Brute-force de répertoires
- `httrack` - Mirror de site web
- `curl` / `wget` - Récupération de fichiers
- `ftp` - Client FTP pour connexions anonymes
- `mysql` / `mysqladmin` - Clients base de données

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

### **Conseils de Recherche:**
- **Dans les fichiers texte:** Les flags apparaissent souvent en clair
- **Dans les réponses HTTP:** Vérifier les headers et le contenu (headers personnalisés)
- **Dans les connexions FTP:** Toujours tester "anonymous" comme login
- **Dans les répertoires uploads:** Chercher des fichiers cachés ou renommés  
- **Dans les fichiers de config:** Chercher des credentials pour d'autres services
- **Dans les bases de données:** Les flags peuvent être des noms de DB ou dans les tables
- **Dans les mirrors:** Analyser tous les fichiers PHP/XML téléchargés

---

💡 **Conseil Final:** Restez méthodique, documentez tout, et n'hésitez pas à revenir aux bases si vous êtes bloqué. La patience et la persévérance sont clés dans les CTF !