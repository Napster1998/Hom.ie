const Mymap = L.map('Mymap').setView([53.350140,-6.266155], 11);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(Mymap);



let listingsObject
console.log(listings)
if (listings.textContent) {

    listingsObject = JSON.parse(listings.textContent);

    console.log('listingObjeect:',listingsObject)

}

listingsArr = listingsObject || []
console.log(listingsArr)


listingsArr.forEach(element => {
    let popup = `<div>
    <b>EIR CODE</b>
    <p>${element.eir}</p>
    <b>Available Beds</b>
    <p>${element.noOfBeds}</p>
    <b>Contact</b>
    <p>${element.contact}</p>
    </div>`
    const marker = L.marker(element).bindPopup(popup).addTo(Mymap);
});
