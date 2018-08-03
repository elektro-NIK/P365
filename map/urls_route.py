from django.urls import path, include, register_converter

from P365.converters import UintWithoutZero
from map.models import RouteModel
from map.views import RouteView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, RouteEditView

app_name = 'route'

register_converter(UintWithoutZero, 'uint_id')

urlpatterns = [
    path('<uint_id:id>/',               RouteView.as_view(),                    name='view'),
    path('<uint_id:id>/edit/',          RouteEditView.as_view(),                name='edit'),
    path('<uint_id:id>/', include([
        path('json_get/',           JSONFeatureView.as_view(),              name='json'),
        path('json_change_status/', JSONFeatureChangeStatusView.as_view(),  name='json_change_status'),
        path('json_delete/',        JSONFeatureDeleteView.as_view(),        name='json_delete'),
    ]), {'model': RouteModel}),
    path('json_ids/',               JSONFeatureIdsView.as_view(),   {'model': RouteModel},  name='json_ids'),
    path('json_get_all/',           JSONFeaturesView.as_view(),     {'model': RouteModel},  name='json_all'),
    path('create/',                 RouteEditView.as_view(),                                name='create'),
]
