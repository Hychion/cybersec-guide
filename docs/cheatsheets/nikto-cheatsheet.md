# 🛡️ Nikto Cheat Sheet

> Un guide rapide pour utiliser **Nikto**, un scanner de vulnérabilités web open source.

---

## 📌 Qu'est-ce que Nikto ?

Nikto est un scanner en ligne de commande conçu pour tester les serveurs web et détecter :

- Fichiers/répertoires dangereux
- Scripts obsolètes ou vulnérables
- Mauvaises configurations
- Fuites d’informations via headers ou bannières
- Failles connues dans les services HTTP/HTTPS

---

## 🚀 Commandes de base

```bash
nikto -h http://example.com
```
> Scan HTTP simple

```bash
nikto -h https://example.com -p 443
```
> Scan HTTPS sur port 443

```bash
nikto -h http://192.168.1.10
```
> Scan via une IP locale

---

## ⚙️ Options utiles

| Option | Description |
|--------|-------------|
| `-h` | Spécifie l'hôte (URL ou IP) |
| `-p` | Définit le port |
| `-ssl` | Force l’utilisation du protocole HTTPS |
| `-Display V` | Affiche plus de détails pendant le scan |
| `-output fichier.txt` | Enregistre le résultat dans un fichier |
| `-Tuning x` | Sélectionne les types de tests (voir ci-dessous) |
| `-evasion` | Techniques d’évasion pour contourner les protections |
| `-Plugins` | Spécifie un ou plusieurs plugins à utiliser |

---

## 🧪 Modes de test (option `-Tuning`)

| Code | Type de tests |
|------|----------------|
| 0 | Tests généraux |
| 1 | Fichiers dangereux |
| 2 | Scripts obsolètes |
| 3 | Fichiers de configuration |
| 4 | Informations d’identification par défaut |
| 5 | Tests d'injection |
| 6 | Tests de scripts spécifiques |
| 7 | Identification de logiciel |
| 8 | Répertoire de scripts |
| 9 | Vulnérabilités divers |

**Exemple :**  
```bash
nikto -h http://site.com -Tuning 012
```

---

## 🕵️ Utilisation via Tor

```bash
proxychains nikto -h http://siteonion.onion
```

Assure-toi que Tor est lancé et `proxychains.conf` est configuré avec :
```conf
socks5 127.0.0.1 9050
```

---

## 📁 Exemple de scan avec export

```bash
nikto -h https://target.com -output rapport.txt
```

---

## ⚠️ Notes

- **Nikto n’est pas furtif** : il est détectable facilement dans les logs serveur.
- Utiliser Nikto **avec autorisation uniquement** – c’est un outil de pentest, pas un outil offensif illégal.
- Combine-le avec d’autres outils comme **WhatWeb**, **Dirb**, **sqlmap** pour une analyse plus poussée.

---

## 📚 Ressources

- [Site officiel de Nikto](https://cirt.net/Nikto2)
- [Code source GitHub](https://github.com/sullo/nikto)

---

> 🧠 _Pour un pentest web efficace, Nikto est un bon point de départ mais ne remplace pas une analyse manuelle approfondie._
