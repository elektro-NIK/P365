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

    $.getJSON(tracks_url, function (data) {
        var json = JSON.parse(data);
        L.geoJson(json, {
            onEachFeature: function (feature, layer) {
                layer.bindPopup('<p>' + '<b>' + feature.properties.name + '</b>' +
                                '<br>' + feature.properties.description, '</p>');
            }
        }).addTo(map)
    }).fail(function() {setErrorMsg()});

    $.getJSON(pois_url, function (data) {
        var json = JSON.parse(data);
        L.geoJson(json, {
            onEachFeature: function (feature, layer) {
                layer.bindPopup('<p>' + '<b>' + feature.properties.name + '</b>' +
                                '<br>' + feature.properties.description, '</p>');
            }
        }).addTo(map);
    }).fail(function() {setErrorMsg()});
}