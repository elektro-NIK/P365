from django.db.models import Q
from django.shortcuts import render
from django.views import View
from taggit.models import Tag

from map.models import POIModel, RouteModel, TrackModel
from story.models import StoryModel


class TagCloudView(View):
    @staticmethod
    def get(request):
        return render(request, 'tag-cloud.html', {
            'title': 'Tagcloud',
        })


class TagView(View):
    @staticmethod
    def get(request, tagslug):
        tag = Tag.objects.get(slug=tagslug)
        stories = StoryModel.objects.filter(
            Q(tags=tag), Q(is_active=True)
        ).order_by('-created')
        if request.user.is_anonymous:
            pois = POIModel.objects.filter(tags=tag, is_active=True, public=True).order_by('-created')
            routes = RouteModel.objects.filter(tags=tag, is_active=True, public=True).order_by('-created')
            tracks = TrackModel.objects.filter(tags=tag, is_active=True, public=True).order_by('-start_date')
        else:
            pois = POIModel.objects.filter(
                Q(tags=tag), Q(is_active=True), Q(user=request.user) | Q(public=True)
            ).order_by('-created')
            routes = RouteModel.objects.filter(
                Q(tags=tag), Q(is_active=True), Q(user=request.user) | Q(public=True)
            ).order_by('-created')
            tracks = TrackModel.objects.filter(
                Q(tags=tag), Q(is_active=True), Q(user=request.user) | Q(public=True)
            ).order_by('-start_date')
        return render(request, 'tag.html', {
            'title': '#' + tagslug,
            'tag': tag,
            'pois': pois,
            'routes': routes,
            'tracks': tracks,
            'stories': stories,
        })
