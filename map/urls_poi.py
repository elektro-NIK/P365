from django.urls import path, include
from django.contrib.auth.decorators import login_required

from map.models import POIModel
from map.views import POIView, JSONFeatureIdsView, JSONFeatureView, JSONFeaturesView, JSONFeatureChangeStatusView, \
    JSONFeatureDeleteView, POIEditView

urlpatterns = [
    path('<int:id>/',               login_required(POIView.as_view()),                      name='poi'),
    path('<int:id>/edit/',          login_required(POIEditView.as_view()),                  name='poi_edit'),
    path('<int:id>/', include([
        path('json_get/',           login_required(JSONFeatureView.as_view()),              name='json_poi'),
        path('json_change_status/', login_required(JSONFeatureChangeStatusView.as_view()),  name='json_poi_change_status'),
        path('json_delete/',        login_required(JSONFeatureDeleteView.as_view()),        name='json_poi_delete'),
    ]), {'model': POIModel}),
    path('json_ids/',       login_required(JSONFeatureIdsView.as_view()),   {'model': POIModel},    name='json_poi_ids'),
    path('json_get_all/',   login_required(JSONFeaturesView.as_view()),     {'model': POIModel},    name='json_pois'),
    path('create/',         login_required(POIEditView.as_view()),                                  name='poi_create'),
]
