from django.urls import path, include
from django.contrib.auth.decorators import login_required

from map.models import TrackModel
from map.views import TrackView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView

urlpatterns = [
    path('<int:id>/',                            login_required(TrackView.as_view()),                    name='track'),
    path('<int:id>/', include([
        path('json_get/',              login_required(JSONFeatureView.as_view()),              name='json_track'),
        path('json_change_status/',    login_required(JSONFeatureChangeStatusView.as_view()),  name='json_track_change_status'),
        path('json_delete/',           login_required(JSONFeatureDeleteView.as_view()),        name='json_track_delete'),
    ]), {'model': TrackModel}),
    path('json_ids/',       login_required(JSONFeatureIdsView.as_view()),   {'model': TrackModel}, name='json_track_ids'),
    path('json_get_all/',   login_required(JSONFeaturesView.as_view()),     {'model': TrackModel}, name='json_tracks'),
]
