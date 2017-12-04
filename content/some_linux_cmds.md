Title: Quelques commandes linux
Slug: quelquescommandeslinux
Tags: blocnote, linux
Author: xdze2
Summary: à ne pas oublier
Date: 2017-11-18 20:00
Image: images/tux.jpg

# Démarrer un VirtualEnv python

    $ virtualenv -p /usr/bin/python3 py3
    $ source ./py3/bin/activate

    $ virtualenv --system-site-packages -p /usr/bin/python3 py3 
        
## et installer les librairies python "de base"

    $ pip install jupyter matplotlib scipy pandas
        
et lancer `jupyter`:

    $ jupyter notebook
        
* pour créer la liste des paquets (et enregistrer puis installer):

    $ pip freeze  > requirements.txt
    $ pip freeze --local -r requirements.txt
    $ pip freeze --local > requirements.txt
    $ pip install -r requirements.txt
    
    
# Générer un mot de passe aléatoire

   $ apg
       
# Scan local network

    $ arp-scan 192.168.0.0/24

    $ nmap -O -v scanme.nmap.org
        
# Serveur http python

    $ python -m SimpleHTTPServer
        
        
# Voir les variables d'environement

    $ printenv
    $ echo $MA_VARIABLE


