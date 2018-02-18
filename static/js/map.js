function setErrorMsg() {
    $('#msg-wrong').html('<div class="alert alert-warning alert-dismissable fade in">' +
        '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>' +
        '<strong>Something went wrong!</strong> Please try again.' +
        '</div>')
}

function map_init_basic (map, options) {
    // Fixme!
    var tracks_url = '/map/geojson_tracks/';
    var pois_url = '/map/geojson_pois/';

    var bounds;

    $.getJSON(tracks_url, function (data) {
        var json = JSON.parse(data);
        b = L.geoJson(json, {
            onEachFeature: function (feature, layer) {
                layer.bindPopup('<p>' + '<b>' + feature.properties.name + '</b>' +
                                '<br>' + feature.properties.description, '</p>');
            }
        });
        b.addTo(map)
        bounds = b.getBounds();
    }).fail(function() {setErrorMsg()});

    $.getJSON(pois_url, function (data) {
        var json = JSON.parse(data);
        var b = L.geoJson(json, {
            onEachFeature: function (feature, layer) {
                layer.bindPopup('<p>' + '<b>' + feature.properties.name + '</b>' +
                                '<br>' + feature.properties.description, '</p>');
            }
        });
        b.addTo(map);
        bounds += b.getBounds();
        map.fitBounds(b.getBounds());
    }).fail(function() {setErrorMsg()});
}