Title: Quelques commandes linux
Slug: quelquescommandeslinux
Tags: blocnote, linux
Author: xdze2
Summary: à ne pas oublier
Date: 2017-11-18 20:00
Image: images/tux.jpg

# Python related

## Démarrer un VirtualEnv python

    $ virtualenv -p /usr/bin/python3 py3
    $ source ./py3/bin/activate

    $ virtualenv --system-site-packages -p /usr/bin/python3 py3 
 
Pour que jupyter retrouve le bon kernel ([ref.](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments)):

    $ source py3/bin/activate
    $ pip install ipykernel
    $ python -m ipykernel install --user --name py3 --display-name "Py3 (env)"
        
### et installer les librairies python "de base"

    $ pip install jupyter matplotlib scipy pandas
        
Pour lancer `jupyter`:

    $ jupyter notebook
        
* pour créer la liste des paquets (et enregistrer puis installer):

    $ pip freeze  > requirements.txt
    $ pip freeze --local -r requirements.txt
    $ pip freeze --local > requirements.txt
    $ pip install -r requirements.txt

## Serveur http python

    $ python -m SimpleHTTPServer
        
Avec python3:
    $ python3 -m http.server 8850    

# Linux
    
## Générer un mot de passe aléatoire

   $ apg
       
## Scan local network

    $ arp-scan 192.168.0.0/24

    $ nmap -O -v scanme.nmap.org
        
        
## Voir les variables d'environement

    $ printenv
    $ echo $MA_VARIABLE


