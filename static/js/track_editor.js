$(window).on('map:init', function (e) {
    var detail = e.originalEvent ?
                 e.originalEvent.detail : e.detail;
    $('div.leaflet-container').height($(window).height()-180);   // <--- Fixme
    detail.map.invalidateSize();
});