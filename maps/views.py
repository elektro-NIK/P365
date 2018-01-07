from django.shortcuts import render
from django.views import View


class MapView(View):
    @staticmethod
    def get(request):
        return render(request, 'map.html', {'title': 'Map'})


class TracksView(View):
    @staticmethod
    def get(request):
        return render(request, 'tracks.html', {'title': 'Tracks'})
