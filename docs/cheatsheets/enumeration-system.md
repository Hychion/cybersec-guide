# 🖥️ Énumération Locale (Post-exploitation / Privilege Escalation)

Lorsqu'on accède à une machine via une faille, la **première étape** est de faire un maximum d'**énumération locale** pour comprendre l’environnement et identifier des **failles potentielles d’escalade de privilèges** ou des informations sensibles.

---

## 📌 Objectifs principaux

- Connaître l’OS, l’utilisateur courant, les services lancés
- Repérer les fichiers sensibles, permissions mal configurées
- Détecter les tâches planifiées, scripts exécutés par root
- Trouver des failles privesc connues

---

## 👣 1. Informations système

```bash
uname -a                      # Info noyau
cat /etc/os-release           # Distro
hostname                      # Nom de la machine
id                            # Infos utilisateur courant
whoami                        # Utilisateur
```

---

## 🧑‍💻 2. Utilisateurs et groupes

```bash
cat /etc/passwd               # Tous les utilisateurs
cut -d: -f1 /etc/passwd       # Liste simple
getent passwd                 # Similaire

cat /etc/group                # Groupes
```

---

## 📂 3. Fichiers et permissions sensibles

### 🔐 Fichiers SUID

```bash
find / -type f -perm -4000 2>/dev/null
```

### 🔐 Fichiers SGID

```bash
find / -type f -perm -2000 2>/dev/null
```

### 📁 World-writable

```bash
find / -type f -perm -0002 2>/dev/null
find / -type d -perm -0002 2>/dev/null
```

---

## 🧾 4. Fichiers d’historique et mots de passe

```bash
cat ~/.bash_history
ls -la /home/*/
grep -i 'pass\|password\|pwd' /home/*/.*
```

---

## 🛠️ 5. Processus et services

```bash
ps aux
top
netstat -tulpn
ss -tulpn
systemctl list-units --type=service
```

---

## 🧪 6. Permissions sudo

```bash
sudo -l
```

➡️ Chercher des commandes exécutable en root sans mot de passe (NOPASSWD)

---

## 🧱 7. Capabilities Linux

```bash
getcap -r / 2>/dev/null
```

➡️ Certaines capacités comme `cap_setuid` ou `cap_net_bind_service` peuvent être exploitables

---

## 🕳️ 8. Cron Jobs & scripts root

```bash
cat /etc/crontab
ls -la /etc/cron.*
```

➡️ Vérifier si des scripts sont modifiables par l’utilisateur courant

---

## 📦 9. Outils d’automatisation (recommandés)

### 📌 linpeas

```bash
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

### 📌 pspy (pour surveiller les tâches root en live)

```bash
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
chmod +x pspy64
./pspy64
```

---

## 🧠 Conseils

- Toujours vérifier les permissions des fichiers exécutés automatiquement
- Pense à regarder `/opt/`, `/scripts`, `/dev/shm`, `/tmp`
- Combine les commandes `find`, `grep`, `ls`, `cat` pour gagner du temps

---

📁 Fichier prêt à être ajouté à ta section `cheatsheets/` ou `cours/privilege-escalation/`
