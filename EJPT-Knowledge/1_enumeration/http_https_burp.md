# HTTP Method Enumeration - Cheat Sheet

## Vue d'ensemble
Guide pratique pour l'énumération des méthodes HTTP et l'exploitation WebDAV sur applications web avec curl et Burp Suite.

## Phase 1: Reconnaissance Web

### Identification des pages accessibles
```bash
# Exploration manuelle des liens
http://demo.ine.local/login.php
http://demo.ine.local/post.php

# Découverte de répertoires cachés
dirb http://demo.ine.local
```

**Répertoires découverts:** css, img, js, mail, uploads, vendor

## Phase 2: Énumération avec CURL

### Test de la page d'accueil (index.php)

#### Méthodes supportées
```bash
# GET Request
curl -X GET demo.ine.local

# HEAD Request
curl -I demo.ine.local

# OPTIONS Request (révèle les méthodes autorisées)
curl -X OPTIONS demo.ine.local -v
```
**Résultat:** GET, HEAD, OPTIONS supportées

#### Méthodes non supportées
```bash
# POST Request (non autorisée)
curl -X POST demo.ine.local

# PUT Request (non autorisée)
curl -X PUT demo.ine.local
```

### Test de login.php

```bash
# Vérification des méthodes supportées
curl -X OPTIONS demo.ine.local/login.php -v
```
**Résultat:** GET, POST, HEAD, OPTIONS supportées

#### Test d'authentification
```bash
# POST avec credentials
curl -X POST demo.ine.local/login.php -d "name=john&password=password" -v
```
**Résultat:** Redirection 302 (authentification réussie)

### Test de post.php

```bash
curl -X OPTIONS demo.ine.local/post.php -v
```
**Résultat:** GET, POST, HEAD, OPTIONS supportées

## Phase 3: Exploitation WebDAV

### Identification du répertoire /uploads

```bash
# Test des méthodes WebDAV
curl -X OPTIONS demo.ine.local/uploads/ -v
```
**Découverte:** Module WebDAV activé avec support PUT/DELETE

### Upload de fichiers via PUT

```bash
# Création du fichier local
echo "Hello World" > hello.txt

# Upload via PUT
curl demo.ine.local/uploads/ --upload-file hello.txt
```

### Suppression de fichiers via DELETE

```bash
curl -X DELETE demo.ine.local/uploads/hello.txt
```

## Phase 4: Énumération avec Burp Suite

### Configuration proxy
1. Configurer FoxyProxy pour utiliser Burp Suite
2. Intercepter les requêtes dans Burp

### Tests via Repeater

#### Page d'accueil
```http
GET / HTTP/1.1
Host: demo.ine.local
```
**Résultat:** 200 OK

```http
OPTIONS / HTTP/1.1
Host: demo.ine.local
```
**Résultat:** Allow: GET, HEAD, OPTIONS

```http
POST / HTTP/1.1
Host: demo.ine.local
```
**Résultat:** 405 Method Not Allowed

#### Login.php
```http
POST /login.php HTTP/1.1
Host: demo.ine.local
Content-Type: application/x-www-form-urlencoded

name=john&password=password
```
**Résultat:** 302 Redirect (succès)

#### Upload WebDAV
```http
PUT /uploads/hello.txt HTTP/1.1
Host: demo.ine.local
Content-Length: 11

Hello World
```
**Résultat:** 201 Created

```http
DELETE /uploads/hello.txt HTTP/1.1
Host: demo.ine.local
```
**Résultat:** 204 No Content

## Résumé des Vulnérabilités

### WebDAV mal configuré
- **Répertoire:** /uploads
- **Méthodes dangereuses:** PUT, DELETE activées
- **Impact:** Upload/suppression de fichiers arbitraires
- **Exploitation:** Possible upload de webshells

### Différences de méthodes par endpoint
| Endpoint | GET | POST | PUT | DELETE | OPTIONS |
|----------|-----|------|-----|--------|---------|
| / (index.php) | ✅ | ❌ | ❌ | ❌ | ✅ |
| /login.php | ✅ | ✅ | ❌ | ❌ | ✅ |
| /post.php | ✅ | ✅ | ❌ | ❌ | ✅ |
| /uploads/ | ✅ | ❌ | ✅ | ✅ | ✅ |

## Commandes de Test Rapide

### Script d'énumération automatique
```bash
#!/bin/bash
methods=("GET" "POST" "PUT" "DELETE" "OPTIONS" "PATCH" "HEAD")
endpoints=("/" "/login.php" "/post.php" "/uploads/")

for endpoint in "${endpoints[@]}"; do
    echo "Testing $endpoint:"
    for method in "${methods[@]}"; do
        response=$(curl -s -o /dev/null -w "%{http_code}" -X $method demo.ine.local$endpoint)
        echo "  $method: $response"
    done
    echo
done
```

## Mesures de Sécurisation

### Désactivation des méthodes dangereuses
```apache
# Dans .htaccess ou configuration Apache
<Limit PUT DELETE>
    Deny from all
</Limit>
```

### Restriction WebDAV
```apache
# Désactiver WebDAV
LoadModule dav_module modules/mod_dav.so
<Directory "/uploads">
    Dav Off
</Directory>
```

### Headers de sécurité
```apache
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
```

## Points Clés d'Apprentissage

- L'énumération des méthodes HTTP révèle la surface d'attaque
- WebDAV mal configuré permet l'upload de fichiers malveillants
- Les méthodes OPTIONS révèlent les capacités des endpoints
- Différents endpoints peuvent avoir des configurations de méthodes distinctes
- Burp Suite et curl offrent des approches complémentaires pour les tests

Cette méthodologie d'énumération est essentielle pour identifier les vecteurs d'attaque potentiels lors des tests de pénétration web.