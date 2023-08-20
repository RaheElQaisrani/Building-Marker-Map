var map = L.map('map').setView([44.5, -69.0], 8);

var near_coordinates = {{ near_coordinates | tojson | safe }};
var far_coordinates = {{ far_coordinates | tojson | safe }};

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to create a marker with a specified color
function createMarker(lat, lng, color) {
var latLng = L.latLng(lat, lng);

// Determine the icon URL based on the color
var iconUrl = color === 'blue' ? '{{ url_for("static", filename="assets/blue.png") }}' : '{{ url_for("static", filename="assets/red.png") }}';

var marker = L.marker(latLng, {
icon: L.icon({
    iconUrl: iconUrl,
    iconSize: [24, 24], // Adjust the size as needed
    iconAnchor: [12, 24] // Adjust the anchor point as needed
})
});

return marker;
}

// Add markers for near coordinates (red)
near_coordinates.forEach(function(coord) {
    var marker = createMarker(coord[1], coord[0], 'red');
    marker.addTo(map);
});

// Add markers for far coordinates (blue)
far_coordinates.forEach(function(coord) {
    var marker = createMarker(coord[1], coord[0], 'blue');
    marker.addTo(map);
});