
const map = L.map('map').setView([53.3498, 6.2603], 13);

// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//     maxZoom: 18,
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1,
//     accessToken: mapBoxApiKey
// }).addTo(mymap);

// Adding Markers

const marker = L.marker([40.748708, -73.985433]).addTo(map);