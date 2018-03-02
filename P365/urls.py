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
from django.contrib.auth.views import logout_then_login

from profile import urls as profile_urls
from calendar_year import urls as calendar_urls
from map import urls as map_urls
from track import urls as track_urls
from story import urls as story_urls
from gpx import urls as gpx_urls

from profile.views import LoginView, ProfileRedirect, SignUpView, IndexView

urlpatterns = [
    # main
    url(r'^$', IndexView.as_view(),                                 name='index'),
    url(r'^admin/', admin.site.urls,                                name='admin'),
    # auth
    url(r'^login/$', LoginView.as_view(),                           name='login'),
    url(r'^register/$', SignUpView.as_view(),                       name='signup'),
    url(r'^logout/$', logout_then_login,                            name='logout'),
    # redirection
    url(r'^accounts/profile/$', ProfileRedirect.as_view()),
    # includes
    url(r'^user/', include(profile_urls)),
    url(r'^calendar/', include(calendar_urls)),
    url(r'^track/', include(track_urls)),
    url(r'^map/', include(map_urls)),
    url(r'^story/', include(story_urls)),
    url(r'^gpx/', include(gpx_urls)),
]
