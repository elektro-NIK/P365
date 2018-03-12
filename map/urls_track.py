from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from map.models import TrackModel
from map.views import TrackView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$',
        login_required(TrackView.as_view()),                                          name='track'),
    url(r'^json_ids/$',
        login_required(JSONFeatureIdsView.as_view()),          {'model': TrackModel}, name='json_track_ids'),
    url(r'^(?P<id>[0-9]+)/json_get/$',
        login_required(JSONFeatureView.as_view()),             {'model': TrackModel}, name='json_track'),
    url(r'^json_get_all/$',
        login_required(JSONFeaturesView.as_view()),            {'model': TrackModel}, name='json_tracks'),
    url(r'^(?P<id>[0-9]+)/json_change_status/$',
        login_required(JSONFeatureChangeStatusView.as_view()), {'model': TrackModel}, name='json_track_change_status'),
    url(r'^(?P<id>[0-9]+)/json_delete/$',
        login_required(JSONFeatureDeleteView.as_view()),       {'model': TrackModel}, name='json_track_delete'),
]
