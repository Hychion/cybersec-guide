# 🖧 Énumération SMB & Active Directory (Windows Network)

Cette cheat sheet couvre l'énumération des **partages SMB** et des environnements **Active Directory** (AD), souvent rencontrés dans les réseaux Windows internes.

---

## 📁 1. Partages SMB (Server Message Block)

### 🔍 Enumération des partages

#### 📦 smbclient

```bash
smbclient -L //IP -N
```

🔸 `-L` = liste les partages  
🔸 `-N` = sans mot de passe

#### 📦 smbmap

```bash
smbmap -H IP
```

#### 📦 nmap (scripts NSE)

```bash
nmap -p445 --script=smb-enum-shares,smb-enum-users IP
```

---

### 🔐 Accéder à un partage SMB

```bash
smbclient //IP/partage -N
```

Ou avec authentification :

```bash
smbclient //IP/partage -U utilisateur
```

---

## 🧑‍💻 2. Énumération Active Directory (AD)

### 📋 enum4linux (outil de base)

```bash
enum4linux -a IP
```

🔹 Récupère :
- Infos système Windows
- Utilisateurs/domaines/groupes
- Partages, SID, etc.

---

### 📋 rpcclient

```bash
rpcclient -U "" IP
```

Puis dans la console RPC :

```bash
enumdomusers
querydominfo
enumalsgroups
```

---

### 📋 crackmapexec (très puissant)

```bash
crackmapexec smb IP -u '' -p '' --shares
crackmapexec smb IP --users
```

Avec un compte connu :

```bash
crackmapexec smb IP -u utilisateur -p motdepasse --groups
```

---

### 🧠 ldapsearch (si port 389 ouvert)

```bash
ldapsearch -x -h IP -b "dc=domain,dc=local"
```

🔸 Utile pour extraire des infos d’un annuaire LDAP/AD

---

## 🛠️ 3. Enumération utilisateurs

### 🧪 Utilisateurs via enum4linux :

```bash
enum4linux -U IP
```

### 🔍 Utilisateurs via usernames list :

```bash
crackmapexec smb IP -u userlist.txt -p '' --no-bruteforce
```

---

## 🔐 4. Vulnérabilités connues

### 🎯 Null sessions activées ?

```bash
rpcclient -U "" IP
```

Si tu obtiens un prompt `rpcclient>`, la session null est ouverte = GROSSE faille.

### 🎯 SMBv1 activé ?

```bash
nmap -p445 --script smb-protocols IP
```

---

## 🧠 Conseils Pentest

- Regarde toujours si le port 139 ou 445 est ouvert
- Essaie avec `-N` (anonyme) avant de forcer une auth
- Note les SID/RID pour user bruteforce ou privesc Windows
- Combine avec BloodHound si tu dumpes un AD plus tard

---

📁 À placer dans `cheatsheets/` ou `cours/forensic/` / `cours/reseaux/`
