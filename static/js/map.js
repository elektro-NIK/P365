function parseData (map, data, url, url_edit) {
    var json = JSON.parse(data);
    b = L.geoJson(json, {
        onEachFeature: function (feature, layer) {
            var popup =
            '<p>' +
                '<a href="' + url.replace('0', feature.properties.pk) + '">' +
                    '<b>' + feature.properties.name + '</b>' +
                '</a>';
            if (url_edit)
                popup += ' <a href="' + url_edit.replace('0', feature.properties.pk) + '" class="glyphicon glyphicon-pencil"></a>'
            popup += '<br>' + feature.properties.description + '</p>'
            layer.bindPopup(popup);
            layer.on('click', function() {
                map.fitBounds(this.getBounds());
             });
        }
    });
    b.addTo(map);
    bounds ? bounds.extend(b.getBounds()) : bounds = b.getBounds()
    bounds.isValid() ? map.fitBounds(bounds) : {}
}

function get_all (map, url_ids, url_get, url_show, url_edit) {
    $.getJSON(url_ids)
    .done(function(data) {
        if (data.length > 0) {
            $('.leaflet-container').height($('.leaflet-container').height() - 5);
            $('.progress').show();
            for (i = 0; i < data.length; i++) {
                var id = data[i];
                var url = url_get.replace('0', id);
                var step = 1./3/data.length;
                $.getJSON(url)
                .done(function(data) {
                    progress += step;
                    $('.progress-bar').css('width', (progress*100).toString()+'%');
                    if (progress > 1.000001-step) {
                        $('.progress').hide();
                        $('.leaflet-container').height('100%');
                    }
                    parseData(map, data, url_show, url_edit);
                })
                .fail(function()     {setErrorMsg()});
            }
        }
        else {
            progress += 1./3
        }
    })
    .fail(function() {setErrorMsg()});
}