from django.urls import path

from .views import ProfileView

app_name = 'user'

urlpatterns = [
    path('<slug:username>/', ProfileView.as_view(), name='profile'),
]
