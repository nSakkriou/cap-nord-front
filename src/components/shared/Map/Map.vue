<template>
    <div id="map" style="height: 500px;"></div>
  </template>
  
  <script>
  import L from 'leaflet';
  import 'leaflet-gpx'; // Import du plugin leaflet-gpx
  
  export default {
    name: "MapWithGpx",
    mounted() {
      // Initialisation de la carte
      const map = L.map('map').setView([51.505, -0.09], 13);
  
      // Ajouter une couche de tuiles à la carte (OpenStreetMap dans cet exemple)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(map);
  
      // Charger le fichier GPX
/*       const gpx = '/cap-nord.gpx'; // Chemin vers ton fichier GPX local
      new L.GPX(gpx, {
        async: true,
        marker_options: {
          startIconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
          endIconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-red.png',
          shadowUrl: 'https://leafletjs.com/examples/custom-icons/leaf-shadow.png'
        }
      }).on('loaded', function(e) {
        map.fitBounds(e.target.getBounds());
      }).addTo(map); */
    }
  }
  </script>
  
  <!-- Optionnel : Ajouter du style pour Leaflet -->
  <style>
    #map {
      height: 500px;
      width: 100%;
    }
  </style>
  