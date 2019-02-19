function editEvent(event) {
    $('#event-modal input[name="event-index"]').val(event.id ? event.id : '');
    $('#event-modal input[name="event-name"]').val(event.name ? event.name : '');
    $('#event-modal textarea[name="event-description"]').val(event.description ? event.description : '');
    $('#event-modal input[name="event-start-date"]').datepicker('update', event.startDate ? event.startDate : '');
    $('#event-modal input[name="event-end-date"]').datepicker('update', event.endDate ? event.endDate : '');
    $('#event-modal').modal();
}

function deleteEvent(event) {
    var csrf_token = $("input[name='csrfmiddlewaretoken']")[0].value;
    $.ajax({
        type: "POST",
        url: url_delete,
        data: {
            csrfmiddlewaretoken: csrf_token,
            id: event.id
        },
        success: function() {
            updateAllEvents()
        },
        error: function() {
            setErrorMsg()
        }
    })
}

function saveEvent() {
    var update_event = {
        id: $('#event-modal input[name="event-index"]').val(),
        name: $('#event-modal input[name="event-name"]').val(),
        description: $('#event-modal textarea[name="event-description"]').val(),
        startDate: $('#event-modal input[name="event-start-date"]').datepicker('getDate'),
        endDate: $('#event-modal input[name="event-end-date"]').datepicker('getDate')
    };

    var csrf_token = $("input[name='csrfmiddlewaretoken']")[0].value
    $.ajax({
        type: "POST",
        url: url_save,
        data: {
            csrfmiddlewaretoken: csrf_token,
            event: JSON.stringify(update_event)
        },
        success: function() {
            updateAllEvents();
        },
        error: function() {
            setErrorMsg();
        }
    });
    $('#event-modal').modal('hide');
}

function updateAllEvents() {
    $.ajax({
        url: url_update,
        success: function (data) {
            for (var i in data) {
                data[i].startDate = new Date(data[i].startDate);
                data[i].endDate = new Date(data[i].endDate);
            }
            $('#calendar').data('calendar').setDataSource(data);
        },
        error: function() {
            setErrorMsg();
        }
    })
}

$(function() {
    $('#calendar').calendar({
        style:'border',
        enableContextMenu: true,
        enableRangeSelection: true,
        roundRangeLimits: true,
        contextMenuItems:[
            {
                text: 'Edit',
                click: editEvent
            },
            {
                text: 'Delete',
                click: deleteEvent
            }
        ],
        selectRange: function(e) {
            editEvent({ startDate: e.startDate, endDate: e.endDate });
        },
        mouseOnDay: function(e) {
            if(e.events.length > 0) {
                var content = '';
                for(var i in e.events) {
                    content += '<div class="event-tooltip-content">'
                             + '<div class="event-name" style="color:' + e.events[i].color + '">' + e.events[i].name + '</div>'
                             + '<div class="event-description">' + e.events[i].description + '</div>'
                             + '</div>';
                }
                $(e.element).popover({
                    trigger: 'manual',
                    container: 'body',
                    html:true,
                    content: content
                });
                $(e.element).popover('show');
            }
        },
        mouseOutDay: function(e) {
            if(e.events.length > 0) {
                $(e.element).popover('hide');
            }
        },
        dayContextMenu: function(e) {
            $(e.element).popover('hide');
        }
    });
    $('#save-event').click(function() {
        saveEvent();
    });
    updateAllEvents();
});
