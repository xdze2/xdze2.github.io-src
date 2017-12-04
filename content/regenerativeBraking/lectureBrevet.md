Title: Regenerative braking system for bicycle
Slug: regenerativebrakingsystem
Tags: physique, vélo
Author: xdze2
Summary: Comment procurer une aide au démarrage en vélo qui utilise l'énergie à priori perdu lors du freinage ?
Date: 2017-11-14 13:00
Image: regenerativeBraking/images/thumbnail.jpg


# Regenerative braking system for bicycle

Ceux qui font du vélo en ville savent que démarer et accélerer est ce qui demande le plus d'effort.  Un cycliste évite donc le plus possible de devoir s'arreter (parfois en désaccord avec le code de la route). 

Hors l'énergie que nous coûte le démarrage correspond à l'énergie dissiper par les freins lors de l'arret. 

Comment procurer une aide au démarrage en vélo en utilisant l'énergie à priori perdu lors du freinage ?


Pour qu'un tel système soit intéressant, j'image quelques conditions: 

* Low tech (c.a.d. principalement non électrique).
* Il doit être adaptable sur un vélo existant (c.a.d. dans le moyeu ou attachable sur le cadre).
* Le système doit être raisonablement simple (pas pneumatique ou hydrolique).

Il existe beaucoup de brevets et projets s'attaquant à cette question. 

On peut noter cette vidéo de [P. Cortona](https://www.youtube.com/watch?v=wxhyJAr-YCM) qui semble presenter un prototype fonctionnel et raisonable. Malheureusement, on ne trouve pas plus d'information. Le projet `Quirky.com` cité n'existe plus. 

Et avec un projet, universitaire, avec un volant d'inertie: [KERS bicycle technology university project at AIT](https://www.youtube.com/watch?v=5FJcEvijjks). Et aussi the [Maxwell von Stein’s bike](https://www.wired.com/2011/08/regenerative-flywheel-powered-bicycle/).


Le brevet de [Mark R. Brent et Jim M. Papadopoulos (1986)](https://www.google.com/patents/US4744577) semble correspondre à mes conditions (système dans le moyeu). J'ai donc commencé par analyser ce brevet pour en comprendre le fonctionnement de ce mécanisme. 

## Analyse du brevet de Mark R. Brent et Jim M. Papadopoulos (1986)

### Prior art
* Le ratio energie stocker par rapport au poids est supérieure pour les volant d'inertie (Flywheels)... mais ces systèmes sont lourds et complexe (paliers, transmission variable)

* Deux brevets cités: Pepper et [P. Cauchon](https://www.google.com/patents/US2965393). Dans le brevet de P. Cauchon, l'embrayage du système se fait par un galet venant en contact avec le pneu. Des ressorts métalliques semblent être utilisés pour stocker l'énergie. 

* Ici, les ressort métallique sont considérés non utilisable parce que trop lourds pour stocker l'énergie necessaire. Un élastique caoutchouc est préféré. 


### Figures annotées

 [<img src="regenerativeBraking/images/brevet_Fig1_color.jpg" alt="Fig1" width='250px' />](regenerativeBraking/images/brevet_Fig1_color.jpg)
 [<img src="regenerativeBraking/images/brevet_Fig2_color.jpg" alt="Fig1" width='250px' />](regenerativeBraking/images/brevet_Fig2_color.jpg)
 [<img src="regenerativeBraking/images/brevet_Fig3_color.jpg" alt="Fig1" width='250px' />](regenerativeBraking/images/brevet_Fig3_color.jpg)

Voir la légende [ici](regenerativeBraking/images/figures_legende.txt).


### Schéma cinématique
Pour mieux comprendre le fonctionement du mécanisme un schéma aide. 

<img src="regenerativeBraking/images/sch_cinematique_brevet.png" alt="cinematique" width='800px' />
 
Il y a deux commandes qui bloque ou libère chacune un embrayage (ou mécanisme de bloquage). Le système à donc théoriquement **4 états possibles :** 

* **frein bloqué seul**: la couronne est entrainée par la roue. L'engrennage soleil tourne alors dans le sens inverse. Ceci emagasine de l'énergie dans le ressort. 
* **'Release' bloqué seul**: Alors le ressort est en prise direct avec la roue. L'énergie du ressort est transmise à la roue qui tourne vers l'avant. à noter qu'il n'y a pas de réduction de vitesse de rotation possible ici. 
 
* **tout libre**: La roue n'entraine aucune engrenage... rien ne se passe. 
* **tout bloqué**: Le mécanisme est bloqué... problème.

_Rq:_ un cliquet est utilisé dans le brevet. 

### Ce qui est bien:
* Actionné par le frein (friction)... mais est-ce réelement bien ?
* _Planet Gear_: le mécanisme permet l'inversion du sens de rotation entre la charge et la décharge relativement simplement. N'est pas forcement nécessaire, si les deux extremités du ressort sont accessibles. 

* Quand l'engrenage _Sun_ est bloqué (c.a.d. ressort au max) alors l'engrenage _Ring_ est aussibloqué: le comportement est alors celui d'un vrai frein.

### Ce qui n'est pas super:
* L'_Elastic material_ est en dehors du Hub! (voir Fig. 1)
* Le système de frein est questionable: système de levier non décrit et appuis en un point unique sur le _brake pad_...
* L'important mécanisme d'engagement _Clutch 220_ est non décrit. 

* Pas de freinage d'urgence. Il faut toujours charger le ressort à fond avant de pouvoir bloquer la roue. Cece limite l'avantage d'un système actionné par le frein.

* Pas de vrai dosage du frein... l'énergie est perdu en friction quand on ne freine pas au maximum... (Mais est-ce que c'est possible de faire autrement sans variateur continu ?)


### Bugs dans le brevet:
* Le _Lever 219_ est dessiné avec une mauvaise orientation sur Fig. 3 par rapport à la Fig. 2
* Qu'elle est l'utilité du _Planet alignement disc 216_ ? Les axes des planétaires sont fixés au _Reaction arm 211_. Le _Planet alignement disc 216_ rend donc solidaire les _Planet Gears_ avec le _Sun Gear_ ce qui n'a pas de sens...
* Le dessin du _Ratchets 24_ est plein. On devrait voir le passage de l'axe... 


# Energie stockable dans un ressort ?

Le premier inconvénient de la solution proposée dans le brevet est que le matériaux élastique est placé sur le cadre, en dehors du système mécanique. On peut se demander si un ressort spiral métallique ne pourrait pas convenir, malgré le problème du poids indiqué dans le brevet. 

La première question à répondre est donc le dimensionnement du ressort. 


On peut tirer sur un matériau élastique jusqu'à ce qu'il case (ou bien se déforme plastiquement). La limite élastique du matériau (yield strength, yield stress) est donc limitante dans la quantité d'énergie stockable.
 
<img src="regenerativeBraking/images/graph_def_contrainte.jpg" alt="graph deformation/contrainte" />

L'énergie élastique par unité de volume est :
$$
\delta U_{max} = \frac{\sigma_Y^2}{2\,E} 
$$

où $E$ est le module de Young et $\sigma_Y$ la contrainte correspondant à la limite élastique du matériau.

Pour un ressort de volume $V$ fabriqué dans un matériau de densité $\rho$ :
$$
U_{max} = \frac{\sigma_Y^2}{2\,E} \, V = \frac{\sigma_Y^2}{2\,E} \, \frac{m_{ressort}}{\rho}
$$

Nous pouvons donc comparer les matériaux entre-eux en utilisant le critère : $\frac{\sigma_Y^2}{E\,\rho}$.

Voir le notebook [`Dimensionnement`](https://github.com/xdze2/xdze2.github.io-src/blob/master/content/regenerativeBraking/dimensionnement.ipynb) pour le calcul et les références des valeurs. 

Voici les résultats pour quelques matériaux. Pour que cela soit plus parlant, la masse du ressort nécessaire pour stocker l'énergie cinétique d'un cycliste de 90kg et roulant à 15 km/h est calculée.
 
                              masse ressort    rho;        E;   sigma_Y
                 Acier struct. : 60.938 kg     7.8;  200 GPa;   200 MPa 
                 Acier ressort :  1.354 kg     7.8;  160 GPa;  1200 MPa 
           Corde à piano (6mm) :  1.138 kg     7.8;  210 GPa;  1500 MPa 
             Alliage de Titane :  0.798 kg     4.4;  120 GPa;  1020 MPa 
           Corde à piano (1mm) :  0.529 kg     7.8;  210 GPa;  2200 MPa 
              Caoutchouc butyl :  0.177 kg     1.2;    7 MPa;     9 MPa 
            Caoutchouc naturel :      4 g      0.7;    1.5 MPa;  20 MPa 


Le caoutchouc naturel semble bien le meilleur candidat. Le caoutchouc butyl est celui utilisé pour les chambres à air. Il faut noté que le comportement du caoutchouc n'est pas du tout linéaire. La valeur obtenue est donc fortement approximative. 


_Rq:_ Les fibres de verre ou de carbones semblent aussi très intéressantes.


## La suite

* Regarder le brevet de [Regenerative braking and driving apparatus (2003)](https://www.google.com/patents/US6557877  ) de Jason Dunkley qui utilise un ressort de torsion monté dans le moyeu. 
* Affiner le dimensionnement avec un ressort de torsion, ou spirale



