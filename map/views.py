from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views import View

from map.models import TrackModel, POIModel, RouteModel


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


# def calculate_length(line):
#     line.srid = 4326
#     line.transform(3035)
#     return line.length / 1000
#
#
# class TrackEditView(View):
#     @staticmethod
#     def get(request, id):
#         user = User.objects.get(username=request.user.username)
#         track = TrackModel.objects.get(id=id)
#         if track.is_active and track.user == user:
#             form = TrackEditForm(initial={
#                 'name': track.name,
#                 'description': track.description,
#                 'activity': track.activity,
#                 'geom': track.geom
#             })
#             return render(request, 'track_edit.html', {'title': track.name,
#                                                        'form': form,
#                                                        'feature': track,
#                                                        'time': (track.finish_date - track.start_date)})
#         return HttpResponseForbidden()
#
#     @staticmethod
#     def post(request, id):
#         form = TrackEditForm(request.POST)
#         if form.is_valid():
#             user = User.objects.get(username=request.user.username)
#             track = TrackModel.objects.get(id=id)
#             if track.user == user:
#                 from sys import stderr
#                 print(form.cleaned_data['activity'], file=stderr)
#                 activity = TagModel.objects.get(name=form.cleaned_data['activity'])
#                 track.name = form.cleaned_data['name']
#                 track.description = form.cleaned_data['description']
#                 track.geom = form.cleaned_data['geom']
#                 track.length = calculate_length(track.geom)
# feature.speed = feature.length / ((feature.finish_date - feature.start_date).total_seconds() // 3600)
#                 # Fix me: altitude
#                 track.altitude_gain = 0
#                 track.altitude_loss = 0
#                 track.activity = activity
#                 track.save()
#                 return HttpResponseRedirect(reverse('tracks'))
#             return HttpResponseForbidden()
#         track = TrackModel.objects.get(id=id)
#         return render(request, 'track_edit.html', {'title': track.name,
#                                                    'form': form,
#                                                    'feature': track,
#                                                    'time': (track.finish_date - track.start_date)})
