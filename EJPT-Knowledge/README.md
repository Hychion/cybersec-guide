# 🎯 eJPT Knowledge Base - Méthodologie de Penetration Testing

## 📚 Vue d'ensemble

Ce repository contient une base de connaissances complète pour la certification **eJPT (eLearnSecurity Junior Penetration Tester)**. Il suit une méthodologie structurée en phases distinctes pour mener un test de pénétration efficace.

---

## 🔄 Méthodologie en 6 phases

### 🔍 Phase 1 : Information Gathering (Reconnaissance)

**Objectif :** Collecter un maximum d'informations sur la cible sans interaction directe.

#### Reconnaissance passive (OSINT)
- **Google Dorking** : Recherche d'informations publiques
- **Réseaux sociaux** : LinkedIn, Facebook, Twitter
- **Archives web** : Wayback Machine, cached pages
- **DNS enumeration** : Sous-domaines, enregistrements MX/TXT
- **WHOIS** : Informations sur le domaine et l'organisation

#### Reconnaissance active
- **Ping sweep** : Découverte d'hôtes actifs
- **DNS zone transfer** : Tentative de transfert de zone
- **Port knocking** : Tests de connectivité discrets

**Outils principaux :**
- `nslookup`, `dig`, `host`
- `whois`
- `theHarvester`
- Google Dorks
- Metasploit auxiliary modules

**Livrables :**
- Liste des domaines/sous-domaines
- Adresses email découvertes
- Technologies identifiées
- Structure organisationnelle

---

### 🔎 Phase 2 : Scanning & Enumeration

**Objectif :** Identifier les services, ports ouverts et versions des applications.

#### Network Discovery
- **Host discovery** : Identification des machines actives
- **Port scanning** : Découverte des ports ouverts
- **Service detection** : Identification des services et versions
- **OS fingerprinting** : Détection du système d'exploitation

#### Service Enumeration
- **FTP (21)** : Anonymous login, version, banner grabbing
- **SSH (22)** : Version, algorithmes supportés
- **SMTP (25)** : User enumeration, relay test
- **HTTP/HTTPS (80/443)** : Technologies web, répertoires
- **SMB (139/445)** : Partages, utilisateurs, domaine
- **MySQL (3306)** : Version, databases accessibles

**Outils principaux :**
- `nmap` avec scripts NSE
- `masscan`, `rustscan`
- `enum4linux`, `smbclient`
- `gobuster`, `dirb`, `ffuf`
- Metasploit scanner modules

**Livrables :**
- Cartographie réseau complète
- Inventaire des services par machine
- Versions détaillées des applications
- Partages et ressources accessibles

---

### 🎯 Phase 3 : Vulnerability Assessment

**Objectif :** Identifier les vulnérabilités exploitables dans les services découverts.

#### Vulnerability Scanning
- **Automated scanning** : Nessus, OpenVAS, Nuclei
- **Manual testing** : Tests spécifiques par service
- **Web vulnerabilities** : OWASP Top 10
- **Network vulnerabilities** : CVE connus, misconfigurations

#### Vulnerability Analysis
- **CVSS scoring** : Évaluation de la criticité
- **Exploitability assessment** : Facilité d'exploitation
- **Impact analysis** : Conséquences potentielles
- **False positive elimination** : Validation manuelle

**Outils principaux :**
- `nmap --script vuln`
- `nikto`, `wapiti`
- `searchsploit`
- Metasploit auxiliary scanners
- `nuclei` templates

**Livrables :**
- Liste des vulnérabilités par criticité
- Preuves de concept (PoC)
- Matrice risque/impact
- Recommandations de priorisation

---

### ⚔️ Phase 4 : Exploitation

**Objectif :** Exploiter les vulnérabilités pour obtenir un accès initial aux systèmes.

#### Initial Access
- **Remote exploits** : Buffer overflow, injection SQL
- **Web application attacks** : XSS, CSRF, file upload
- **Social engineering** : Phishing, ingénierie sociale
- **Password attacks** : Brute force, dictionary attacks

#### Exploit Development
- **Public exploits** : Exploit-DB, GitHub
- **Custom exploits** : Adaptation d'exploits existants
- **Metasploit modules** : Utilisation du framework
- **Manual exploitation** : Tests manuels approfondis

**Outils principaux :**
- Metasploit Framework
- `hydra`, `medusa`
- Burp Suite, OWASP ZAP
- Custom scripts et exploits
- `sqlmap`

**Livrables :**
- Accès confirmé aux systèmes
- Shells/backdoors installés
- Données sensibles récupérées
- Preuves d'exploitation (screenshots)

---

### 🚀 Phase 5 : Post-Exploitation

**Objectif :** Maintenir l'accès, escalader les privilèges et explorer le réseau.

#### Privilege Escalation
- **Local enumeration** : Informations système
- **Kernel exploits** : Vulnérabilités du noyau
- **Service misconfigurations** : Services mal configurés
- **Credential harvesting** : Récupération de mots de passe

#### Lateral Movement
- **Network mapping** : Découverte du réseau interne
- **Credential reuse** : Test des credentials sur d'autres systèmes
- **Pivoting** : Utilisation de la machine compromise comme relay
- **Domain enumeration** : Exploration de l'Active Directory

#### Persistence
- **Backdoors** : Installation de portes dérobées
- **Service creation** : Création de services malveillants
- **Registry modification** : Modification du registre Windows
- **Scheduled tasks** : Tâches planifiées

**Outils principaux :**
- Metasploit post-exploitation modules
- `mimikatz`, `bloodhound`
- `linpeas`, `winpeas`
- `privesccheck.ps1`
- `psexec`, `wmiexec`

**Livrables :**
- Accès administrateur confirmé
- Cartographie du réseau interne
- Bases de données de credentials
- Mécanismes de persistance

---

### 📊 Phase 6 : Reporting

**Objectif :** Documenter les findings et fournir des recommandations.

#### Documentation
- **Executive summary** : Résumé pour la direction
- **Technical details** : Détails techniques pour l'équipe IT
- **Risk assessment** : Évaluation des risques
- **Remediation guidance** : Guide de correction

#### Proof of Concept
- **Screenshots** : Preuves visuelles
- **Command outputs** : Sorties de commandes
- **Exploit code** : Code d'exploitation utilisé
- **Video demonstrations** : Démonstrations vidéo

**Livrables :**
- Rapport exécutif
- Rapport technique détaillé
- Plan de remédiation
- Présentation des résultats

---

## 🛠️ Outils par phase

| Phase | Outils principaux | Modules Metasploit |
|-------|-------------------|-------------------|
| **Reconnaissance** | nslookup, whois, theHarvester | auxiliary/gather/* |
| **Scanning** | nmap, rustscan, masscan | auxiliary/scanner/* |
| **Vulnerability Assessment** | nikto, nuclei, searchsploit | auxiliary/scanner/*/*, --script vuln |
| **Exploitation** | Metasploit, hydra, sqlmap | exploit/*/*/*, auxiliary/admin/* |
| **Post-Exploitation** | mimikatz, bloodhound, linpeas | post/*/*/*, exploit/*/local/* |
| **Reporting** | KeepNote, CherryTree, Markdown | db_export, report generation |

---

## 📈 Workflow eJPT recommandé

### 🎯 Approche méthodique
1. **Toujours commencer par la reconnaissance passive**
2. **Scanner progressivement** (ping sweep → port scan → service enum)
3. **Prioriser les services web** (HTTP/HTTPS très présents dans l'eJPT)
4. **Utiliser Metasploit dès que possible** (framework central de l'exam)
5. **Documenter chaque étape** avec screenshots

### ⚡ Raccourcis pour l'exam
- **Nmap one-liner** : `nmap -sV -sC -O target`
- **Metasploit quick scan** : `db_nmap -sV target; search type:exploit`
- **Web enum rapide** : `gobuster dir -u http://target -w common.txt`
- **SMB check** : `enum4linux target`
- **Privilege escalation** : `use post/multi/recon/local_exploit_suggester`

---

## 📚 Structure du repository

```
eJPT-Knowledge-Base/
├── docs/methodology/          # Méthodologies détaillées
├── docs/cheatsheets/          # Fiches techniques rapides
├── metasploit/               # Focus Metasploit Framework
├── enumeration/              # Techniques d'énumération
├── exploitation/             # Techniques d'exploitation
├── post-exploitation/        # Post-exploitation et persistence
├── labs/                     # Laboratoires pratiques
├── scripts/                  # Scripts d'automatisation
└── templates/                # Templates de rapport
```

---

## 🎓 Conseils pour l'eJPT

### ✅ Do's
- **Suivre la méthodologie** étape par étape
- **Utiliser Metasploit** autant que possible
- **Documenter avec screenshots** chaque finding
- **Tester les credentials** sur tous les services
- **Explorer les applications web** en détail

### ❌ Don'ts
- **Ne pas sauter d'étapes** dans la méthodologie
- **Ne pas ignorer les services** "non-standards"
- **Ne pas oublier l'énumération locale** après compromission
- **Ne pas négliger la documentation** pendant l'exam

### 🔥 Points clés eJPT
- **Metasploit est roi** : Maîtriser le framework est essentiel
- **Web apps omniprésentes** : Beaucoup de vulnérabilités web
- **Credentials everywhere** : Toujours chercher des mots de passe
- **SMB souvent vulnérable** : EternalBlue, null sessions, etc.
- **Post-exploitation importante** : Escalation de privilèges fréquente

---

## 🚀 Getting Started

1. **Cloner le repository**
```bash
git clone https://github.com/votre-username/eJPT-Knowledge-Base.git
cd eJPT-Knowledge-Base
```

2. **Commencer par la méthodologie**
```bash
cd docs/methodology/
cat penetration-testing-methodology.md
```

3. **Utiliser les cheatsheets pendant les labs**
```bash
cd docs/cheatsheets/
cat metasploit-cheatsheet.md
```

4. **Pratiquer avec les labs**
```bash
cd labs/beginner/
cat lab-01-basic-nmap.md
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines.

## 📄 License

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

---

**🎯 Objectif final :** Maîtriser cette méthodologie pour réussir l'eJPT et devenir un pentester efficace !

*Happy Hacking! 🚀*