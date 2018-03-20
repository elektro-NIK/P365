from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, LineString
from django.core.serializers import serialize
from django.http import HttpResponseForbidden, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from google_api.elevation import get_elevation
from hashtag.models import TagModel

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
        user = User.objects.get(username=request.user.username)
        if id:
            poi = POIModel.objects.get(id=id)
            if poi.user != user:
                return HttpResponseForbidden()
            form = POIForm(instance=poi, initial={'tag': poi.tag})
            return render(request, 'editor.html', {'title': poi.name, 'form': form})
        else:
            form = POIForm()
            return render(request, 'editor.html', {'title': 'New POI', 'form': form})

    @staticmethod
    def post(request, id=None):
        form = POIForm(request.POST)
        title = form['name'].value()
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            user = User.objects.get(username=request.user.username)
            tag, _ = TagModel.objects.get_or_create(name=form.cleaned_data['tag'])
            # Add altitude data
            geom = Point(*get_elevation(form.cleaned_data['geom']))
            if id:
                poi = POIModel.objects.get(id=id)
                if poi.user == user:
                    poi.name, poi.description, poi.tag, poi.geom = name, description, tag, geom
                    poi.save()
                else:
                    return HttpResponseForbidden()
            else:
                POIModel(name=name, description=description, user=user, tag=tag, geom=geom).save()
            return HttpResponseRedirect(reverse('table'))
        else:
            return render(request, 'editor.html', {'title': title, 'form': form})


class RouteEditView(View):
    @staticmethod
    def get(request, id=None):
        user = User.objects.get(username=request.user.username)
        if id:
            route = RouteModel.objects.get(id=id)
            if route.user != user:
                return HttpResponseForbidden()
            form = RouteForm(instance=route, initial={'tag': route.tag})
            return render(request, 'editor.html', {'title': route.name, 'form': form})
        else:
            form = RouteForm()
            return render(request, 'editor.html', {'title': 'New route', 'form': form})

    @staticmethod
    def post(request, id=None):
        form = RouteForm(request.POST)
        title = form['name'].value()
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            user = User.objects.get(username=request.user.username)
            tag, _ = TagModel.objects.get_or_create(name=form.cleaned_data['tag'])
            # Add altitude data
            geom = LineString(*get_elevation(form.cleaned_data['geom']))
            # Calculate min, max, loss, gain altitude
            alt = [i[2] for i in geom]
            loss, gain = 0, 0
            last_alt = geom[0][2]
            for point in geom:
                if last_alt > point[2]:
                    loss += last_alt - point[2]
                elif last_alt < point[2]:
                    gain += point[2] - last_alt
                last_alt = point[2]
            if id:
                route = RouteModel.objects.get(id=id)
                if route.user == user:
                    route.name, route.description, route.tag, route.geom = name, description, tag, geom
                    route.save()
                else:
                    return HttpResponseForbidden()
            else:
                RouteModel(
                    name=name,
                    description=description,
                    user=user,
                    tag=tag,
                    altitude_max=max(alt),
                    altitude_min=min(alt),
                    altitude_gain=gain,
                    altitude_loss=loss,
                    geom=geom
                ).save()
            return HttpResponseRedirect(reverse('table'))
        else:
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
