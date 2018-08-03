from django.urls import path

from calendar_year.views import CalendarView, GetAllEventsView, DeleteEventView, UpdateCreateEventView

app_name = 'calendar'

urlpatterns = [
    path('',                        CalendarView.as_view(),             name='view'),
    path('get_all_events/',         GetAllEventsView.as_view(),         name='get_all_events'),
    path('delete_event/',           DeleteEventView.as_view(),          name='delete_event'),
    path('update_or_create_event/', UpdateCreateEventView.as_view(),    name='update_event'),
]
