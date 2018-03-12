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

from profile import urls as urls_profile
from calendar_year import urls as urls_calendar
from map import urls_map, urls_poi, urls_route, urls_track
from table import urls as urls_table
from story import urls as urls_story

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
    # tabs
    url(r'^calendar/', include(urls_calendar)),
    url(r'^map/', include(urls_map)),
    url(r'^table/', include(urls_table)),
    url(r'^story/', include(urls_story)),
    # other
    url(r'^user/', include(urls_profile)),
    url(r'^poi/', include(urls_poi)),
    url(r'^route/', include(urls_route)),
    url(r'^track/', include(urls_track)),
]
