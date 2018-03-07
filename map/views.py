from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views import View

from poi.models import POIModel
from track.models import TrackModel


class MapView(View):
    @staticmethod
    def get(request):
        return render(request, 'map.html', {'title': 'Map', 'active': 'map'})


class GetPoisView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        pois = POIModel.objects.filter(user=user, is_active=True)
        data = serialize('geojson', pois, geometry_field='geom')
        return JsonResponse(data, safe=False)


class TracksNumsView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True)
        tracks = [track.id for track in tracks]
        from sys import stderr
        print(tracks, file=stderr)
        return JsonResponse(tracks, safe=False)


class GetTrackView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        track = TrackModel.objects.get(id=id)
        if track.is_active and track.user == user:
            data = serialize('geojson', [track], geometry_field='geom')
            return JsonResponse(data, safe=False)
        return HttpResponseForbidden()