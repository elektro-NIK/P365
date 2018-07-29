from django.urls import path
from django.contrib.auth.decorators import login_required

from map.models import TrackModel, RouteModel, POIModel
from .views import TableView, UpdateTableView

urlpatterns = [
    path('',                login_required(TableView.as_view()), name='table'),
    path('update_tracks/',  login_required(UpdateTableView.as_view()), {'model': TrackModel, 'template': 'partials/_tracks-table.html', 'temp_var_name': 'tracks'}, name='update_tracks_table'),
    path('update_routes/',  login_required(UpdateTableView.as_view()), {'model': RouteModel, 'template': 'partials/_routes-table.html', 'temp_var_name': 'routes'}, name='update_routes_table'),
    path('update_pois/',    login_required(UpdateTableView.as_view()), {'model': POIModel,   'template': 'partials/_pois-table.html',   'temp_var_name': 'pois'},   name='update_pois_table'),
]
