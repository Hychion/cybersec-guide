# 🔍 Nmap & Rustscan - Cheatsheet complète eJPT

## 🚀 1. Nmap - Bases et syntaxe

### Syntaxe générale
```bash
nmap [options] [target(s)]
```

### Types de cibles
| Format | Exemple | Description |
|--------|---------|-------------|
| **IP unique** | `nmap 192.168.1.100` | Scanner une IP |
| **Plusieurs IPs** | `nmap 192.168.1.1 192.168.1.5 192.168.1.10` | IPs séparées par espaces |
| **Plage d'IPs** | `nmap 192.168.1.1-50` | Plage d'adresses |
| **Sous-réseau** | `nmap 192.168.1.0/24` | CIDR notation |
| **Domaine** | `nmap scanme.nmap.org` | Nom de domaine |
| **Fichier** | `nmap -iL targets.txt` | Liste de cibles dans un fichier |

---

## 🔎 2. Types de scan Nmap

### Scans de découverte d'hôtes
| Option | Description | Usage |
|--------|-------------|-------|
| `-sn` | Ping scan (pas de port scan) | `nmap -sn 192.168.1.0/24` |
| `-Pn` | Pas de ping (assume hôte up) | `nmap -Pn target` |
| `-PS<port>` | TCP SYN ping | `nmap -PS22,80,443 target` |
| `-PA<port>` | TCP ACK ping | `nmap -PA80 target` |
| `-PU<port>` | UDP ping | `nmap -PU53 target` |
| `-PE` | ICMP Echo ping | `nmap -PE target` |

### Scans de ports TCP
| Option | Description | Avantage | Détection |
|--------|-------------|----------|-----------|
| `-sS` | SYN scan (stealth) | Rapide, discret | Faible |
| `-sT` | TCP connect scan | Fiable | Moyenne |
| `-sA` | ACK scan | Bypass firewall | Faible |
| `-sW` | Window scan | Détection OS | Faible |
| `-sM` | Maimon scan | Bypass firewall | Faible |
| `-sF` | FIN scan | Très discret | Très faible |
| `-sX` | Xmas scan | Très discret | Très faible |
| `-sN` | Null scan | Très discret | Très faible |

### Scans UDP
| Option | Description | Usage |
|--------|-------------|-------|
| `-sU` | UDP scan | `nmap -sU target` |
| `-sU --top-ports 100` | Top 100 ports UDP | `nmap -sU --top-ports 100 target` |

---

## ⚙️ 3. Options de ports

### Spécification des ports
| Option | Exemple | Description |
|--------|---------|-------------|
| `-p <port>` | `-p 80` | Port spécifique |
| `-p <port1,port2>` | `-p 22,80,443` | Ports multiples |
| `-p <début-fin>` | `-p 1-1000` | Plage de ports |
| `-p-` | `-p-` | Tous les ports (1-65535) |
| `--top-ports <n>` | `--top-ports 100` | Les n ports les plus courants |
| `-F` | `-F` | Fast scan (100 ports courants) |

### Protocoles
| Option | Description |
|--------|-------------|
| `-p T:80,U:53` | TCP port 80 et UDP port 53 |
| `-pU:53,111,137` | Ports UDP spécifiques |
| `-pT:21-25,80,139,8080` | Ports TCP spécifiques |

---

## 🕵️ 4. Détection de services et versions

### Options de détection
| Option | Description | Exemple |
|--------|-------------|---------|
| `-sV` | Détection de version | `nmap -sV target` |
| `--version-intensity <0-9>` | Intensité de détection | `nmap -sV --version-intensity 9 target` |
| `--version-light` | Détection rapide | `nmap -sV --version-light target` |
| `--version-all` | Tests exhaustifs | `nmap -sV --version-all target` |

### Détection d'OS
| Option | Description | Exemple |
|--------|-------------|---------|
| `-O` | Détection OS | `nmap -O target` |
| `--osscan-limit` | Limiter scan OS | `nmap -O --osscan-limit target` |
| `--osscan-guess` | Forcer guess OS | `nmap -O --osscan-guess target` |

---

## 📜 5. Scripts NSE (Nmap Scripting Engine)

### Utilisation des scripts
| Option | Description | Exemple |
|--------|-------------|---------|
| `-sC` | Scripts par défaut | `nmap -sC target` |
| `--script <script>` | Script spécifique | `nmap --script http-title target` |
| `--script <catégorie>` | Catégorie de scripts | `nmap --script vuln target` |
| `--script-args` | Arguments pour scripts | `nmap --script http-brute --script-args userdb=users.txt target` |

### Catégories de scripts
| Catégorie | Description | Exemple |
|-----------|-------------|---------|
| **auth** | Authentification | `nmap --script auth target` |
| **broadcast** | Découverte broadcast | `nmap --script broadcast` |
| **brute** | Attaques par force brute | `nmap --script brute target` |
| **default** | Scripts par défaut | `nmap --script default target` |
| **discovery** | Découverte de services | `nmap --script discovery target` |
| **dos** | Déni de service | `nmap --script dos target` |
| **exploit** | Exploitation | `nmap --script exploit target` |
| **external** | Scripts externes | `nmap --script external target` |
| **fuzzer** | Fuzzing | `nmap --script fuzzer target` |
| **intrusive** | Scripts intrusifs | `nmap --script intrusive target` |
| **malware** | Détection malware | `nmap --script malware target` |
| **safe** | Scripts sûrs | `nmap --script safe target` |
| **version** | Détection de version | `nmap --script version target` |
| **vuln** | Vulnérabilités | `nmap --script vuln target` |

### Scripts essentiels par service
| Service | Scripts utiles |
|---------|----------------|
| **HTTP** | `http-title, http-headers, http-methods, http-robots.txt, http-enum` |
| **SMB** | `smb-os-discovery, smb-security-mode, smb-enum-shares, smb-vuln-*` |
| **FTP** | `ftp-anon, ftp-bounce, ftp-brute, ftp-vuln-cve2010-4221` |
| **SSH** | `ssh-hostkey, ssh-auth-methods, ssh-brute, ssh2-enum-algos` |
| **SMTP** | `smtp-commands, smtp-enum-users, smtp-open-relay, smtp-vuln-*` |
| **DNS** | `dns-brute, dns-zone-transfer, dns-recursion` |
| **MySQL** | `mysql-info, mysql-brute, mysql-empty-password, mysql-users` |

---

## ⏱️ 6. Timing et performance

### Templates de timing
| Option | Niveau | Description | Usage |
|--------|--------|-------------|-------|
| `-T0` | Paranoid | Très lent, furtif | Éviter détection |
| `-T1` | Sneaky | Lent, furtif | Éviter détection |
| `-T2` | Polite | Lent, peu intrusif | Éviter surcharge réseau |
| `-T3` | Normal | Défaut | Usage normal |
| `-T4` | Aggressive | Rapide | Réseaux rapides |
| `-T5` | Insane | Très rapide | Réseaux très rapides |

### Options de performance
| Option | Description | Exemple |
|--------|-------------|---------|
| `--min-rate <n>` | Paquets minimum par seconde | `nmap --min-rate 1000 target` |
| `--max-rate <n>` | Paquets maximum par seconde | `nmap --max-rate 5000 target` |
| `--max-parallelism <n>` | Scans parallèles max | `nmap --max-parallelism 100 target` |
| `--scan-delay <time>` | Délai entre probes | `nmap --scan-delay 1s target` |

---

## 🔥 7. Commandes Nmap essentielles pour l'eJPT

### Reconnaissance de base
| Commande | Description |
|----------|-------------|
| `nmap -sn 192.168.1.0/24` | Découverte d'hôtes |
| `nmap -sS -O target` | Scan SYN + OS detection |
| `nmap -sV -sC target` | Scan version + scripts défaut |
| `nmap -A target` | Scan agressif (tout) |
| `nmap -p- target` | Scan tous les ports |

### Scans spécialisés
| Commande | Description |
|----------|-------------|
| `nmap -sU --top-ports 100 target` | Top 100 ports UDP |
| `nmap --script vuln target` | Scan de vulnérabilités |
| `nmap -sS -sV -p 80,443 --script http-* target` | Énumération web complète |
| `nmap -p 139,445 --script smb-* target` | Énumération SMB complète |
| `nmap -sS -O -sV --script=banner target` | Banner grabbing |

### Scans furtifs
| Commande | Description |
|----------|-------------|
| `nmap -sS -T1 -f target` | Scan SYN lent + fragmentation |
| `nmap -sF -T0 target` | Scan FIN très lent |
| `nmap -D RND:10 target` | Decoy scan (10 leurres) |
| `nmap -S <spoofed_ip> target` | Spoof source IP |

---

## ⚡ 8. Rustscan - Le scanner rapide

### Installation
```bash
# Debian/Ubuntu
wget https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb
dpkg -i rustscan_2.0.1_amd64.deb

# Cargo
cargo install rustscan

# Docker
docker run -it --rm --name rustscan rustscan/rustscan:2.0.1
```

### Syntaxe de base
```bash
rustscan [OPTIONS] <target>
```

### Commandes Rustscan essentielles
| Commande | Description |
|----------|-------------|
| `rustscan -a target` | Scan rapide de base |
| `rustscan -a target -p 1-1000` | Ports spécifiques |
| `rustscan -a target --ulimit 5000` | Augmenter limite |
| `rustscan -a target -t 2000` | Timeout personnalisé |
| `rustscan -a target -b 4500` | Batch size |

### Options importantes
| Option | Description | Exemple |
|--------|-------------|---------|
| `-a, --addresses` | Adresses cibles | `rustscan -a 192.168.1.1,192.168.1.5` |
| `-p, --ports` | Ports spécifiques | `rustscan -a target -p 22,80,443` |
| `-r, --range` | Plage de ports | `rustscan -a target -r 1-1000` |
| `--top` | Top ports | `rustscan -a target --top` |
| `-u, --ulimit` | Limite de fichiers | `rustscan -a target -u 10000` |
| `-t, --timeout` | Timeout | `rustscan -a target -t 5000` |
| `-b, --batch-size` | Taille batch | `rustscan -a target -b 10000` |
| `--accessible` | Ports accessibles seulement | `rustscan -a target --accessible` |

---

## 🔄 9. Intégration Rustscan + Nmap

### Rustscan avec Nmap backend
| Commande | Description |
|----------|-------------|
| `rustscan -a target -- -sV` | Rustscan + détection version |
| `rustscan -a target -- -sC` | Rustscan + scripts par défaut |
| `rustscan -a target -- -A` | Rustscan + scan agressif |
| `rustscan -a target -- -sV -sC -O` | Scan complet |

### Workflow optimal eJPT
```bash
# 1. Découverte rapide avec Rustscan
rustscan -a target --accessible

# 2. Scan détaillé avec Nmap sur ports trouvés
nmap -sV -sC -p <ports_trouvés> target

# Ou en une commande
rustscan -a target -- -sV -sC -A
```

---

## 📊 10. Output et formats

### Formats de sortie Nmap
| Option | Format | Usage |
|--------|--------|-------|
| `-oN <file>` | Normal | `nmap -oN scan.txt target` |
| `-oX <file>` | XML | `nmap -oX scan.xml target` |
| `-oG <file>` | Grepable | `nmap -oG scan.grep target` |
| `-oA <basename>` | Tous formats | `nmap -oA scan target` |
| `-oS <file>` | Script kiddie | `nmap -oS scan.skid target` |

### Verbose et debug
| Option | Description |
|--------|-------------|
| `-v` | Verbose |
| `-vv` | Très verbose |
| `-d` | Debug |
| `-dd` | Debug détaillé |
| `--reason` | Raison du statut |
| `--open` | Ports ouverts seulement |
| `--packet-trace` | Trace des paquets |

---

## 🎯 11. Exemples pratiques pour l'eJPT

### Reconnaissance initiale
```bash
# Découverte d'hôtes
nmap -sn 192.168.1.0/24

# Scan rapide des hôtes trouvés
rustscan -a 192.168.1.100,192.168.1.105,192.168.1.110

# Scan détaillé
nmap -sV -sC -O 192.168.1.100
```

### Énumération de services
```bash
# Web
nmap -p 80,443,8080 --script http-* target

# SMB
nmap -p 139,445 --script smb-* target

# SSH
nmap -p 22 --script ssh-* target

# FTP
nmap -p 21 --script ftp-* target
```

### Scan de vulnérabilités
```bash
# Scan général de vulnérabilités
nmap --script vuln target

# Vulnérabilités spécifiques
nmap --script smb-vuln-* target
nmap --script http-vuln-* target
```

---

## 💡 12. Conseils et astuces eJPT

### Workflow recommandé
1. **Ping sweep** : `nmap -sn network/24`
2. **Rustscan rapide** : `rustscan -a targets`
3. **Nmap détaillé** : `nmap -sV -sC -p ports target`
4. **Scripts spécialisés** : `nmap --script service-* target`
5. **Vulnérabilités** : `nmap --script vuln target`

### Optimisations eJPT
```bash
# Scan rapide mais complet
nmap -sS -sV -sC --top-ports 1000 -T4 target

# Alternative avec Rustscan
rustscan -a target -u 5000 -- -sV -sC

# Pour réseaux lents
nmap -sS -sV --top-ports 100 -T3 target
```

### Scripts NSE prioritaires eJPT
```bash
# HTTP
nmap --script http-title,http-headers,http-methods,http-robots.txt target

# SMB (très important)
nmap --script smb-os-discovery,smb-security-mode,smb-enum-shares target

# Vulnérabilités critiques
nmap --script smb-vuln-ms17-010,http-vuln-*,ftp-vuln-* target
```

---

## 🔧 13. Dépannage et limitations

### Problèmes courants
| Problème | Solution |
|----------|----------|
| **Scan lent** | Utiliser `-T4` ou `--min-rate 1000` |
| **Ports filtrés** | Essayer `-sA` ou `-sF` |
| **Pas de réponse** | Utiliser `-Pn` |
| **Permission denied** | Lancer en tant que root |
| **Timeout** | Augmenter `--host-timeout` |

### Limitations
- **Rustscan** : Pas de détection de service native
- **Nmap UDP** : Très lent par nature
- **Scripts NSE** : Peuvent être bruyants
- **Scan complet** : Très long sur tous les ports

---

## 📝 14. Aide-mémoire one-liners

### Découverte réseau
```bash
# Hosts up
nmap -sn 192.168.1.0/24 | grep "Nmap scan report" | cut -d' ' -f5

# Ports ouverts uniquement
nmap --open target | grep "^[0-9]"
```

### Scan express
```bash
# Scan ultra-rapide
rustscan -a target --accessible -- -sV

# Top 1000 ports avec services
nmap -sS -sV --top-ports 1000 -T4 target

# Vulnérabilités express
nmap --script vuln --script-args vulns.short target
```

**🎯 Conseil final pour l'eJPT :** Commence toujours par `rustscan` pour la vitesse, puis utilise `nmap -sV -sC` sur les ports trouvés. Cette combinaison est optimale pour l'examen chronométré !