from django.shortcuts import render
from django.views import View

from map.models import POIModel, RouteModel, TrackModel
from story.models import StoryModel
from tag.models import TagModel


class TagView(View):
    @staticmethod
    def get(request, slug):
        tag = TagModel.objects.get(slug=slug)
        pois = POIModel.objects.filter(tag=tag)
        routes = RouteModel.objects.filter(tag=tag)
        tracks = TrackModel.objects.filter(tag=tag)
        stories = StoryModel.objects.filter(tags=tag)
        return render(request, 'tag.html', {
            'title':  tag.name,
            'pois':   pois,
            'routes': routes,
            'tracks': tracks,
            'stories': stories,
        })
