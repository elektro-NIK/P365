from django.urls import path, include

from map.models import TrackModel
from map.views import TrackView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView

urlpatterns = [
    path('<int:id>/',               TrackView.as_view(),                    name='track'),
    path('<int:id>/', include([
        path('json_get/',           JSONFeatureView.as_view(),              name='json_track'),
        path('json_change_status/', JSONFeatureChangeStatusView.as_view(),  name='json_track_change_status'),
        path('json_delete/',        JSONFeatureDeleteView.as_view(),        name='json_track_delete'),
    ]), {'model': TrackModel}),
    path('json_ids/',               JSONFeatureIdsView.as_view(),   {'model': TrackModel},  name='json_track_ids'),
    path('json_get_all/',           JSONFeaturesView.as_view(),     {'model': TrackModel},  name='json_tracks'),
]
