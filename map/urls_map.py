from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import MapView

urlpatterns = [
    url(r'^$', login_required(MapView.as_view()), name='map'),
]
