# 🌐 Cheat Sheet : Nmap pour l'Énumération & Discrétion

Nmap est un outil **essentiel** pour scanner les ports, détecter les services et faire de l'énumération avancée (scripts NSE). Voici une cheat sheet complète avec une section dédiée à l’**évasion et la discrétion**.

---

## 🧭 1. Scan de base

```bash
nmap IP
```

---

## 🔍 2. Détection de ports

### 🔹 TCP connect scan (lent, mais fiable)

```bash
nmap -sT IP
```

### 🔹 SYN scan (rapide, silencieux)

```bash
nmap -sS IP
```

### 🔹 UDP scan

```bash
nmap -sU -p 53,123,161 IP
```

---

## 🧰 3. Détection de services et OS

```bash
nmap -sS -sV -O -Pn IP
```

- `-sV` : versions de services
- `-O` : détection OS
- `-Pn` : skip ping (utile si ICMP bloqué)

---

## 🧠 4. Scan complet de ports

```bash
nmap -p- IP
```

➡️ Tous les 65535 ports (par défaut, Nmap ne scanne que les 1000 plus courants)

---

## 🧪 5. Scripts NSE (Nmap Scripting Engine)

### 🔹 Liste des scripts

```bash
ls /usr/share/nmap/scripts/
```

### 🔹 Utiliser un script

```bash
nmap --script=http-title IP
```

### 🔹 Catégories utiles

```bash
nmap --script=vuln IP
nmap --script=default IP
nmap --script=smb-enum-shares,smb-enum-users -p 445 IP
```

---

## 🕵️ 6. Discrétion et évasion (stealth mode)

### 🔹 Pas de DNS, pas de ping

```bash
nmap -n -Pn IP
```

### 🔹 Modifier la vitesse de scan

```bash
nmap -T0 IP       # Paranoïaque
nmap -T1 IP       # Sneaky
```

### 🔹 Spoofing (adresse source falsifiée)

```bash
nmap -S FAKE_IP IP
```

### 🔹 Scan fragmenté (contourner IDS)

```bash
nmap -f IP
```

### 🔹 Randomisation d’ordre de scan

```bash
nmap --randomize-hosts -p 80 IP
```

### 🔹 Spoof MAC address

```bash
nmap --spoof-mac 0 IP           # 0 = MAC aléatoire
nmap --spoof-mac Cisco IP       # Ex: simulateur de matos Cisco
```

---

## 🧮 7. Scan de réseau / multiple hôtes

```bash
nmap 192.168.1.0/24
nmap -iL hosts.txt
```

---

## 📦 8. Sauvegarde des résultats

```bash
nmap -oA scan_result IP         # Formats .nmap, .xml, .gnmap
nmap -oN output.txt IP          # Format brut
```

---

## 🧠 Astuces

- Toujours commencer par un `-p-` pour ne rien rater
- Combine avec `--script` pour exploiter au max la détection de vulnérabilités
- Pour le stealth, couple Nmap avec un proxy ou VPN
- Teste d'abord sur un scope restreint avant de scanner un /16 complet

---

📁 À mettre dans `cheatsheets/` ou `cours/pentest/`
