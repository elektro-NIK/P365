from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from story.views import StoriesView

urlpatterns = [
    url(r'^wall/$', login_required(StoriesView.as_view()),       name='stories'),
]
