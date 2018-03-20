import mimetypes
from os.path import splitext

from django.contrib.auth.models import User
from django.contrib.gis.geos import LineString, Point
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from google_api.elevation import get_elevation
from gpx.parser.GPXParser import GPXParser
from map.models import TrackModel, RouteModel, POIModel


class TableView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        pois = POIModel.objects.filter(user=user, is_active=True).order_by('-created')
        routes = RouteModel.objects.filter(user=user, is_active=True).order_by('-created')
        tracks = TrackModel.objects.filter(user=user, is_active=True).order_by('-created')
        return render(request, 'table.html', {
            'title':  'Table',
            'active': 'table',
            'pois':   pois,
            'routes': routes,
            'tracks': tracks,
        })

    @staticmethod
    def post(request):
        file = request.FILES['gpx_file']
        ext, mime, size = splitext(file.name)[1][1:].lower(), mimetypes.guess_type(file.name)[0], len(file)
        if ext == 'gpx' and mime is None and size < 25 * 1024 * 1024:
            user = User.objects.get(username=request.user.username)
            parser = GPXParser(file.read().decode())
            tracks, routes, pois = parser.tracks(), parser.routes(), parser.pois()
            for key, value in tracks.items():
                TrackModel(
                    name=key,
                    user=user,
                    start_date=value['start_date'],
                    finish_date=value['finish_date'],
                    length=value['length'],
                    speed=value['speed'],
                    speed_max=value['speed_max'],
                    altitude_gain=value['altitude_gain'],
                    altitude_loss=value['altitude_loss'],
                    altitude_max=value['altitude_max'],
                    altitude_min=value['altitude_min'],
                    geom=value['geom']
                ).save()
            for key, value in routes.items():
                RouteModel(
                    name=key,
                    description=value['description'],
                    user=user,
                    length=value['length'],
                    geom=LineString(*get_elevation(value['geom'])),
                ).save()
            for key, value in pois.items():
                POIModel(
                    name=key,
                    description=value['description'],
                    user=user,
                    geom=Point(*get_elevation(value['geom'])),
                ).save()
        return HttpResponseRedirect(reverse('table'))


class UpdateTablesView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        pois = POIModel.objects.filter(user=user, is_active=True).order_by('-created')
        routes = RouteModel.objects.filter(user=user, is_active=True).order_by('-created')
        tracks = TrackModel.objects.filter(user=user, is_active=True).order_by('-start_date')
        return render(request, '_tables.html', {
            'title': 'Table',
            'active': 'table',
            'pois': pois,
            'routes': routes,
            'tracks': tracks,
        })


class UpdateTableView(View):
    @staticmethod
    def get(request, model, template, temp_var_name):
        user = User.objects.get(username=request.user.username)
        objs = model.objects.filter(user=user, is_active=True).order_by('-created')
        return render(request, template, {temp_var_name: objs})
