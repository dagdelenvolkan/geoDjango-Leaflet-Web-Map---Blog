// Haritamızı oluşturmak için map isimli bir değişken tanımlıyoruz
var map = L.map('map').setView([41.1245, 28.9100], 10);


//Haritamızın görüntüleneceği tile katmanını ayarlıyoruz. Bu projede OpenStreetMap kullanacağız.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a target="blank" href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' +
      ' | &copy; <a  target="blank" href="https://data.ibb.gov.tr/license">IBB Lisans</a>'
}).addTo(map);


// Cluster'ı tanımlayalım
var markers = new L.markerClusterGroup();

// API adresi
var url = 'http://127.0.0.1:8000/saglik/';


fetch(url)
.then(res => res.json())
.then(data => markers.addLayer(L.geoJson(data, {
    onEachFeature: function  (feature, layer) {
        layer.bindPopup('<table> <tr>' + ' <td> <strong>ADI </strong> </td>' + '<td>' + feature.properties.ADI.toUpperCase() + '</td> </tr>' +
        '<tr> <td> <strong>KATEGORİ </strong> </td>' + '<td>' + feature.properties.ALT_KATEGORI.toUpperCase() + '</td> </tr>'+
         '<tr> <td> <strong>AMBULANS </strong> </td>' + '<td>' + feature.properties.AMBULANS.toUpperCase() + '</td> </tr>'+
         '<tr> <td> <strong>ACİL SERVİS </strong> </td>' + '<td>' + feature.properties.ACIL_SERVIS + '</td> </tr>' +
         '<tr> <td> <strong>İLÇE </strong> </td>' + '<td>' + feature.properties.ILCE_ADI + '</td> </tr>' 
         );
         layer.bindTooltip('Ayrıntılar için tıklayın.');
      }
})).addTo(map))
.catch(e => console.log(e));