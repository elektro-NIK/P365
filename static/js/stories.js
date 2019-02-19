$('div.well').on('click', 'a.btn-delete', function(){
    var well = $(this).parent().parent().parent(),
        id = well.attr('id').replace('story', ''),
        token = $('[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: url_story_delete.replace('0', id),
        data: {
            csrfmiddlewaretoken: token
        },
        success: function() {
            well.parent().addClass('hidden');
        },
        error: function() {
            setErrorMsg();
        }
    });
    return false;
});
