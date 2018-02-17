$(window).on('map:init', function (e) {
    var detail = e.originalEvent ?
                 e.originalEvent.detail : e.detail;
    var height;
    if($(window).height() > $(document).height()) {
        height = $(window).height()-180;                                // <--- Fixme
    }
    else {
        height = $(window).height() * 2 - $(document).height() - 70;    // <--- Fixme
    }
    $('div.leaflet-container').height(height);
    detail.map.invalidateSize();
});