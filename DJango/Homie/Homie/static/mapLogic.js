


a = [53.3888336,-6.4185164]
b = [53.388183,-6.368405]


const Mymap = L.map('Mymap').setView([53.350140,-6.266155], 11);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(Mymap);

arr = [a,b]
arr.forEach(element => {
    var marker = L.marker(element).addTo(Mymap);
});

//var marker = L.marker(a,b).addTo(Mymap);
//var marker1 = L.marker(b).addTo(Mymap);


//const far = L.marker(b).addTo(Mymap);