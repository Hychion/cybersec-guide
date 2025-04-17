Official : github.com/bee-san/RustScan

# 🦀 RustScan Cheat Sheet

RustScan est un scanner de ports ultra-rapide écrit en Rust, conçu pour être à la fois rapide, sécurisé, et simple à utiliser. Ce fichier `.md` fournit une vue d'ensemble des principales options disponibles ainsi que des exemples d'utilisation.

---

## 📌 Commandes de base

### Afficher l'aide
```
rustscan --help
```

### Afficher la version
```
rustscan --version
```

---

## 🧰 Options Utiles

| Option | Description |
|--------|-------------|
| `-a`, `--address` | Spécifie l'adresse IP cible. Obligatoire. |
| `--range` | Définit une plage de ports à scanner (ex: `1-65535`) |
| `--batch-size` | Définit le nombre de ports scannés en parallèle |
| `--timeout` | Spécifie le temps limite d'attente pour chaque port (en ms) |
| `--quiet` | Active le mode silencieux (affiche uniquement les ports ouverts) |
| `-b`, `--banner` | Affiche une bannière RustScan à l'exécution |
| `-g`, `--greppable` | Format de sortie facilement analysable via grep/sed/etc |
| `--ulimit` | Définit une limite personnalisée pour les fichiers ouverts |
| `-p`, `--port` | Spécifie manuellement les ports à scanner |
| `-n`, `--no-config` | Ignore le fichier de configuration local |
| `--accessibility` | Active une sortie optimisée pour les lecteurs d'écran |

---

## 🔁 Intégration avec Nmap

RustScan peut être utilisé avec Nmap pour des analyses plus poussées après détection des ports ouverts :

```
rustscan -a 192.168.1.1 -- -A
```

---

## 💡 Exemples

### Scanner tous les ports sur une IP
```
rustscan -a 192.168.1.1 --range 1-65535
```

### Scanner avec un timeout personnalisé
```
rustscan -a 10.0.0.5 --timeout 1000
```

### Scanner en mode silencieux (quiet mode)
```
rustscan -a 192.168.1.1 --quiet
```

### Scanner avec batch-size ajusté
```
rustscan -a 10.10.10.10 --batch-size 2000
```

---

## 🔐 Pourquoi l’utiliser ?

- **Ultra rapide** grâce à Rust
- **Sécure** par design
- **Facilement scriptable**
- Compatible avec les audits discrets et pentests

---

