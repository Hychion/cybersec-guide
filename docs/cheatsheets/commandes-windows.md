# 🪟 Windows Command Cheat Sheet – Utilisation Système et Post-Exploitation

Cette cheat sheet regroupe les **commandes Windows** essentielles, utiles en administration système, post-exploitation ou audit de sécurité.

---

## 🧭 1. Informations système & utilisateur

```cmd
systeminfo                     # Infos système complètes
hostname                       # Nom de la machine
whoami                         # Utilisateur courant
whoami /priv                   # Privilèges de l'utilisateur
net user                       # Utilisateurs du système
net localgroup administrators  # Membres du groupe admin
```

---

## 📁 2. Navigation et gestion de fichiers

```cmd
cd                            # Changer de dossier
dir                           # Lister les fichiers
copy fichier1 fichier2        # Copier un fichier
move fichier dossier\        # Déplacer
del fichier                   # Supprimer
type fichier.txt              # Lire le contenu d'un fichier
attrib                       # Voir/éditer les attributs d’un fichier
```

---

## 🔐 3. Droits et sécurité

```cmd
icacls fichier                # Droits sur fichier
cacls fichier                 # Ancienne version de icacls
runas /user:admin cmd         # Lancer cmd en tant qu'autre utilisateur
cmdkey /list                  # Voir les credentials enregistrés
```

---

## 🔎 4. Recherche

```cmd
findstr /S /I "mot" *.txt     # Recherche récursive insensible à la casse
dir /s /b | find "nom"        # Recherche d’un fichier
```

---

## 🕒 5. Tâches et planifications

```cmd
schtasks /query /fo LIST /v   # Voir les tâches planifiées
tasklist                      # Processus actifs
taskkill /F /PID <pid>        # Tuer un processus
```

---

## 🛠️ 6. Réseau

```cmd
ipconfig /all                # Interfaces réseau
ping IP                      # Tester la connectivité
netstat -ano                 # Ports ouverts + PID
tracert 8.8.8.8              # Tracer une route réseau
arp -a                       # Table ARP
```

---

## 🔗 7. Connexions & partages

```cmd
net share                    # Partages disponibles
net use                      # Connexions réseau
net use z: \\ip\partage    # Monter un partage distant
```

---

## 📦 8. Services et drivers

```cmd
sc query                     # Liste les services
sc qc nom_service            # Détails d’un service
driverquery                  # Liste les drivers installés
```

---

## 🧪 9. Forensic / post-exploitation

```cmd
dir /a /s C:\Users\*\.ssh        # Recherche de clés SSH
type %USERPROFILE%\.bash_history   # Historique WSL
reg query HKCU                     # Registre utilisateur
reg query HKLM                     # Registre machine
wmic qfe list                      # Patches installés
```

---

## 🧰 10. Outils intégrés utiles

```cmd
msinfo32                     # Infos système graphique
dxdiag                       # Diagnostic graphique
eventvwr                     # Visionneuse d’événements
control                      # Ouvre le panneau de config
```

---

📁 À placer dans `docs/cheatsheets/commandes-windows.md`
