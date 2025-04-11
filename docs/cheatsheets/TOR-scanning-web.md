
📦 Fichier prêt : proxychains-nmap-onion-guide.md

# 🧅 Guide Complet : Scanner un Service .onion avec Proxychains + Nmap

> 🎯 Objectif : Scanner un service `.onion` en passant par le réseau Tor via Proxychains + Nmap, dans un cadre **légal, éducatif et sécurisé**.

---

## 🔧 Installation des Outils Requis

### 1. Mettre à jour le système

```bash
sudo apt update && sudo apt upgrade -y
```
### 2. Installer Tor

```bash
sudo apt install tor
sudo service tor start
```
### 3. Installer Proxychains
```bash
sudo apt install proxychains
```

Vérifie la config dans /etc/proxychains.conf :
Elle doit contenir la ligne suivante (souvent déjà en place) :
```bash
....
socks5  127.0.0.1 9050
```

## 🧪 Vérifier que Proxychains fonctionne avec Tor

Lance ce test :
```bash
proxychains curl http://check.torproject.org
```

Tu dois voir :

    ✅ "Congratulations. This browser is configured to use Tor."

## 🌐 Scanner un Service .onion avec Nmap via Proxychains
### Exemple simple
```bash
proxychains nmap -sT -Pn -n -p 80,443 exempleonion123.onion
```
### Explication des options :

    -sT : Scan TCP connect (obligatoire car le SYN scan ne marche pas via Tor)

    -Pn : Ne pas essayer de ping la cible (les .onion ne répondent pas)

    -n : Ne fait pas de résolution DNS

    -p : Ports à cibler (ici HTTP & HTTPS)

### Exemple plus complet (scan de ports supplémentaires)
```bash
proxychains nmap -sT -Pn -n -p 21,22,53,80,443,8080 exempleonion123.onion
```
    🕓 Attention : les scans via Tor sont lents, c’est normal !

## 🔐 Bonnes Pratiques (OPSEC)

    ✅ Utiliser une machine virtuelle (Kali, Parrot, Tails OS)

    ✅ Passer par un VPN avant Tor (double couche d’anonymat)

    ✅ Ne jamais scanner agressivement (pas de -A, pas de full scan sur .onion)

    ✅ Ne pas utiliser ton pseudo habituel sur des services .onion

    ✅ Ne jamais télécharger de fichiers .onion sans sandbox

## 📚 Références Utiles

    Tor Project

    Nmap

    Proxychains GitHub

    DarkFail – index des services .onion (à visiter via Tor)

## ⚠ Avertissement

    Ce guide est fourni exclusivement à des fins éducatives. L’utilisation d’outils de scan ou d’analyse doit toujours se faire dans le cadre de tests autorisés, de laboratoires personnels ou d’études légales. Toute mauvaise utilisation est sous votre propre responsabilité.