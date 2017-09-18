Title: Tube & OpenFoam
Slug: tube_openfoam
Tags: modélisation, physique, openFoam
Author: xdze2
Summary: flow in a tube
Date: 2017-09-06 20:00
Image: images/paraFoam_mesh_s.png
Status: draft

# Physique - écoulement dans un tuyau


[Écoulement de Poiseuille](https://en.wikipedia.org/wiki/Hagen%E2%80%93Poiseuille_equation)

$$
\Delta = 8 \mu \, \frac{U}{R^2}
$$

$$
Re = 2 R \, U \, \frac{\rho}{\mu}
$$

* R: rayon (m)
* U: vitesse à l'entrée (m/s)
* $\rho$: densité (kg/m3)
* $\mu$: viscosité dynamique (Pa.s)

La viscosité dynamique de l'eau est $ \mu_{eau} \approx 1e^{-3} Pa.s$ à une température de 20°C. 

Géométrie :
* R = 3 mm
* L = 51 mm


...
* U = 0.1 m/s ... Re = 600


# Choix du solver 

* `Simple` :  steady-state
* `Piso`   : transient  - explicit
* `Pimple` : transient - implicit


* `simpleFoam` : Steady, turbulent
* `icoFoam` : Transient, laminar, Newtonian
* `pimpleFoam` : Transient, turbulent, large time step (implicit)
* `pisoFoam` : transient, turbulent


https://www.cfd-online.com/Forums/openfoam-solving/68072-pimplefoam-vs-simplefoam-vs-pisofoam-vs-icofoam.html

http://www.openfoam.com/documentation/user-guide/standard-solvers.php

# Paramètres physiques

### transportProperties 
        nu              [0 2 -1 0 0 0 0] 1e-6;




