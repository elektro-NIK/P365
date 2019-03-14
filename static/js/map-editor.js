$(window).on('map:init', function (e) {
    $("input[name='leaflet-base-layers']").on('click', function () {
        var index = $("input[name='leaflet-base-layers']").index(this);
        localStorage.setItem('map_index', index);
    });
    var index = localStorage.getItem('map_index');
    if (index)
        $("input[name='leaflet-base-layers']")[index].click();

    var map = e.originalEvent ? e.originalEvent.detail.map : e.detail.map;
    map.setZoom(7);

    map.on('click', function() {
        var layers = [];
        var poi = null;
        var counter = 0;
        map.eachLayer(function(layer) {
            if (layer instanceof L.Polyline)
                layers.push(layer);
            if (layer instanceof L.Marker) {
                poi = layer;
                counter++;
            }
        });
        if (layers.length > 0 && counter === 0)
            map.fitBounds(L.featureGroup(layers).getBounds());
        if (poi && counter === 1) {
            var zoom = map.getZoom();
            map.fitBounds(L.latLngBounds([poi.getLatLng()]));
            map.setZoom(zoom);
        }
    });
});