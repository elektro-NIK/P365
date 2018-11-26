function map_init_basic (map, options) {
    var info_height = $('#info').height();
    var page_height = $(document).height();
    var window_height = $(window).height();
    var header_height = $('#header_container').height() + parseInt($('#header_container').css('margin-bottom').replace('px', ''));
    var footer_height = $('footer').height();
    if (info_height + header_height >= window_height)
        var height = window_height - header_height;
    else if (info_height + header_height + footer_height <= window_height)
        var height = page_height - header_height - footer_height - parseInt($('#header_container').css('margin-bottom').replace('px', '')) - 2;
    else
        var height = info_height;
    var height = window_height - header_height - parseInt($('#header_container').css('margin-bottom').replace('px', ''));
    $('div.leaflet-container').height(height);
    map.invalidateSize();
    bounds = map.getBounds();
    map.on('click', function() {
        bounds && bounds.isValid() ? map.fitBounds(bounds) : {};
    });

    $.getJSON(url_track_json)
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
            useHeightIndicator: true,
        }).addTo(map);
        var track = L.geoJson(JSON.parse(data), {
            onEachFeature: elevation.addData.bind(elevation)
        }).addTo(map);
        bounds = track.getBounds();
        map.fitBounds(bounds);
    }).fail(function() {setErrorMsg()});
}
