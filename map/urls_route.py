from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from map.models import RouteModel
from map.views import RouteView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, RouteEditView

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$',
        login_required(RouteView.as_view()),                                          name='route'),
    url(r'^json_ids/$',
        login_required(JSONFeatureIdsView.as_view()),          {'model': RouteModel}, name='json_route_ids'),
    url(r'^(?P<id>[0-9]+)/json_get/$',
        login_required(JSONFeatureView.as_view()),             {'model': RouteModel}, name='json_route'),
    url(r'^json_get_all/$',
        login_required(JSONFeaturesView.as_view()),            {'model': RouteModel}, name='json_routes'),
    url(r'^(?P<id>[0-9]+)/json_change_status/$',
        login_required(JSONFeatureChangeStatusView.as_view()), {'model': RouteModel}, name='json_route_change_status'),
    url(r'^(?P<id>[0-9]+)/json_delete/$',
        login_required(JSONFeatureDeleteView.as_view()),       {'model': RouteModel}, name='json_route_delete'),
    url(r'^create/$',
        login_required(RouteEditView.as_view()),                                      name='route_create'),
    url(r'^(?P<id>[0-9]+)/edit/$',
        login_required(RouteEditView.as_view()),                                      name='route_edit'),
]
