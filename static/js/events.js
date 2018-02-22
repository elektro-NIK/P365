function setErrorMsg() {
    $('#msg-wrong').html('<div class="alert alert-warning alert-dismissable fade in">' +
        '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>' +
        '<strong>Something went wrong!</strong> Please try again.' +
        '</div>')
}

function editEvent(event) {
    $('#event-modal input[name="event-index"]').val(event.id ? event.id : '');
    $('#event-modal input[name="event-name"]').val(event.name ? event.name : '');
    $('#event-modal textarea[name="event-description"]').val(event.description ? event.description : '');
    $('#event-modal input[name="event-start-date"]').datepicker('update', event.startDate ? event.startDate : '');
    $('#event-modal input[name="event-end-date"]').datepicker('update', event.endDate ? event.endDate : '');
    $('#event-modal').modal();
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
        },
    });
    $('#save-event').click(function() {
        saveEvent();
    });
    updateAllEvents();
})
