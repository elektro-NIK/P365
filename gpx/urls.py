from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import GPXImportView

urlpatterns = [
    url(r'^import/$', login_required(GPXImportView.as_view()), name='import_gpx'),
]
