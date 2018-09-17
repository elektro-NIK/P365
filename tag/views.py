from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from map.models import POIModel, RouteModel, TrackModel


class TagCloudView(View):
    @staticmethod
    def get(request):
        return render(request, 'tag-cloud.html', {
            'title': 'Tagcloud',
        })


class TagView(View):
    @staticmethod
    def get(request, tagslug):
        if request.user.is_anonymous:
            pois = POIModel.objects.filter(
                Q(tags__slug=tagslug), Q(is_active=True), Q(public=True)
            ).order_by('-created')
            routes = RouteModel.objects.filter(
                Q(tags__slug=tagslug), Q(is_active=True), Q(public=True)
            ).order_by('-created')
            tracks = TrackModel.objects.filter(
                Q(tags__slug=tagslug), Q(is_active=True), Q(public=True)
            ).order_by('-start_date')
        else:
            pois = POIModel.objects.filter(
                Q(tags__slug=tagslug), Q(is_active=True), Q(user=request.user) | Q(public=True)
            ).order_by('-created')
            routes = RouteModel.objects.filter(
                Q(tags__slug=tagslug), Q(is_active=True), Q(user=request.user) | Q(public=True)
            ).order_by('-created')
            tracks = TrackModel.objects.filter(
                Q(tags__slug=tagslug), Q(is_active=True), Q(user=request.user) | Q(public=True)
            ).order_by('-start_date')
        return render(request, 'tag.html', {
            'title': '#' + tagslug,
            'pois': pois,
            'routes': routes,
            'tracks': tracks,
        })
