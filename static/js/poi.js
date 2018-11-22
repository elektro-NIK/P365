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
    $('div.leaflet-container').height(height);
    map.invalidateSize();

    $.getJSON(url_poi)
    .done(function (data) {
        var poi = L.geoJson(JSON.parse(data)).addTo(map);
        map.fitBounds(poi.getBounds());
        map.setZoom(13);
    }).fail(function() {setErrorMsg()});
}
