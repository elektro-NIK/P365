function delete_feature (map, feature, url) {
    var token = $('[name=csrfmiddlewaretoken]').val()
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function() {
            map.eachLayer(function (layer) {
                if (layer.feature == feature)
                    map.removeLayer(layer);
            });
        },
        error: function() {
            setErrorMsg();
        }
    });
}

function addPopup (map, feature, layer, url, url_edit, url_delete) {
    var popup = $('<p>').append($('<a>').attr('href', url.replace('0', feature.properties.pk)).html($('<b>').html(feature.properties.name)), ' ');
    if (url_edit)
        popup.append($('<a>').attr('href', url_edit.replace('0', feature.properties.pk)).addClass('glyphicon glyphicon-pencil'), ' ');
    if (!feature.properties.public)
        popup.append($('<a>').attr('href', '#').addClass('glyphicon glyphicon-trash').on('click', function() {
            delete_feature(map, feature, url_delete.replace('0', feature.properties.pk));
        }));
    popup.append($('<br>'), (feature.properties.description || ''));
    layer.bindPopup(popup[0]);
}

function parseData (map, data, url, url_edit, url_delete) {
    var json = JSON.parse(data);
    b = L.geoJson(json, {
        onEachFeature: function(feature, layer) {
            addPopup(map, feature, layer, url, url_edit, url_delete);
            layer.on('click', function() {
                this.feature.geometry.type != 'Point' ? map.fitBounds(this.getBounds()) : {};
            });
        }
    });
    b.addTo(map);
    bounds ? bounds.extend(b.getBounds()) : bounds = b.getBounds();
    bounds.isValid() ? map.fitBounds(bounds) : {};
}

function get_all (map, url_ids, url_get, url_show, url_edit, url_delete) {
    $.getJSON(url_ids)
    .done(function(data) {
        if (data.length > 0) {
            if (progress < 0) {
                progress += 1;
                $('.leaflet-container').height($('.leaflet-container').height() - 5);
            }
            $('.progress').show();
            for (i = 0; i < data.length; i++) {
                var url = url_get.replace('0', data[i]);
                var step = 1./3/data.length;
                $.getJSON(url)
                .done(function(data) {
                    progress += step;
                    $('.progress-bar').css('width', (progress*100).toString()+'%');
                    if (progress > 1.000001-step) {
                        $('.progress').hide();
                        $('.leaflet-container').height('100%');
                    }
                    parseData(map, data, url_show, url_edit, url_delete);
                })
                .fail(function() {setErrorMsg()});
            }
        }
        else
            progress += 1./3;
    })
    .fail(function() {setErrorMsg()});
}