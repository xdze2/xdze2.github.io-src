Title: De FreeCad à OpenFoam
Slug: geom_mesh
Tags: modélisation, physique, openFoam
Author: xdze2
Summary: tutorial pour importer une géométrie FreeCad dans OpenFoam, en passant par Gmsh
Date: 2017-09-05 20:00
Image: images/paraFoam_mesh_s.png

# De FreeCad à OpenFoam

Ceci est le début d'un projet pour utiliser l'environement de calcul CFD libre: [OpenFoam](http://www.openfoam.com/) ([doc](https://cfd.direct/)).

Dans cette première partie, nous allons voir comment créer une géométrie -modèle 3D- avec [FreeCad](https://www.freecadweb.org/), puis créer un maillage sur cette géométrie avec [Gmesh](http://gmsh.info/). Et enfin comment importer le maillage dans OpenFoam. 


Les opérations sont: 

1. Création de la géométrie avec FreeCad
2. Transfert dans Gmsh
3. Définition des groupes de surfaces (physical elements), pour les futurs conditions aux limites.
4. Génération du maillage
5. Transfert dans OpenFoam, en récupérant les labels des surfaces


La principale inspiration est la vidéo [FreeCAD, Gmsh, OpenFoam - an opensource CFD case](https://www.youtube.com/watch?v=KeEp6EJuIxU).


# FreeCad
On commence par créer une géométrie simple, un tuyau coudé, avec la fonction de balayage ([part sweep](https://www.freecadweb.org/wiki/Part_Sweep)).

Il y a deux esquisses. L'une est le chemin de balayage :

<img src="./calculs_num/images/freecad_esquisse_balayage.png" alt="esquise 1" width='50%' />

et l'autre, dans un plan perpendiculaire, est la section du tube que l'on souhaite créer. 

Vue 3d des esquisses :
<img src="./calculs_num/images/freecad_esquisse3D.png" alt="esquisse 3d" width='70%' />

Ce qui donne au final ce volume: 
<img src="./calculs_num/images/freecad_tube.png" alt="esquisse 3d"  width='70%' />


Le modèle est ensuite exporté (`Pièce/Exportation CAO...`) au format STEP (Standard for the Exchange of Product model data, [format ISO-10303](https://en.wikipedia.org/wiki/ISO_10303)). C'est un fichier texte lissible.

_Rq:_ On peut, à priori, définir l'unité des dimensions pour l'export au format STEP dans les paramètres de FreeCad (Edition/Préférences/Import-Export/STEP). Ici en millimètre. 


La suite se passe avec Gmsh. C'est un logiciel libre de maillage. 

# Gmsh
L'interface se présente comme ceci avec un menu hierachique des actions possible à gauche:

<img src="./calculs_num/images/gmsh_vide.png" alt="esquisse 3d"  width='70%' />

`File/Open...` permet d'ouvrir le fichier STEP.

La première chose à faire est de définir les 'Physical groups'. Ceci correspond à assigner un label pour chaque surfaces et volumes permettant ensuite de les retrouver dans OpenFoam. 

Dans l'arborescence du menu à gauche, on trouve l'action `ADD - Surface`. Il est aussi important de créer un volume. 

<img src="./calculs_num/images/gmesh_addphysicalgroups.png" alt="esquisse 3d"  width='70%' />

Pour la création du maillage, le paramètre le plus important est la taille des élements crées. 
C'est le paramètre `Element size factor` dans l'onglet `Mesh-General` de la boite `Tool/Options` :

<img src="./calculs_num/images/gmsh_eltsizefactor.png" alt="esquisse 3d"  width='70%' />

Il faut ensuite cliquer succesivement sur `1D`, `2D` et `3D`, dans le menu `Mesh`-`Define`, pour créer le maillage.

En jouant sur les paramètres de visibilité et de couleur, on obtient la vue suivante ([voir](http://onelab.info/pipermail/gmsh/2012/007649.html)):
<img src="./calculs_num/images/gmesh_finalmesh.png" alt="esquisse 3d"  width='70%' />

Il reste à enregistrer le maillage: `File/Save Mesh`. Un fichier `.msh` est créé. Lui aussi est lissible avec un editeur de texte. C'est la liste de tout les points du maillage et des élements. L'information des 'Physical groups' est indiquée dans la définition des éléments ([spec.](http://gmsh.info/doc/texinfo/gmsh.html#MSH-ASCII-file-format), [man page](http://www.manpagez.com/info/gmsh/gmsh-2.2.6/gmsh_63.php)), dans la 4ième colonne :

        $Elements
        4682
        1 2 2 9 1 271 10 11
        2 2 2 9 1 196 11 10
        3 2 2 9 1 214 10 271
        4 2 2 9 1 10 9 179
        5 2 2 9 1 9 10 214
        6 2 2 9 1 245 10 179
        7 2 2 9 1 196 10 245
        ...etc


Un fichier `.geo` est aussi créé, correspondant simplement aux commandes effectuées, sans le maillage: 

        Merge "coude.step";
        Physical Surface(8) = {4};
        Physical Surface(9) = {1, 2, 3};
        Physical Surface(10) = {5};
        Physical Volume(11) = {1};


_Rq:_ il doit être possible de créer un maillage bien plus joli, avec une extrusion par exemple... ([bifurcation mesh](http://www.micronanoflows.ac.uk/news/creating-openfoam-meshes-with-gmsh))


# OpenFoam

La doc du programme [gmshToFoam](https://openfoamwiki.net/index.php/GmshToFoam) est plutôt succincte.

Il faut travailler dans le repertoire d'un projet existant. La façon la plus simple est de copier un cas d'exemple. 

        $ ls $FOAM_TUTORIALS/incompressible/


En partant de l'exemple `cavity` ([tuto](https://cfd.direct/openfoam/user-guide/cavity/#x5-40002.1)):

        $ cp -r $FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity . 
        
Le fichier de maillage est ensuite copier à la racine du répertoire du projet. Puis le programme de conversion est exécuté, avec en paramètre le fichier du maillage :      

        $ gmshToFoam coude.msh

La correspondance entre les 'physical groups' et les patchs de OpenFoam est rendue par `gmshToFoam`:

        [...]
        Mapping region 9 to Foam patch 0
        Mapping region 8 to Foam patch 1
        Mapping region 10 to Foam patch 2
        Mapping region 11 to Foam cellZone 0
        [...]

Le maillage est créé dans le repertoire `constant/polyMesh`.

Dans notre cas: region 8 -> inlet, region 9 -> tube, region 10 -> outlet. On peut donc renomer les patchs dans le fichier `constant/polyMesh/boundary`.

Les valeurs physiques correspondantes aux conditions aux limites sont spécifiées dans les fichiers `0/U` et `0/P`.

Le logiciel paraview permet d'afficher le maillage:

        $ paraFoam

<img src="./calculs_num/images/paraFoam_mesh.png" alt="paraFoam"  width='70%' />

On peut vérifier le maillage:

        $ checkMesh


Et aussi changer son échelle (par exemple de millimètre à mètre) ([doc.](https://openfoamwiki.net/index.php/TransformPoints)):

        $ transformPoints -scale '(1e-3 1e-3 1e-3)'


# la suite
La suite est de paramétrer le solveur et d'effectuer le calcul. 


