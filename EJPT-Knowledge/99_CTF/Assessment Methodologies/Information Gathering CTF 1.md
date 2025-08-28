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
   nmap target.ine.local -sC -sV
   ```
   - Identifier les services et leurs versions
   - Noter les technologies utilisées

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

#### **Question 5:** *"Certain files may reveal something interesting when mirrored."*
- **Action:** Créer un mirror complet du site
- **Commande:** `httrack http://target.ine.local -O target.html`
- **Emplacement:** Fichier `xmlrpc0db0.php` dans le mirror
- **🏁 Flag:** `e79d9c81cc384cdd91bbc563fd61b7ee`

### **Assessment Methodologies - Information Gathering**

| Question | Challenge Type | Action | Commande/Méthode | Flag Attendu |
|----------|---------------|--------|------------------|--------------|
| Q1 | Robots.txt | Vérifier fichier standard | `curl http://target.ine.local/robots.txt` | `f2ee2d09e076462eadce8807895a4461` |
| Q2 | Version identification | Scanner les services | `nmap -sC -sV target` | `3395843029c743ddb00c9adac8b2c7cc` |
| Q3 | Directory browsing | Brute-force répertoires | `dirb http://target.ine.local` | `ccca869e58f54c02b0fa4f9b5a1ee84f` |
| Q4 | Backup files | Scanner avec extensions | `dirb [...] -X .bak,.sql,.zip` | `de9e6050a6de44daa74e91e87b3112f3` |
| Q5 | Mirror analysis | Copie locale complète | `httrack http://target.ine.local` | `e79d9c81cc384cdd91bbc563fd61b7ee` |

### **Checklist de Sécurité Web**

#### ✅ **Toujours Vérifier:**
- [ ] `robots.txt`
- [ ] Scan Nmap complet (`-sC -sV`)
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
- `nmap` - Scan de ports et services
- `dirb` / `gobuster` - Brute-force de répertoires
- `httrack` - Mirror de site web
- `curl` / `wget` - Récupération de fichiers

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
| **Directory Browsing** | Répertoire `wp-content/uploads/` | Brute-force puis navigation |
| **Backup Files** | Fichier `wp-config.bak` | Scan avec extensions + curl |
| **Mirror Analysis** | Fichier `xmlrpc0db0.php` | Analyse du mirror local |

### **Conseils de Recherche:**
- **Dans les fichiers texte:** Les flags apparaissent souvent en clair
- **Dans les réponses HTTP:** Vérifier les headers et le contenu
- **Dans les répertoires uploads:** Chercher des fichiers cachés ou renommés
- **Dans les mirrors:** Analyser tous les fichiers PHP/XML téléchargés

---

💡 **Conseil Final:** Restez méthodique, documentez tout, et n'hésitez pas à revenir aux bases si vous êtes bloqué. La patience et la persévérance sont clés dans les CTF !