from django.urls import path

from table.views import TableView
from .views import ProfileView

app_name = 'user'

urlpatterns = [
    path('<slug:username>/',        ProfileView.as_view(),  name='profile'),
    path('<slug:username>/table/',  TableView.as_view(),    name='table')
]
