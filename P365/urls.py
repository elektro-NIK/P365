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

from maps.views import MapView, TracksView
from profile import urls as profile_urls
from profile.views import LoginView, ProfileRedirect, SignUpView, IndexView, CalendarView
from story.views import StoriesView

urlpatterns = [
    url(r'^$', IndexView.as_view(),                                 name='index'),
    url(r'^admin/', admin.site.urls,                                name='admin'),
    url(r'^login/$', LoginView.as_view(),                           name='login'),
    url(r'^register/$', SignUpView.as_view(),                       name='signup'),
    url(r'^logout/$', logout_then_login,                            name='logout'),
    url(r'^calendar/$', login_required(CalendarView.as_view()),     name='calendar'),
    url(r'^map/$', login_required(MapView.as_view()),               name='map'),
    url(r'^tracks/$', login_required(TracksView.as_view()),         name='tracks'),
    url(r'^stories/$', login_required(StoriesView.as_view()),       name='stories'),
    url(r'^accounts/profile/$', ProfileRedirect.as_view()),
    url(r'^user/', include(profile_urls)),
]
