// Haritamızı oluşturmak için map isimli bir değişken tanımlıyoruz
var map = L.map('map').setView([41.1245, 28.9100], 10);


//Haritamızın görüntüleneceği tile katmanını ayarlıyoruz. Bu projede OpenStreetMap kullanacağız.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a target="blank" href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' +
      ' | &copy; <a  target="blank" href="https://data.ibb.gov.tr/license">IBB Lisans</a>'
}).addTo(map);