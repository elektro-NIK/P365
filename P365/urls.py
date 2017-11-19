"""P365 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from map_app import urls as map_urls
from djgeojson.views import GeoJSONLayerView
from map_app.models import POIModel
from map_app.views import UploadGPXView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^map/', include(map_urls)),
    url(r'^data.geojson/$', GeoJSONLayerView.as_view(model=POIModel, properties=('name', 'desc', 'user')), name='POI'),
    url(r'^upload/$', UploadGPXView.as_view(), name='upload'),
]
