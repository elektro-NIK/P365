from django.urls import path, include, register_converter

from P365.converters import UintWithoutZero
from map.models import POIModel
from map.views import POIView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, POIEditView

register_converter(UintWithoutZero, 'uint_id')

urlpatterns = [
    path('<uint_id:id>/',               POIView.as_view(),                      name='poi'),
    path('<uint_id:id>/edit/',          POIEditView.as_view(),                  name='poi_edit'),
    path('<uint_id:id>/', include([
        path('json_get/',           JSONFeatureView.as_view(),              name='json_poi'),
        path('json_change_status/', JSONFeatureChangeStatusView.as_view(),  name='json_poi_change_status'),
        path('json_delete/',        JSONFeatureDeleteView.as_view(),        name='json_poi_delete'),
    ]), {'model': POIModel}),
    path('json_ids/',               JSONFeatureIdsView.as_view(),   {'model': POIModel},    name='json_poi_ids'),
    path('json_get_all/',           JSONFeaturesView.as_view(),     {'model': POIModel},    name='json_pois'),
    path('create/',                 POIEditView.as_view(),                                  name='poi_create'),
]
