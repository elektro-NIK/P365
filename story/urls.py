from django.urls import path

from story.views import StoriesView

urlpatterns = [
    path('', StoriesView.as_view(), name='stories'),
]
