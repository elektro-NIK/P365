from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import MapView

urlpatterns = [
    path('', login_required(MapView.as_view()), name='map'),
]
