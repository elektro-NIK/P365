function setErrorMsg() {
    $('#msg').html('<div class="alert alert-warning alert-dismissable fade in">' +
        '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>' +
        '<strong>Something went wrong!</strong> Please try again.' +
        '</div>')
}

function updateTable() {
    var table_url = '/get_tracks_table/';       // Fixme!
    $.ajax({
        type: 'GET',
        url: table_url,
        success: function(response) {
            $('#track-table').html(response);
        },
        error: function() {
            setErrorMsg();
        }
    });
}

$('#track-table').on('click', 'td.status a', function() {
    var id = $(this).attr('id').replace('status', '');
    $.ajax({
        type: 'POST',
        url: '/track/'+id+'/change_status/',   // Fixme!
        data: {
            csrfmiddlewaretoken: $('form').find('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function() {
            updateTable();
        },
        error: function() {
            setErrorMsg();
        }
    });
    return false;
});

$('#track-table').on('click', 'td.edit a.glyphicon-trash', function(){
    var id = $(this).attr('id').replace('delete', '');
    $.ajax({
        type: 'POST',
        url: '/track/'+id+'/delete/',
        data: {
            csrfmiddlewaretoken: $('form').find('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function() {
            $('#track'+id).hide();
        },
        error: function() {
            setErrorMsg();
        }
    });
    return false;
});