from django.urls import path

from .views import TagCloudView, TagView

app_name = 'tag'

urlpatterns = [
    path('',                TagCloudView.as_view(), name='tag_cloud'),
    path('<slug:tagslug>/', TagView.as_view(),      name='tag'),
]