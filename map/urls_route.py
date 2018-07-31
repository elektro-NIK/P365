from django.urls import path, include

from map.models import RouteModel
from map.views import RouteView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, RouteEditView

urlpatterns = [
    path('<int:id>/',               RouteView.as_view(),                    name='route'),
    path('<int:id>/edit/',          RouteEditView.as_view(),                name='route_edit'),
    path('<int:id>/', include([
        path('json_get/',           JSONFeatureView.as_view(),              name='json_route'),
        path('json_change_status/', JSONFeatureChangeStatusView.as_view(),  name='json_route_change_status'),
        path('json_delete/',        JSONFeatureDeleteView.as_view(),        name='json_route_delete'),
    ]), {'model': RouteModel}),
    path('json_ids/',               JSONFeatureIdsView.as_view(),   {'model': RouteModel},  name='json_route_ids'),
    path('json_get_all/',           JSONFeaturesView.as_view(),     {'model': RouteModel},  name='json_routes'),
    path('create/',                 RouteEditView.as_view(),                                name='route_create'),
]
