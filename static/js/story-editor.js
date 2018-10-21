var mapsPlaceholder = [];

function map_init_basic (map, options) {
    mapsPlaceholder.push(map);
    var form_height = $('#other').height();
    var page_height = $(document).height();
    var window_height = $(window).height();
    var header_height = $('#header_container').height() + parseInt($('#header_container').css('margin-bottom').replace('px', ''));
    var footer_height = $('footer').height();
    var selector_height = $("select[name='track']").parent().height() + parseInt($("select[name='track']").parent().css('margin-bottom').replace('px', ''));
    if (form_height + header_height >= window_height)
        var height = window_height - header_height;
    else if (form_height + header_height + footer_height <= window_height)
        var height = page_height - header_height - footer_height - parseInt($('#header_container').css('margin-bottom').replace('px', '')) - 2;
    else
        var height = form_height;
    $('div.leaflet-container').height(height - selector_height);
    map.invalidateSize();
}

$(window).on('load', function() {
    $("select[name='track']").change();
    $("select[name='event']").change();
});
