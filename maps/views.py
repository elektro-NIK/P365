from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import TrackModel, POIModel


class MapView(View):
    @staticmethod
    def get(request):
        return render(request, 'map.html', {'title': 'Map'})


class TracksView(View):
    @staticmethod
    def get(request):
        return render(request, 'tracks.html', {'title': 'Tracks'})


class GetTracksView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True)
        data = serialize('geojson', tracks, geometry_field='geom')
        return JsonResponse(data, safe=False)


class GetPoisView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        pois = POIModel.objects.filter(user=user, is_active=True)
        data = serialize('geojson', pois, geometry_field='geom')
        return JsonResponse(data, safe=False)