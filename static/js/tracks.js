function setErrorMsg() {
    $('#msg').html('<div class="alert alert-warning alert-dismissable fade in">' +
        '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>' +
        '<strong>Something went wrong!</strong> Please try again.' +
        '</div>')
}

$('td.status a').click(function() {
    var id = $(this).attr('id').replace('status', '');
    var a = $(this);
    $.ajax({
        type: 'POST',
        url: '/track/'+id+'/change_status/',
        data: {
            csrfmiddlewaretoken: $('form').find('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function() {
            icon = a.attr('class')
            if (icon.includes('globe')) {
                a.attr('class', icon.replace('globe', 'user'));
                a.attr('title', 'private');
            }
            else {
                a.attr('class', icon.replace('user', 'globe'));
                a.attr('title', 'public');
            }
        },
        error: function() {
            setErrorMsg();
        }
    })
    return false;
})