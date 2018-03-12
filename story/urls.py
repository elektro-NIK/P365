from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from story.views import StoriesView

urlpatterns = [
    url(r'^$', login_required(StoriesView.as_view()),       name='stories'),
]
