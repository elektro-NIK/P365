from django.urls import path, register_converter

from P365.converters import UintWithoutZero
from .views import CalendarView, DatesEventView, GetAllEventsView, DeleteEventView, UpdateCreateEventView

app_name = 'calendar'

register_converter(UintWithoutZero, 'uint_id')

urlpatterns = [
    path('',                        CalendarView.as_view(),             name='view'),
    path('<uint_id:id>/dates_get/', DatesEventView.as_view(),           name='dates_event'),
    path('get_all_events/',         GetAllEventsView.as_view(),         name='get_all_events'),
    path('delete_event/',           DeleteEventView.as_view(),          name='delete_event'),
    path('update_or_create_event/', UpdateCreateEventView.as_view(),    name='update_event'),
]
