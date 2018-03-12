from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from map.models import POIModel
from map.views import POIView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$',
        login_required(POIView.as_view()),                                          name='poi'),
    url(r'^json_ids/',
        login_required(JSONFeatureIdsView.as_view()),          {'model': POIModel}, name='json_poi_ids'),
    url(r'^(?P<id>[0-9]+)/json_get/$',
        login_required(JSONFeatureView.as_view()),             {'model': POIModel}, name='json_poi'),
    url(r'^json_get_all/$',
        login_required(JSONFeaturesView.as_view()),            {'model': POIModel}, name='json_pois'),
    url(r'^(?P<id>[0-9]+)/json_change_status/$',
        login_required(JSONFeatureChangeStatusView.as_view()), {'model': POIModel}, name='json_poi_change_status'),
    url(r'^(?P<id>[0-9]+)/json_delete/$',
        login_required(JSONFeatureDeleteView.as_view()),       {'model': POIModel}, name='json_poi_delete'),
]
