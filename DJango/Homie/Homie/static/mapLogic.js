const Mymap = L.map('Mymap').setView([53.350140,-6.266155], 11);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(Mymap);



let listingsObject
console.log(listings)
if (listings.textContent) {

    listingsObject = JSON.parse(listings.textContent);

    console.log(listingsObject)

}

listingsArr = listingsObject || []

listingsArr.forEach(element => {
    var marker = L.marker(element).addTo(Mymap);
});
