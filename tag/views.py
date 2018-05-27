from django.shortcuts import render
from django.views import View

from map.models import POIModel, RouteModel, TrackModel
from story.models import StoryModel


class TagView(View):
    @staticmethod
    def get(request, slug):
        pois = POIModel.objects.filter(tag=slug)
        routes = RouteModel.objects.filter(tag=slug)
        tracks = TrackModel.objects.filter(tag=slug)
        stories = StoryModel.objects.filter(tags=slug)
        return render(request, 'tag.html', {
            'title':  slug,
            'pois':   pois,
            'routes': routes,
            'tracks': tracks,
            'stories': stories,
        })
