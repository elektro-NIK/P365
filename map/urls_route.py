from django.urls import path, include
from django.contrib.auth.decorators import login_required

from map.models import RouteModel
from map.views import RouteView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, RouteEditView

urlpatterns = [
    path('<int:id>/',              login_required(RouteView.as_view()),                   name='route'),
    path('<int:id>/edit/',          login_required(RouteEditView.as_view()),               name='route_edit'),
    path('<int:id>/', include([
        path('json_get/',           login_required(JSONFeatureView.as_view()),             name='json_route'),
        path('json_change_status/', login_required(JSONFeatureChangeStatusView.as_view()), name='json_route_change_status'),
        path('json_delete/',        login_required(JSONFeatureDeleteView.as_view()),       name='json_route_delete'),
    ]), {'model': RouteModel}),
    path('json_ids/',     login_required(JSONFeatureIdsView.as_view()), {'model': RouteModel}, name='json_route_ids'),
    path('json_get_all/', login_required(JSONFeaturesView.as_view()),   {'model': RouteModel}, name='json_routes'),
    path('create/',       login_required(RouteEditView.as_view()),                             name='route_create'),
]
