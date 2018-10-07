from django.urls import path, register_converter

from P365.converters import UintWithoutZero
from .views import StoriesView, StoryView, StoryEditView

app_name = 'story'

register_converter(UintWithoutZero, 'uint_id')

urlpatterns = [
    path('',                    StoriesView.as_view(),      name='stories'),
    path('<uint_id:id>/',       StoryView.as_view(),        name='view'),
    path('<uint_id:id>/edit/',  StoryEditView.as_view(),    name='edit'),
    path('create/',             StoryEditView.as_view(),    name='create'),
]
