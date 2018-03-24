from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, LineString
from django.core.serializers import serialize
from django.http import HttpResponseForbidden, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from google_api.elevation import get_elevation
from tag.models import TagModel

from .forms import POIForm, RouteForm
from .models import TrackModel, POIModel, RouteModel


class MapView(View):
    @staticmethod
    def get(request):
        return render(request, 'map.html', {'title': 'Map', 'active': 'map'})


class POIView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        poi = POIModel.objects.get(id=id)
        if poi.public or poi.user == user:
            return render(request, 'poi.html', {'title': poi.name, 'poi': poi})
        return HttpResponseForbidden()


class RouteView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        route = RouteModel.objects.get(id=id)
        if route.public or route.user == user:
            return render(request, 'route.html', {'title': route.name, 'route': route})
        return HttpResponseForbidden()


class TrackView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        track = TrackModel.objects.get(id=id)
        if track.public or track.user == user:
            return render(request, 'track.html', {'title': track.name, 'track': track})
        return HttpResponseForbidden()


class POIEditView(View):
    @staticmethod
    def get(request, id=None):
        if id:
            poi = POIModel.objects.get(id=id)
            if poi.user == request.user:
                form = POIForm(instance=poi)
                return render(request, 'editor.html', {'title': poi.name, 'form': form})
            return HttpResponseForbidden()
        form = POIForm()
        return render(request, 'editor.html', {'title': 'New POI', 'form': form})

    @staticmethod
    def post(request, id=None):
        form = POIForm(request.POST)
        if form.is_valid():
            poi = form.save(commit=False)
            poi.user = request.user
            poi.save()
            return HttpResponseRedirect(reverse('table'))
        return render(request, 'editor.html', {'title': form['name'].value(), 'form': form})


class RouteEditView(View):
    @staticmethod
    def get(request, id=None):
        user = User.objects.get(username=request.user.username)
        if id:
            route = RouteModel.objects.get(id=id)
            if route.user == request.user:
                form = RouteForm(instance=route, initial={'tag': route.tag})
                return render(request, 'editor.html', {'title': route.name, 'form': form})
            return HttpResponseForbidden()
        form = RouteForm()
        return render(request, 'editor.html', {'title': 'New route', 'form': form})

    @staticmethod
    def post(request, id=None):
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            route.user = request.user
            route.length = form.cleaned_data['geom'].length * 100
            # Calculate min, max, loss, gain altitude
            alts = [i[2] for i in form.cleaned_data['geom']]
            diffs = [alts[i] - alts[i-1] for i in range(1, len(alts))]
            gain, loss = [i for i in diffs if i > 0], [-i for i in diffs if i < 0]
            #
            route.altitude_max = max(alts)
            route.altitude_min = min(alts)
            route.altitude_gain = sum(gain)
            route.altitude_loss = sum(loss)
            route.save()
            return HttpResponseRedirect(reverse('table'))
        else:
            title = form['name'].value()
            return render(request, 'editor.html', {'title': title, 'form': form})


class JSONFeatureIdsView(View):
    @staticmethod
    def get(request, model):
        user = User.objects.get(username=request.user.username)
        objs = model.objects.filter(user=user, is_active=True)
        ids = [obj.id for obj in objs]
        return JsonResponse(ids, safe=False)


class JSONFeatureView(View):
    @staticmethod
    def get(request, id, model):
        user = User.objects.get(username=request.user.username)
        obj = model.objects.get(id=id)
        if obj.public or obj.user == user:
            data = serialize('geojson', [obj], geometry_field='geom')
            return JsonResponse(data, safe=False)
        return HttpResponseForbidden()


class JSONFeaturesView(View):
    @staticmethod
    def get(request, model):
        user = User.objects.get(username=request.user.username)
        objs = model.objects.filter(user=user, is_active=True)
        data = serialize('geojson', objs, geometry_field='geom')
        return JsonResponse(data, safe=False)


class JSONFeatureChangeStatusView(View):
    @staticmethod
    def post(request, id, model):
        user = User.objects.get(username=request.user.username)
        obj = model.objects.get(id=id)
        if obj.user == user:
            obj.public = not obj.public
            obj.save()
            return JsonResponse({})
        return HttpResponseForbidden()


class JSONFeatureDeleteView(View):
    @staticmethod
    def post(request, id, model):
        user = User.objects.get(username=request.user.username)
        obj = model.objects.get(id=id)
        if obj.user == user and not obj.public:
            obj.is_active = False
            obj.save()
            return JsonResponse({})
        return HttpResponseForbidden()
