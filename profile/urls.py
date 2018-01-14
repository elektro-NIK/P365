from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from calendar_year.views import CalendarView
from maps.views import MapView, TracksView
from story.views import StoriesView
from .views import ProfileView

urlpatterns = [
    url(r'^(?P<username>\w+)/$', ProfileView.as_view(), name='profile'),
]
