if (location.hash) {
    $('a[href=\'' + location.hash + '\']').tab('show');
}
var activeTab = localStorage.getItem('activeTab');
if (activeTab) {
    $('a[href="' + activeTab + '"]').tab('show');
}

$('body').on('click', 'a[data-toggle=\'tab\']', function (e) {
    e.preventDefault()
    var tab_name = this.getAttribute('href')
    if (history.pushState) {
        history.pushState(null, null, tab_name)
    }
    else {
        location.hash = tab_name
    }
    localStorage.setItem('activeTab', tab_name)

    $(this).tab('show');
    return false;
});

$(window).on('popstate', function () {
    var anchor = location.hash || $('a[data-toggle=\'tab\']').first().attr('href');
    $('a[href=\'' + anchor + '\']').tab('show');
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

function updateAllTables() {
    updateTable(url_update_tracks, "#table-tracks");
    updateTable(url_update_routes, "#table-routes");
    updateTable(url_update_pois,   "#table-pois");
}

function changeFeature(url, id, token, url_upd, id_upd) {
    $.ajax({
        type: "POST",
        url: url.replace('0', id),
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function() {
            updateTable(url_upd, id_upd);
        },
        error: function() {
            setErrorMsg();
        }
    });
}
