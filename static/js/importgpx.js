$("#selectAllTracks, #selectAllRoutes").click(function() {
    $(this).siblings('div').children('input').prop('checked', this.checked);
});

//$('#save').click(function() {
//    $('#selectAllTracks').siblings('div').children('input:checked').each(function() {
//        var name = $(this).text();
//        $.getJSON("{% url 'geojson_gpx_track' %}", {'name': name})
//            .done(function(data) {
//                console.log(data);
//            })
//            .fail(function() {setErrorMsg()});
//    })
//});