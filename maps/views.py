from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views import View

from .models import TrackModel, POIModel


class MapView(View):
    @staticmethod
    def get(request):
        return render(request, 'map.html', {'title': 'Map', 'active': 'map'})


class TracksView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True)
        return render(request, 'tracks.html', {'title': 'Tracks', 'tracks': tracks, 'active': 'tracks'})


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


class TrackChangeStatusView(View):
    @staticmethod
    def post(request, id):
        track = TrackModel.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
        if track.user == user:
            track.public = not track.public
            track.save()
            return JsonResponse({})
        else:
            return HttpResponseForbidden()
