from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

import calendar_year.urls
import profile.urls
import story.urls
import table.urls
from map import urls_map, urls_poi, urls_route, urls_track
from profile.views import LoginView, ProfileRedirect, SignUpView, IndexView

urlpatterns = [
    # main
    path('',            IndexView.as_view(),        name='index'),
    path('admin/',      admin.site.urls,            name='admin'),
    # auth
    path('login/',      LoginView.as_view(),        name='login'),
    path('register/',   SignUpView.as_view(),       name='signup'),
    path('logout/',     logout_then_login,          name='logout'),
    # redirection
    path('accounts/profile/', ProfileRedirect.as_view()),
    # tabs
    path('calendar/',   include(calendar_year.urls, namespace='calendar')),
    path('map/',        include(urls_map,           namespace='map')),
    path('table/',      include(table.urls,         namespace='table')),
    path('story/',      include(story.urls,         namespace='story')),
    # other
    path('user/',       include(profile.urls,       namespace='user')),
    path('poi/',        include(urls_poi,           namespace='poi')),
    path('route/',      include(urls_route,         namespace='route')),
    path('track/',      include(urls_track,         namespace='track')),
]
