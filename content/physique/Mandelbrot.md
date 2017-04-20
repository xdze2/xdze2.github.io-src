Title: Deep Zoom Image et Mandelbrot
Slug: Mandelbrot
Category: physique
Tags: physique, fractale, algorithme, visualisation
Author: xdze2
Date: 2017-03-31 23:00
Summary: Calcul d'une pyramide d'images, pour créer une vue interactive zoomable de l'ensemble fractal de Mandelbrot.
Image: physique/images/mandelbrot.png
Status: Published

<div id="openseadragon1" style="width: 100%; height: 500px; cursor:all-scroll; background-color:black;border:solid 1px black;"></div>

<script src="static/openseadragon/openseadragon.min.js"></script>
<script type="text/javascript">
    var viewer = OpenSeadragon({
        id: "openseadragon1",
        prefixUrl: "static/openseadragon/images/",
        tileSources: "physique/images/mandelbrot/0_Mandel.dzi"
    });
</script>



{% notebook physique/Mandelbrot.ipynb %}
