# 🐧 Linux Command Cheat Sheet – Utilisation Système et Post-Exploitation

Cette cheat sheet contient les **commandes Linux les plus importantes**, utiles pour la gestion système, le pentest, l’élévation de privilèges et l’analyse forensique.

---

## 📁 1. Système de fichiers & navigation

```bash
pwd                         # Chemin courant
cd /chemin                  # Aller à un répertoire
ls -la                      # Liste détaillée + fichiers cachés
tree                        # Arborescence
df -h                       # Espace disque par partition
du -sh *                    # Taille de chaque fichier/dossier
mount                       # Périphériques montés
umount /mnt/usb             # Démonter une partition
```

---

## 🧑‍💻 2. Utilisateurs & groupes

```bash
whoami                      # Utilisateur courant
id                          # UID, GID, groupes
users                       # Utilisateurs connectés
groups                      # Groupes de l'utilisateur
adduser test                # Ajouter un utilisateur
passwd test                 # Définir un mot de passe
usermod -aG sudo test       # Ajouter aux sudoers
```

---

## 🔐 3. Permissions & sécurité

```bash
chmod +x script.sh          # Rendre exécutable
chmod 755 fichier           # Droits rwxr-xr-x
chown user:group fichier    # Changer propriétaire
umask                       # Masque de création de fichiers
getfacl fichier             # Lire ACL
setfacl -m u:user:rwx file  # Modifier ACL
```

---

## 📦 4. Packages

### Debian / Ubuntu

```bash
apt update && apt upgrade
apt install nom_du_package
dpkg -l                     # Liste des paquets
```

### Red Hat / CentOS

```bash
yum install package
rpm -qa
```

---

## 🔄 5. Services & processus

```bash
ps aux                      # Tous les processus
top / htop                  # En direct
kill -9 PID                 # Forcer l’arrêt d’un processus
systemctl status service
systemctl start/stop service
```

---

## 🕵️ 6. Monitoring & logs

```bash
journalctl -xe             # Logs système
dmesg                      # Messages du noyau
last                       # Derniers logins
who / w                    # Qui est connecté ?
uptime                     # Durée de fonctionnement
```

---

## 🌐 7. Réseau

```bash
ip a                       # Interfaces réseau
ip r                       # Routes
ping -c 4 1.1.1.1
ss -tuln                   # Ports ouverts
netstat -tulnp             # (équivalent)
hostname -I                # IP locale
```

---

## 🔍 8. Recherche et manipulation

```bash
find / -name "*.conf" 2>/dev/null
grep -i "password" fichier.txt
awk '{print $1}' fichier
cut -d':' -f1 /etc/passwd
strings fichier_binaire
```

---

## 🗜️ 9. Compression & archive

```bash
tar -cvf archive.tar dossier/
tar -xvf archive.tar
tar -czvf archive.tar.gz dossier/
zip -r archive.zip dossier/
unzip archive.zip
```

---

## 🧪 10. Forensic & post-exploitation

```bash
cat ~/.bash_history               # Historique
ls -la /home/*/                   # Répertoires utilisateurs
find / -perm -4000               # SUID
getcap -r / 2>/dev/null          # Capabilities
sudo -l                          # Commandes sudo disponibles
```

---

📁 À placer dans `docs/cheatsheets/commandes-linux.md`