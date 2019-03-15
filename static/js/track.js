function map_init_basic (map, options) {
    $("input[name='leaflet-base-layers']").on('click', function () {
        var index = $("input[name='leaflet-base-layers']").index(this);
        localStorage.setItem('map_index', index);
    });
    var index = localStorage.getItem('map_index');
    if (index)
        $("input[name='leaflet-base-layers']")[index].click();

    $.getJSON(url_track)
    .done(function (data) {
        var elevation = L.control.elevation({
            position: 'bottomleft',
            width: $('div.leaflet-container').width() - 20,
            height: 100,
            margins: {
                top: 10,
                right: 60,
                bottom: 20,
                left: 60
            },
            useHeightIndicator: true
        }).addTo(map);
        var track = L.geoJson(JSON.parse(data), {
            onEachFeature: elevation.addData.bind(elevation)
        }).addTo(map);
        map.fitBounds(track.getBounds());
    }).fail(function() {setErrorMsg()});
}
