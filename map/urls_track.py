from django.urls import path, include, register_converter

from P365.converters import UintWithoutZero
from map.models import TrackModel
from map.views import TrackView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, TrackEditView, JSONFeatureHasStory, JSONFeatureClearStory

app_name = 'track'

register_converter(UintWithoutZero, 'uint_id')

urlpatterns = [
    path('<uint_id:id>/',               TrackView.as_view(),                    name='view'),
    path('<uint_id:id>/edit/',          TrackEditView.as_view(),                name='edit'),
    path('<uint_id:id>/', include([
        path('json_get/',           JSONFeatureView.as_view(),              name='json'),
        path('json_change_status/', JSONFeatureChangeStatusView.as_view(),  name='json_change_status'),
        path('json_delete/',        JSONFeatureDeleteView.as_view(),        name='json_delete'),
        path('json_has_story/',     JSONFeatureHasStory.as_view(),          name='json_has_story'),
        path('json_clear_story/',   JSONFeatureClearStory.as_view(),        name='json_clear_story'),
    ]), {'model': TrackModel}),
    path('json_ids/',               JSONFeatureIdsView.as_view(),   {'model': TrackModel},  name='json_ids'),
    path('json_get_all/',           JSONFeaturesView.as_view(),     {'model': TrackModel},  name='jsons'),
]
