$(window).on('map:init', function (e) {
    var detail = e.originalEvent ?
                 e.originalEvent.detail : e.detail;
    var info_height = $('#info').height()
    var page_height = $(document).height()
    var window_height = $(window).height()
    var header_height = $('#header_container').height() + parseInt($('#header_container').css('margin-bottom').replace('px', ''))
    var footer_height = $('#footer_container').height() + parseInt($('#footer_container').css('margin-top').replace('px', ''))
    var button_height = $('#buttons').height() + parseInt($('.leaflet-container').css('margin-bottom').replace('px', ''))
    if (info_height + header_height >= window_height) {
        height = window_height - header_height;
    }
    else if (info_height + header_height + button_height + footer_height <= window_height) {
        height = page_height - header_height - button_height - footer_height;
    }
    else {
        height = info_height
    }
    $('div.leaflet-container').height(height);
    detail.map.invalidateSize();
});