from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import MapView, GetTracksView, GetPoisView

urlpatterns = [
    url(r'^$', login_required(MapView.as_view()),                       name='map'),
    url(r'^geojson_tracks/$', login_required(GetTracksView.as_view()),  name='geojson_tracks'),
    url(r'^geojson_pois/$', login_required(GetPoisView.as_view()),      name='geojson_pois'),
]
