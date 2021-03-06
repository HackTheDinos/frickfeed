function init() {
  var map = L.map('shippingRecord', {
    maxZoom: 24,
    minZoom: 1,
    crs: L.CRS.Simple
  }).setView([200, 100], 1);

  map.setMaxBounds(new L.LatLngBounds([0,500], [500,0]));

  var imageUrl = 'static/img/shipping_records/frick_2.png';
  var imageBounds = [[250,0], [0,250]];

  L.imageOverlay(imageUrl, imageBounds).addTo(map);
}

init();
