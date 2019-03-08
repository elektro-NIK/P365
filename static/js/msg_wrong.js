function setErrorMsg() {
    $('#msg-wrong').html('' +
        '<div class="alert alert-warning alert-dismissable fade show" role="alert">\n' +
        '    <strong>Something went wrong!</strong> Please try again.\n' +
        '    <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
        '        <span aria-hidden="true">&times;</span>\n' +
        '    </button>\n' +
        '</div>'
    );
}
