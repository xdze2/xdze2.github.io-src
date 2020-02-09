Title: Chaotic Clouds
Slug: chaoticclouds
Tags: visualisation, fractale
Author: xdze2
Summary: Interactive 3D point clouds of strange attractors using Potree 
Date: 2019-12-12 11:00
Image: ./visualisation/images/chemical_Lorentz.png


Visualisation de nuages de points d'attracteur étranges en utilisant Potree, un logiciel habituelement utilisé pour des données géographiques et stéréographiques.

Voir la [version interactive ici](https://xdze2.github.io/chaotic-clouds/)

![screenshot_attractor](./visualisation/images/bluethomasattractor.png)


* Les trajectoires sont intégrées avec [DifferentialEquations.jl](https://docs.juliadiffeq.org/stable/index.html), puis les points sont comptés par voxel afin d'obtenir une distribution de points régulière.
* Le nuage de point est alors transformées et intégrées dans [Potree](http://potree.org/) (a free open-source WebGL based point cloud renderer for large point clouds)

![screenshot_attractor_Lorentz](./visualisation/images/chemicalLorentz01.png)




