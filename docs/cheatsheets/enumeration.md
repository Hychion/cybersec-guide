# Enumeration
# 🗂️ Cheat Sheet : find (Énumération Linux)

La commande `find` est essentielle pour l’énumération lors de phases de pentest ou d’élévation de privilèges sous Linux.

---

## 📌 Syntaxe de base

```bash
find [chemin] [critères] [actions]
```

---

## 🎯 Cas d’usage pratiques

### 🔎 Rechercher un fichier par nom

```bash
find / -name "nom_du_fichier"
```

🔸 Exemple :
```bash
find / -name passwd 2>/dev/null
```

---

### 🔐 Fichiers SUID (potentiellement exploitables pour privesc)

```bash
find / -type f -perm -4000 2>/dev/null
```

---

### 🔐 Fichiers SGID

```bash
find / -type f -perm -2000 2>/dev/null
```

---

### 👀 Fichiers appartenant à un utilisateur

```bash
find / -user nom_utilisateur 2>/dev/null
```

---

### 🧑‍🏫 Fichiers appartenant à un groupe

```bash
find / -group nom_du_groupe 2>/dev/null
```

---

### 📁 Fichiers world-writable

```bash
find / -type f -perm -0002 2>/dev/null
```

---

### 📁 Dossiers world-writable

```bash
find / -type d -perm -0002 2>/dev/null
```

---

### 📅 Fichiers modifiés récemment (moins de X jours)

```bash
find / -type f -mtime -3 2>/dev/null
```

---

### 🔤 Rechercher par extension de fichier

```bash
find / -type f -name "*.sh" 2>/dev/null
```

---

### 🧨 Fichiers exécutables appartenant à root

```bash
find / -type f -executable -user root 2>/dev/null
```

---

### 🔍 Fichiers contenant une chaîne de texte

```bash
find / -type f -exec grep -i "mot" {} \; 2>/dev/null
```

---

## 📦 Bonus : find avec xargs

```bash
find / -name "*.log" 2>/dev/null | xargs grep "mot"
```

---

## 🧙 Tips pentest / privesc

- Repérer les **scripts modifiables** (souvent lancés par cron)
- Inspecter les fichiers dans `/etc`, `/var/backups`, `/home/*/`
- Combiner `find` + `grep` pour rechercher des secrets (`pass`, `pwd`, `token`, etc.)