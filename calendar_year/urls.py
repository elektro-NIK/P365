from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from calendar_year.views import CalendarView, GetAllEventsView, DeleteEventView, UpdateCreateEventView

urlpatterns = [
    url(r'^$', login_required(CalendarView.as_view()),                                  name='calendar'),
    url(r'^get_all_events/$', login_required(GetAllEventsView.as_view()),               name='get_all_events'),
    url(r'^delete_event/$', login_required(DeleteEventView.as_view()),                  name='delete_event'),
    url(r'^update_or_create_event/$', login_required(UpdateCreateEventView.as_view()),  name='update_event'),
]
