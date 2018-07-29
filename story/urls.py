from django.urls import path
from django.contrib.auth.decorators import login_required

from story.views import StoriesView

urlpatterns = [
    path('', login_required(StoriesView.as_view()), name='stories'),
]
