Official : github.com/bee-san/RustScan

# 🦀 RustScan - Cheatsheet Complet

RustScan est un scanner de ports ultra-rapide écrit en Rust, conçu pour la rapidité, la sécurité et la flexibilité. Cette cheatsheet explore **toutes les options**, **scénarios pratiques**, **intégrations** et **tips avancés** pour tirer le meilleur de cet outil.

---

## 📦 Installation

### Depuis les dépôts
```bash
sudo pacman -S rustscan  # Arch
sudo apt install rustscan # Debian/Ubuntu
```

### Depuis GitHub
```bash
cargo install rustscan
```

---

## 🔧 Commande de base

```bash
rustscan -a <IP>
```

---

## 📖 Aide & Version

| Option | Description |
|--------|-------------|
| `--help` | Affiche l'aide complète |
| `--version` | Affiche la version de RustScan |

---

## 🎛️ Options de Scan

| Option | Description |
|--------|-------------|
| `-a`, `--address` | Adresse IP cible |
| `-p`, `--port <PORTS>` | Liste ou plage de ports à scanner (ex: `80,443,8000-8100`) |
| `--range <START-END>` | Plage entière à scanner (équivalent rapide au `-p`) |
| `--timeout <MILLISEC>` | Temps d'attente en ms pour chaque port |
| `--batch-size <NUM>` | Nombre de ports scannés simultanément |
| `--ulimit <NUM>` | Définit la limite de fichiers ouverts |
| `--no-config` | Ignore les fichiers de config utilisateur |
| `--accessibility` | Active la sortie lisible pour les lecteurs d'écran |

---

## 🤫 Modes de sortie

| Option | Description |
|--------|-------------|
| `--quiet` | N'affiche que les ports ouverts |
| `-g`, `--greppable` | Format de sortie lisible via `grep`, `awk`, etc |
| `-b`, `--banner` | Affiche la bannière RustScan à l'exécution |

---

## 🧪 Exemples de Scans Simples

### Scanner tous les ports
```bash
rustscan -a 192.168.1.10 --range 1-65535
```

### Scanner une liste spécifique
```bash
rustscan -a 10.0.0.1 -p 22,80,443,3306
```

### Scanner silencieusement avec timeout custom
```bash
rustscan -a 192.168.1.15 --timeout 2000 --quiet
```

### Scanner avec plus de threads
```bash
rustscan -a 192.168.1.1 --batch-size 5000
```

---

## 🔄 Intégration avec Nmap

```bash
rustscan -a 192.168.1.1 -- -A -sC -sV
```

➡️ Les ports ouverts trouvés seront transmis à Nmap pour un scan approfondi.

---

## 🧩 Multi-Scan (Adresses multiples)

### Avec un fichier :
```bash
rustscan -a targets.txt
```
Où `targets.txt` contient :
```
192.168.1.1
192.168.1.2
192.168.1.3
```

### Avec des sous-réseaux :
RustScan ne supporte pas nativement les CIDR, mais tu peux générer une liste via :
```bash
ipcalc -n 192.168.1.0/24 | awk '/HostMin/,/HostMax/' > ips.txt
rustscan -a ips.txt
```

---

## 🧠 Tips Avancés

- **Maximiser la vitesse** : utiliser `--batch-size` à un nombre élevé (ex: 10000), ajuster `--timeout` intelligemment.
- **Utilisation furtive** : combiner avec VPN, Tor, ou proxy pour anonymiser.
- **Parsing automatique** : utiliser `--greppable` pour chaîner avec des outils :
```bash
rustscan -a 192.168.1.1 --greppable | grep 80
```
- **Integration avec scripts** :
```bash
for ip in $(cat ips.txt); do rustscan -a $ip -- -sV -oN scan_$ip.txt; done
```

---

## 🚀 Cas d’usage typiques

- **Pentesting rapide en réseau local**
- **Découverte de services dans une plage IP**
- **Pré-analyse avant une phase Nmap**
- **Automatisation dans un pipeline CI/CD de sécurité**

---

## 📁 Exemple de config `.rustscan.toml`

```toml
[settings]
ports = "1-1000"
batch_size = 3000
timeout = 1500
greppable = true
```

---

📌 **Note** : RustScan ne supporte pas encore le scanning UDP.

---

## ❤️ Projet GitHub

https://github.com/RustScan/RustScan

---

Fait avec 💀 depuis ton shell Arch Hynix. Prêt pour tous les audits ⚡
