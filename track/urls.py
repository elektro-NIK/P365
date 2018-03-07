from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import TrackView, GetTrackView, TrackEditView, TrackChangeStatusView, TrackDeleteView, GetTracksTableView, TracksView


urlpatterns = [
    url(r'^(\d+)/$', TrackView.as_view(),                                           name='track'),
    url(r'^(\d+)/edit/$', login_required(TrackEditView.as_view()),                  name='edit_track'),
    url(r'^(\d+)/delete/$', login_required(TrackDeleteView.as_view()),              name='delete_track'),
    url(r'^(\d+)/change_status/$', login_required(TrackChangeStatusView.as_view()), name='change_track_status'),
    url(r'^(\d+)/json/$', GetTrackView.as_view(),                                   name='geojson_get_track'),
    url(r'^table/$', login_required(TracksView.as_view()),                          name='tracks'),
    url(r'^json_table/$', login_required(GetTracksTableView.as_view()),             name='get_tracks_table'),
]
