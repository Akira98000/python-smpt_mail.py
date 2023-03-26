
# Python SMTP Mail Sender

## Le fonctionnement du programme

Le programme utilise le module smtplib pour créer une session SMTP avec un serveur de messagerie 
(smtp.gmail.com dans ce cas). Ensuite, il s'authentifie en utilisant l'adresse email et le mot de passe du destinataire. 
Il crée un objet message avec une en-tête, un corps et des pièces jointes éventuelles à l'aide des modules email.mime.text et 
email.mime.multipart.

Une fois que le message est prêt, 
le programme utilise la méthode sendmail() de l'objet SMTP pour envoyer 
le message à l'adresse email du destinataire spécifiée. En cas de succès, 
il affiche un message confirmant l'envoi du courrier.

En résumé, ce programme utilise le protocole SMTP pour établir une 
connexion avec un serveur de messagerie, s'authentifier en utilisant les informations 
d'identification du destinataire et envoyer un message électronique à l'aide de la méthode sendmail().

## Installation

Soit cloner le projet

```bash
   git clone https://github.com/Akira98000/python-smpt_mail.py.git
```
    
Soit télécharger le fichier depuis ce lien:

https://github.com/Akira98000/python-smpt_mail.py



## License

La licence [MIT](https://choosealicense.com/licenses/mit/) est une licence open source permissive qui permet à quiconque d'utiliser, modifier et distribuer librement le code sous licence, à condition que l'attribution de la licence soit conservée et que toute responsabilité en cas de problème soit déclinée.



## Authors

- [@akirasanthakumaran](https://github.com/Akira98000) Développeur principal du projet.


## Badges

Badge de ce Dépot Git
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)





