# 🧗‍♂️ Windows Privilege Escalation – Cheat Sheet

Ce dossier regroupe une **cheat sheet complète** et des notes pratiques sur l’**élévation de privilèges sous Windows**, basée principalement sur :

- 🔗 [TryHackMe - Windows Privilege Escalation 2.0](https://tryhackme.com/room/windowsprivesc20)
- 📚 Expériences personnelles et d'autres ressources reconnues dans le domaine (GTFOBins, PayloadsAllTheThings, etc.)

---

## 🎯 Objectif

Fournir un **référentiel rapide** et **pédagogique** pour :
- Identifier les vecteurs d’élévation de privilèges sur une machine Windows compromise
- Expliquer chaque méthode avec **des exemples concrets**
- S’appuyer sur les **bonnes pratiques de l’énumération Windows**
- Donner les **outils nécessaires à la détection des mauvaises configurations**

---

## 📚 Contenu inclus

| Thème | Description |
|-------|-------------|
| 🔍 Énumération initiale | Collecte des infos système et utilisateur |
| 🔐 Mots de passe | Récupération de credentials stockés ou faibles |
| 🧰 Outils | WinPEAS, Seatbelt, AccessChk |
| 🕒 Tâches planifiées | Scripts en écriture exécutés automatiquement |
| 🧱 Services | Services modifiables ou exécutés en SYSTEM |
| 🧬 Variables PATH | Hijack de commandes mal appelées |
| 🗂️ Dossiers de démarrage | Exécution automatique à la connexion |
| 🛠️ AlwaysInstallElevated | Installateur MSI avec privilèges SYSTEM |
| 💣 Exploits kernel | Utilisation d’exploits connus Windows |
| 📦 DLL Hijacking | Services chargeant des DLL externes |

---

## 🔧 Outils recommandés

- [WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)
- [Seatbelt](https://github.com/GhostPack/Seatbelt)
- [AccessChk](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk)
- [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)
- [Windows Exploit Suggester](https://github.com/AonCyberLabs/Windows-Exploit-Suggester)

---

## 🧠 Bonnes pratiques

- Ne pas négliger les **droits d’exécution sur les fichiers/services**
- Utiliser `icacls`, `whoami /groups`, `systeminfo`, et `schtasks` pour l’énumération
- Penser à vérifier les **tâches planifiées locales ET globales**
- Être attentif aux chemins non protégés (espaces sans guillemets)

---

---

## 🧭 1. Énumération initiale

🎯 **Objectif :** Identifier les informations système et les configurations susceptibles de présenter des vulnérabilités.

```cmd
systeminfo
whoami /priv
net user
net localgroup administrators
```

---

## 🔐 2. Récupération de mots de passe

🎯 **Objectif :** Trouver des informations d'identification stockées en clair ou de manière insécure.

- **Historique PowerShell**  
```powershell
type $Env:APPDATA\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

- **Fichiers de configuration IIS**  
```cmd
findstr /si password *.config
```

- **Informations d'identification enregistrées**  
```cmd
cmdkey /list
runas /savecred /user:USERNAME cmd.exe
```

- **Sessions PuTTY**  
```cmd
reg query HKCU\Software\SimonTatham\PuTTY\Sessions
```

---

## 🧰 3. Outils d'automatisation

🎯 **Objectif :** Accélérer l'énumération et identifier rapidement les vecteurs d'escalade.

- **WinPEAS**  
  Un script d'énumération complet pour Windows  
  🔗 https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS

- **Seatbelt**  
  Un outil de post-exploitation pour l'énumération de la sécurité sur Windows  
  🔗 https://github.com/GhostPack/Seatbelt

---

## 🕒 4. Tâches planifiées

🎯 **Objectif :** Exploiter des tâches planifiées mal configurées pour exécuter du code avec des privilèges élevés.

- **Lister les tâches**  
```cmd
schtasks /query /fo LIST /v
```

- **Vérifier les permissions**  
```cmd
icacls "C:\chemin\vers\script.bat"
```

---

## 🧱 5. Services Windows

🎯 **Objectif :** Exploiter des services mal configurés pour obtenir des privilèges élevés.

- **Permissions sur les exécutables de service**  
```cmd
sc qc NomDuService
icacls "C:\chemin\vers\service.exe"
```

- **Chemins de service non quotés**  
```cmd
sc qc NomDuService
```

---

## 🧬 6. Variables d'environnement & PATH

🎯 **Objectif :** Détourner des commandes appelées sans chemin absolu en manipulant la variable `%PATH%`.

---

## 🗂️ 7. Dossiers de démarrage

🎯 **Objectif :** Placer un exécutable dans le dossier de démarrage pour qu'il s'exécute avec des privilèges élevés à la connexion.

- **Vérifier les permissions**  
```cmd
icacls "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
```

---

## 🧪 8. Clés de registre AlwaysInstallElevated

🎯 **Objectif :** Exploiter une configuration de registre qui permet l'installation de fichiers MSI avec des privilèges élevés.

- **Vérifier les clés :**
```cmd
reg query HKCU\Software\Policies\Microsoft\Windows\Installer
reg query HKLM\Software\Policies\Microsoft\Windows\Installer
```

---

## 🧠 9. Exploits du noyau

🎯 **Objectif :** Exploiter des vulnérabilités connues du noyau Windows pour obtenir des privilèges SYSTEM.

- **Vérifier la version du système**
```cmd
systeminfo
```

- **Windows Exploit Suggester**  
  🔗 https://github.com/AonCyberLabs/Windows-Exploit-Suggester

- **Metasploit**
```bash
use post/multi/recon/local_exploit_suggester
```

---

## 🧪 10. DLL Hijacking

🎯 **Objectif :** Exploiter des services qui chargent des DLL depuis des emplacements contrôlables.

- Utiliser **Process Monitor** pour identifier les DLL manquantes avec "NAME NOT FOUND"

---

## 🧰 11. Outils utiles

- **AccessChk**  
🔗 https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk

- **Autoruns**  
🔗 https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns
