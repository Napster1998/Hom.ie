
const Mymap = L.map('Mymap').setView([53.350140,-6.266155], 11);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(Mymap);


const marker = L.marker([53.3888336,-6.4185164]).addTo(Mymap);


