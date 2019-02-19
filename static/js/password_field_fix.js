if ($("#id_password")[0]) {
    var input = $("#id_password")[0].outerHTML;
    $("#id_password").replaceWith(
        '<div class="input-group">' +
            '<span class="input-group-addon">' +
                '<i class="glyphicon glyphicon-lock"></i>' +
            '</span>' +
            input +
        '</div>'
    );
}
else if ($("#id_password1")[0] && $("#id_password2")[0]) {
    var input = $("#id_password1")[0].outerHTML;
    $("#id_password1").replaceWith(
        '<div class="input-group">' +
            '<span class="input-group-addon">' +
                '<i class="glyphicon glyphicon-lock"></i>' +
            '</span>' +
            input +
        '</div>'
    );
    input = $("#id_password2")[0].outerHTML;
    $("#id_password2").replaceWith(
        '<div class="input-group">' +
            '<span class="input-group-addon">' +
                '<i class="glyphicon glyphicon-lock"></i>' +
            '</span>' +
            input +
        '</div>'
    );
}
