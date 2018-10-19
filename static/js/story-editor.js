var mapsPlaceholder = [];

function map_init_basic (map, options) {
    mapsPlaceholder.push(map);
}

$(window).on('load', function() {
    $("select[name='track']").change();
});
