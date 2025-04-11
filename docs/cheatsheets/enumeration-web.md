# 🌐 Énumération Web (Cheat Sheet Pentest Web)

Dans le cadre d’un **pentest Web**, la phase d’énumération consiste à découvrir toutes les ressources accessibles (répertoires, fichiers, endpoints API, technologies, vulnérabilités).

---

## 🧭 1. Détection de technologies

### 🔍 whatweb

```bash
whatweb http://target.com
```

### 🔍 Wappalyzer (addon navigateur)

Permet une vue rapide des technologies côté client (CMS, JS libs, etc.).

---

## 📁 2. Brute-force de répertoires et fichiers

### 🔨 gobuster

```bash
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -t 50
```

🔸 Options utiles :
- `-x php,html,txt` → extensions à tester
- `-k` → ignorer les certificats SSL invalides

### ⚡ ffuf (rapide & puissant)

```bash
ffuf -u http://target.com/FUZZ -w /usr/share/wordlists/dirb/common.txt
```

🔸 Peut aussi être utilisé pour fuzz des paramètres :

```bash
ffuf -u http://target.com/page.php?file=FUZZ -w wordlist.txt
```

### 📂 dirb

```bash
dirb http://target.com
```

---

## 🔑 3. Authentification & Bruteforce

### 🗝️ hydra (brute force login)

```bash
hydra -l admin -P rockyou.txt target.com http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials"
```

---

## 📡 4. Analyse de réponses HTTP

### 📦 curl

```bash
curl -I http://target.com     # Headers
curl -sL http://target.com    # Suivre redirections
```

### 📦 httpx

```bash
httpx -u http://target.com -title -tech-detect -status-code
```

---

## 🕳️ 5. Recherche de failles courantes

### 🧪 nikto (scanner de vulnérabilités Web)

```bash
nikto -h http://target.com
```

### 🐍 sqlmap (injection SQL)

```bash
sqlmap -u "http://target.com/page.php?id=1" --batch --dbs
```

---

## 🔍 6. Autres outils utiles

- `nmap -p80,443 -sV --script=http*` : scans NSE http
- `burpsuite` : proxy pour inspection/modification des requêtes
- `wfuzz` : alternative avancée à ffuf/gobuster

---

## 📚 Wordlists recommandées

- `/usr/share/wordlists/dirb/common.txt`
- `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
- `SecLists` (GitHub) : https://github.com/danielmiessler/SecLists

---

## 🧠 Conseils

- Toujours faire l’énumération en HTTP **et** HTTPS
- Tester avec et sans slash (`/admin` vs `/admin/`)
- Surveille les codes HTTP : `200`, `403`, `401`, `500`
- Utilise Burp pour repérer les paramètres et comportements dynamiques

---

📁 Ce fichier peut aller dans `docs/cheatsheets/` ou `docs/cours/pentest/`
