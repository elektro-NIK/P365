function map_init_basic (map, options) {
    var tracks_url = '/map/geojson_tracks/';
    var pois_url = '/map/geojson_pois/';

    $.getJSON(tracks_url, function (data) {
        var json = JSON.parse(data);
        L.geoJson(json).addTo(map);
    });

    $.getJSON(pois_url, function (data) {
        var json = JSON.parse(data);
        L.geoJson(json).addTo(map);
    })
}