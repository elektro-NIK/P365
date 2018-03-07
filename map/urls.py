from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import MapView, GetPoisView, TracksNumsView, GetTrackView

urlpatterns = [
    url(r'^$', login_required(MapView.as_view()),                           name='map'),
    url(r'^geojson_pois/$', login_required(GetPoisView.as_view()),          name='geojson_pois'),
    url(r'^json_tracks_nums/$', login_required(TracksNumsView.as_view()),   name='json_tracks_nums'),
    url(r'^geojson_track/(\d+)/$', login_required(GetTrackView.as_view()),  name='geojson_track'),
]
