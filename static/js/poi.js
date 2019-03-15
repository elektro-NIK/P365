function map_init_basic (map, options) {
    $("input[name='leaflet-base-layers']").on('click', function () {
        var index = $("input[name='leaflet-base-layers']").index(this);
        localStorage.setItem('map_index', index);
    });
    var index = localStorage.getItem('map_index');
    if (index)
        $("input[name='leaflet-base-layers']")[index].click();
    $.getJSON(url_poi)
    .done(function (data) {
        var poi = L.geoJson(JSON.parse(data)).addTo(map);
        map.fitBounds(poi.getBounds());
        map.setZoom(13);
    }).fail(function() {setErrorMsg()});
}
