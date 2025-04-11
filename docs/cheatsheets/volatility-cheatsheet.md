# 🧠 Cheat Sheet : Volatility (Analyse Mémoire)

Volatility est un framework d’analyse forensique de mémoire RAM. Voici une cheat sheet claire pour l’utiliser à la fois via **Docker** et directement sur **Debian** (Kali, Parrot, etc.).

---

## 🐳 Utilisation via Docker (méthode rapide)

### 📦 1. Lancer Volatility3 en Docker

```bash
docker run -v /chemin/vers/dump:/data --rm jpsvolatility/volatility3 -f /data/memdump.raw windows.info
```

🔹 `-v` : monter le dossier contenant le dump  
🔹 `/data/memdump.raw` : chemin du fichier mémoire  
🔹 `windows.info` : plugin à exécuter

---

### 🔁 Exemple complet avec cincan/volatility (Volatility2)

```bash
docker run --rm -v /c/Users/quent/Downloads/MemLabs-Lab1:/tmp -ti cincan/volatility -f /tmp/Challenge.raw imageinfo
```

🔹 Analyse du profil mémoire avec `imageinfo`.

```bash
docker run --rm -v /c/Users/quent/Downloads/MemLabs-Lab1:/tmp -ti cincan/volatility -f /tmp/MemoryDump_Lab1.raw --profile=Win7SP1x64 filescan
```

🔹 Scan des fichiers en mémoire avec le profil spécifié.

---

## 🐧 Utilisation native sur Debian

### 📦 1. Installation (Volatility2)

```bash
sudo apt install volatility
```

### 📦 2. Installation (Volatility3 - recommandé)

```bash
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
python3 -m pip install -r requirements.txt
```

🔗 [https://github.com/volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3)

---

## 🔌 Plugins additionnels (Volatility 3)

### 📦 Volatility Plugins Community

```bash
git clone https://github.com/volatilityfoundation/community.git
```

🔗 [https://github.com/volatilityfoundation/community](https://github.com/volatilityfoundation/community)

### 📦 Windows kernel symbols (optionnel)

```bash
git clone https://github.com/volatilityfoundation/volatility3-symbols.git
```

🔗 [https://github.com/volatilityfoundation/volatility3-symbols](https://github.com/volatilityfoundation/volatility3-symbols)

---

## 📚 Exercices pratiques

🧪 Exos mémoire en ligne :  
🔗 [https://github.com/stuxnet999/MemLabs](https://github.com/stuxnet999/MemLabs)

---

## 🔍 Plugins Utiles

| Plugin              | Description                              |
|---------------------|------------------------------------------|
| `windows.info`      | Infos sur le dump (OS, version, etc.)    |
| `windows.pslist`    | Liste des processus                      |
| `windows.psscan`    | Processus cachés                         |
| `windows.cmdline`   | Commandes utilisées                      |
| `windows.netscan`   | Connexions réseau actives                |
| `windows.filescan`  | Recherche de fichiers                    |
| `windows.hashdump`  | Extraction des hash utilisateurs         |
| `windows.svcscan`   | Services Windows                         |
| `windows.malfind`   | Détection de code injecté en mémoire     |

---

## 🧰 Commandes classiques

### 🔍 Lister les processus

```bash
python3 vol.py -f memdump.raw windows.pslist
```

### 🧑‍💻 Afficher les commandes utilisées

```bash
python3 vol.py -f memdump.raw windows.cmdline
```

### 🕵️ Détecter les connexions réseau

```bash
python3 vol.py -f memdump.raw windows.netscan
```

### 🔐 Extraire les hash NTLM

```bash
python3 vol.py -f memdump.raw windows.hashdump
```

---

## 💡 Conseils

- Assure-toi que ton fichier de dump RAM est **complet** et **non corrompu**
- Commence toujours par `imageinfo` ou `windows.info` pour bien identifier le profil
- Utilise Docker si tu ne veux pas installer Python + dépendances
- Combine avec `strings`, `binwalk`, ou `foremost` pour des analyses hybrides

---

📁 À placer dans `docs/cheatsheets/` ou `docs/forensic/`
