import json

from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponseForbidden, JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from story.models import StoryModel
from .forms import POIForm, RouteForm, TrackForm
from .models import TrackModel, POIModel, RouteModel


@method_decorator(login_required, name='dispatch')
class MapView(View):
    @staticmethod
    def get(request):
        return render(request, 'map.html', {'title': 'Map', 'active': 'map'})


@method_decorator(login_required, name='dispatch')
class POIView(View):
    @staticmethod
    def get(request, id):
        poi = get_object_or_404(POIModel, id=id)
        if (poi.user == request.user or poi.public) and poi.is_active:
            return render(request, 'poi.html', {'title': poi.name, 'poi': poi})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class RouteView(View):
    @staticmethod
    def get(request, id):
        route = get_object_or_404(RouteModel, id=id)
        if (route.user == request.user or route.public) and route.is_active:
            return render(request, 'route.html', {'title': route.name, 'route': route})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class TrackView(View):
    @staticmethod
    def get(request, id):
        track = get_object_or_404(TrackModel, id=id)
        if (track.user == request.user or track.public) and track.is_active:
            return render(request, 'track.html', {'title': track.name, 'track': track})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class POIEditView(View):
    @staticmethod
    def get(request, id=None):
        poi = get_object_or_404(POIModel, id=id) if id else None
        if poi and poi.user != request.user and poi.is_active:
            return HttpResponseForbidden()
        form = POIForm(instance=poi)
        return render(request, 'editor.html', {'title': poi.name if poi else 'New POI', 'form': form})

    @staticmethod
    def post(request, id=None):
        form = POIForm(request.POST)
        if form.is_valid():
            if id:                                                  # update POI
                poi = get_object_or_404(POIModel, id=id)
                poi.name = form.cleaned_data['name']
                poi.description = form.cleaned_data['description']
                poi.geom = form.cleaned_data['geom']
                poi.tags.set(*form.cleaned_data['tags'])
                poi.public = form.cleaned_data['public']
            else:                                                   # create POI
                poi = form.save(commit=False)
                poi.user = request.user
            poi.save()
            form.save_m2m() if not id else None
            return HttpResponseRedirect(reverse('table:view'))
        return render(request, 'editor.html', {'title': form['name'].value(), 'form': form})


@method_decorator(login_required, name='dispatch')
class RouteEditView(View):
    @staticmethod
    def get(request, id=None):
        route = get_object_or_404(RouteModel, id=id) if id else None
        if route and route.user != request.user and route.is_active:
            return HttpResponseForbidden()
        form = RouteForm(instance=route)
        return render(request, 'editor.html', {'title': route.name if route else 'New route', 'form': form})

    @staticmethod
    def post(request, id=None):
        form = RouteForm(request.POST)
        if form.is_valid():
            if id:                                                  # update route
                route = get_object_or_404(RouteModel, id=id)
                route.name = form.cleaned_data['name']
                route.description = form.cleaned_data['description']
                route.geom = form.cleaned_data['geom']
                route.tags.set(*form.cleaned_data['tags'])
                route.public = form.cleaned_data['public']
            else:
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
            #
            route.save()
            form.save_m2m() if not id else None
            return HttpResponseRedirect(reverse('table:view'))
        return render(request, 'editor.html', {'title': form['name'].value(), 'form': form})


@method_decorator(login_required, name='dispatch')
class TrackEditView(View):
    @staticmethod
    def get(request, id=None):
        track = get_object_or_404(TrackModel, id=id) if id else None
        if not track or track.user != request.user and track.is_active:
            return HttpResponseForbidden()
        form = TrackForm(instance=track)
        return render(request, 'editor.html', {'title': track.name, 'form': form})

    @staticmethod
    def post(request, id=None):
        form = TrackForm(request.POST)
        if form.is_valid():
            track = get_object_or_404(TrackModel, id=id)
            track.name = form.cleaned_data['name']
            track.description = form.cleaned_data['description']
            track.tags.set(*form.cleaned_data['tags'])
            track.public = form.cleaned_data['public']
            track.save()
            return HttpResponseRedirect(reverse('table:view'))
        return render(request, 'editor.html', {'title': form['name'].value(), 'form': form})


@method_decorator(login_required, name='dispatch')
class JSONFeatureIdsView(View):
    @staticmethod
    def get(request, model):
        objs = model.objects.filter(user=request.user, is_active=True)
        return JsonResponse([obj.id for obj in objs], safe=False)


@method_decorator(login_required, name='dispatch')
class JSONFeatureView(View):
    @staticmethod
    def get(request, id, model):
        obj = get_object_or_404(model, id=id)
        if (obj.user == request.user or obj.public) and obj.is_active:
            data = serialize('geojson', [obj], geometry_field='geom')
            return JsonResponse(data, safe=False)
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class JSONFeaturesView(View):
    @staticmethod
    def get(request, model):
        objs = model.objects.filter(user=request.user, is_active=True)
        data = serialize('geojson', objs, geometry_field='geom')
        return JsonResponse(data, safe=False)


@method_decorator(login_required, name='dispatch')
class JSONFeatureChangeStatusView(View):
    @staticmethod
    def post(request, id, model):
        obj = get_object_or_404(model, id=id)
        if obj.user == request.user and obj.is_active:
            obj.public = not obj.public
            obj.save()
            return JsonResponse({'Status': 'OK'})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class JSONFeatureDeleteView(View):
    @staticmethod
    def post(request, id, model):
        obj = get_object_or_404(model, id=id)
        if obj.user == request.user and not obj.public and obj.is_active:
            obj.is_active = False
            obj.save()
            return JsonResponse({'Status': 'OK'})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class JSONFeatureHasStory(View):
    @staticmethod
    def get(request, id, model):
        obj = get_object_or_404(model, id=id)
        if obj.user == request.user and obj.is_active:
            return HttpResponse(json.dumps({
                'result': bool(StoryModel.objects.filter(track=obj))
            }), content_type='application/json')
        return HttpResponseForbidden()
