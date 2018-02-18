"""P365 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

from profile import urls as profile_urls
from calendar_year import urls as calendar_urls
from maps import urls as map_urls

from maps.views import TracksView, TrackChangeStatusView, GetTracksTableView, TrackEditView, TrackView
from profile.views import LoginView, ProfileRedirect, SignUpView, IndexView
from story.views import StoriesView

urlpatterns = [
    url(r'^$', IndexView.as_view(),                                 name='index'),
    url(r'^admin/', admin.site.urls,                                name='admin'),

    url(r'^login/$', LoginView.as_view(),                           name='login'),
    url(r'^register/$', SignUpView.as_view(),                       name='signup'),
    url(r'^logout/$', logout_then_login,                            name='logout'),

    url(r'^accounts/profile/$', ProfileRedirect.as_view()),
    url(r'^user/', include(profile_urls)),

    url(r'^calendar/', include(calendar_urls)),
    url(r'^map/', include(map_urls)),
    url(r'^tracks/$', login_required(TracksView.as_view()),         name='tracks'),
    url(r'^stories/$', login_required(StoriesView.as_view()),       name='stories'),

    url(r'^track/(\d+)/$', TrackView.as_view(),                     name='track'),
    url(r'^track/(\d+)/edit/$',
        login_required(TrackEditView.as_view()),                    name='edit_track'),
    url(r'^track/(\d+)/change_status/$',
        login_required(TrackChangeStatusView.as_view()),            name='change_track_status'),
    url(r'^get_tracks_table/$',
        login_required(GetTracksTableView.as_view()),               name='get_tracks_table'),
]
