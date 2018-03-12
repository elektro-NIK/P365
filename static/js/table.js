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
    updateTracksTable();
    updateRoutesTable();
    updatePoisTable();
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
