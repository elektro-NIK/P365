from django.urls import path, include

from map.models import POIModel
from map.views import POIView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, POIEditView

urlpatterns = [
    path('<int:id>/',               POIView.as_view(),                      name='poi'),
    path('<int:id>/edit/',          POIEditView.as_view(),                  name='poi_edit'),
    path('<int:id>/', include([
        path('json_get/',           JSONFeatureView.as_view(),              name='json_poi'),
        path('json_change_status/', JSONFeatureChangeStatusView.as_view(),  name='json_poi_change_status'),
        path('json_delete/',        JSONFeatureDeleteView.as_view(),        name='json_poi_delete'),
    ]), {'model': POIModel}),
    path('json_ids/',               JSONFeatureIdsView.as_view(),   {'model': POIModel},    name='json_poi_ids'),
    path('json_get_all/',           JSONFeaturesView.as_view(),     {'model': POIModel},    name='json_pois'),
    path('create/',                 POIEditView.as_view(),                                  name='poi_create'),
]
