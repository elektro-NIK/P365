import tagulous.views
from django.conf.urls import url

from .views import TagView
from .models import TagModel

urlpatterns = [
    url(r'^autocomplete/$', tagulous.views.autocomplete, {'tag_model': TagModel},   name='tag_autocomplete'),
    url(r'^@(?P<slug>[\w-]+)/$', TagView.as_view(),                                 name='tag_url'),
]
