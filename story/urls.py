from django.urls import path

from .views import StoriesView

app_name = 'story'

urlpatterns = [
    path('', StoriesView.as_view(), name='view'),
]
