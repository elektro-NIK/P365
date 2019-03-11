var mapsPlaceholder = [];
var bounds;

function map_init_basic (map, options) {
    $("input[name='leaflet-base-layers']").on('click', function () {
        var index = $("input[name='leaflet-base-layers']").index(this);
        localStorage.setItem('map_index', index);
    });
    var index = localStorage.getItem('map_index');
    if (index)
        $("input[name='leaflet-base-layers']")[index].click();

    mapsPlaceholder.push(map);
    bounds = map.getBounds();
    map.on('click', function() {
        bounds && bounds.isValid() ? map.fitBounds(bounds) : {};
    });
}

$("select[name='track']").on('change', function() {
    var map = mapsPlaceholder.pop();
    map.eachLayer(function (layer) {
        if (!layer._url)
            map.removeLayer(layer);
    });
    if (this.value) {
        url = url_track_json.replace("0", this.value);
        $.getJSON(url)
        .done(function (data) {
            var track = L.geoJson(JSON.parse(data), {
                onEachFeature: function(feature, layer) {
                    layer.bindPopup(feature.properties.description || '');
                }
            }).addTo(map);
            bounds = track.getBounds();
            map.fitBounds(bounds);
        })
        .fail(function() {setErrorMsg()});
    }
    mapsPlaceholder.push(map);
});

$("select[name='event']").on('change', function() {
    $("#event-dates").html("");
    if (this.value) {
        url = url_calendar_dates.replace("0", this.value);
        $.ajax({
            url: url,
            success: function (data) {
                $("#event-dates").html(data);
            },
            error: function() {setErrorMsg()}
        });
    }
});

$(window).on('load', function() {
    $("select[name='track']").change();
    $("select[name='event']").change();
});