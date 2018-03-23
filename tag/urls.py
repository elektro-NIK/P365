import tagulous.views
from django.conf.urls import url

from .models import TagModel

urlpatterns = [
    url(r'^autocomplete/$', tagulous.views.autocomplete, {'tag_model': TagModel}, name='tag_autocomplete'),
]
