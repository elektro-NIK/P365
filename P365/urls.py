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
    path('', IndexView.as_view(),                           name='index'),
    path('admin/', admin.site.urls,                         name='admin'),
    # auth
    path('login/', LoginView.as_view(),                     name='login'),
    path('register/', SignUpView.as_view(),                 name='signup'),
    path('logout/', logout_then_login,                      name='logout'),
    # redirection
    path('accounts/profile/', ProfileRedirect.as_view()),
    # tabs
    path('calendar/', include(calendar_year.urls)),
    path('map/', include(urls_map)),
    path('table/', include(table.urls)),
    path('story/', include(story.urls)),
    # other
    path('user/', include(profile.urls)),
    path('poi/', include(urls_poi)),
    path('route/', include(urls_route)),
    path('track/', include(urls_track)),
]
