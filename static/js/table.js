if (location.hash) {
    $('a[href=\'' + location.hash + '\']').tab('show');
}
else {
    var activeTab = localStorage.getItem('activeTab');
    if (activeTab) {
        $('a[href="' + activeTab + '"]').tab('show');
    } else {
        $('a[href="#tracks"]').tab('show');
    }
}

$('body').on('click', "a[data-toggle='tab']", function (e) {
    e.preventDefault();
    var tab_name = this.getAttribute('href');
    if (history.pushState) {
        history.pushState(null, null, tab_name)
    }
    else {
        location.hash = tab_name
    }
    localStorage.setItem('activeTab', tab_name);

    $(this).tab('show');
    return false;
});

$(window).on('popstate', function () {
    var anchor = location.hash || $("a[data-toggle='tab']").first().attr('href');
    $("a[href='" + anchor + "']").tab('show');
});

function updateTable(url, id) {
    $.ajax({
        type: "GET",
        url: url,
        success: function(response) {
            $(id).html(response);
        },
        error: function() {
            setErrorMsg();
        }
    });
}

function changeFeature(url, id, url_upd, id_upd) {
    var token = $('[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: url.replace('0', id),
        data: {
            csrfmiddlewaretoken: token
        },
        success: function() {
            updateTable(url_upd, id_upd);
        },
        error: function() {
            setErrorMsg();
        }
    });
}

$('#table-tracks').on('click', 'td.status a', function() {
    var id = $(this).parent().parent().attr('id').replace('track', ''),
        url = url_track_status,
        url_upd = url_track_update,
        id_upd = "#table-tracks";
    if ($(this).attr('title') == 'public' && trackHasStory(url_track_has_story, id)) {
        if (confirm('The track has a related story. \nIf you make the track private - the story will be without the track. \nChange anyway?')) {
            var token = $('[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type: "POST",
                url: url_track_clear_story.replace('0', id),
                data: {
                    csrfmiddlewaretoken: token
                },
                error: function() {
                    setErrorMsg();
                }
            });
            changeFeature(url, id, url_upd, id_upd);
        }
    }
    else
        changeFeature(url, id, url_upd, id_upd);
    return false;
});

$('#table-routes').on('click', 'td.status a', function() {
    var id = $(this).parent().parent().attr('id').replace('route', ''),
        url = url_route_status,
        url_upd = url_route_update,
        id_upd = "#table-routes";
    changeFeature(url, id, url_upd, id_upd);
    return false;
});

$('#table-pois').on('click', 'td.status a', function() {
    var id = $(this).parent().parent().attr('id').replace('poi', ''),
        url = url_poi_status,
        url_upd = url_poi_update,
        id_upd = "#table-pois";
    changeFeature(url, id, url_upd, id_upd);
    return false;
});

function trackHasStory(url, id) {
    return $.ajax({
        type: "GET",
        url: url.replace('0', id),
        async: false
    }).responseJSON.result;
}

$('#table-tracks').on('click', 'td.edit a i.fa-trash', function(){
    var id = $(this).parent().parent().parent().attr('id').replace('track', ''),
        url = url_track_delete,
        url_upd = url_track_update,
        id_upd = "#table-tracks";
    changeFeature(url, id, url_upd, id_upd);
    return false;
});

$('#table-routes').on('click', 'td.edit a i.fa-trash', function(){
    var id = $(this).parent().parent().parent().attr('id').replace('route', ''),
        url = url_route_delete,
        url_upd = url_route_update,
        id_upd = "#table-routes";
    changeFeature(url, id, url_upd, id_upd);
    return false;
});

$('#table-pois').on('click', 'td.edit a i.fa-trash', function(){
    var id = $(this).parent().parent().parent().attr('id').replace('poi', ''),
        url = url_poi_delete,
        url_upd = url_poi_update,
        id_upd = "#table-pois";
    changeFeature(url, id, url_upd, id_upd);
    return false;
});
