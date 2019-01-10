$(window).on('map:init', function (e) {
    $("input[name='leaflet-base-layers']").on('click', function () {
        var index = $("input[name='leaflet-base-layers']").index(this);
        localStorage.setItem('map_index', index);
    });
    var index = localStorage.getItem('map_index');
    if (index)
        $("input[name='leaflet-base-layers']")[index].click();

    var detail = e.originalEvent ?
                 e.originalEvent.detail : e.detail;
    var info_height = $('#info').height();
    var page_height = $(document).height();
    var window_height = $(window).height();
    var header_height = $('#header_container').height() + parseInt($('#header_container').css('margin-bottom').replace('px', ''));
    var footer_height = $('footer').height();
    if (info_height + header_height >= window_height)
        var height = window_height - header_height;
    else if (info_height + header_height + footer_height <= window_height)
        var height = page_height - header_height - footer_height - parseInt($('div.form-group').css('margin-bottom').replace('px', '')) - 2;
    else
        var height = info_height;
    $('div.leaflet-container').height(height);
    detail.map.invalidateSize();
    detail.map.setZoom(7);

    detail.map.on('click', function(e) {
        var layers = [];
        var poi = null;
        var counter = 0;
        detail.map.eachLayer(function(layer) {
            if (layer instanceof L.Polyline)
                layers.push(layer);
            if (layer instanceof L.Marker) {
                poi = layer
                counter++;
            }
        })
        if (layers.length > 0 && counter == 0)
            detail.map.fitBounds(L.featureGroup(layers).getBounds());
        if (poi && counter == 1) {
            var zoom = detail.map.getZoom()
            detail.map.fitBounds(L.latLngBounds([poi.getLatLng()]));
            detail.map.setZoom(zoom);
        }
    });
});