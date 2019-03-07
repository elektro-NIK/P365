function map_init_basic (map, options) {
    map.dragging.disable();
    map.touchZoom.disable();
    map.doubleClickZoom.disable();
    map.scrollWheelZoom.disable();
    map.boxZoom.disable();
    map.keyboard.disable();
    if (map.tap) map.tap.disable();
    $(".leaflet-control-container").css("visibility", "hidden");

    var track_id = parseInt(map._container.id.split('_')[1]);
    if (track_id) {
        $.getJSON(url_track_json.replace('0', track_id))
            .done(function (data) {
                var track = L.geoJson(JSON.parse(data)).addTo(map);
                map.fitBounds(track.getBounds());
            }).fail(function () {
            setErrorMsg()
        });
    } else {
        map.setZoom(1);
    }
}

$('a.btn-delete').on('click', function(event) {
    event.preventDefault();
    event.stopPropagation();
    var card = $(this).parent().parent().parent().parent(),
        id = card.attr('id').replace('story-', ''),
        token = $('[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: url_story_delete.replace('0', id),
        data: {
            csrfmiddlewaretoken: token
        },
        success: function() {
            card.parent().hide();
        },
        error: function() {
            setErrorMsg();
        }
    });
});
