from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from hashtag.models import TagModel
from .forms import TrackEditForm
from .models import TrackModel, POIModel


class MapView(View):
    @staticmethod
    def get(request):
        return render(request, 'map.html', {'title': 'Map', 'active': 'map'})


class TracksView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True)
        return render(request, 'tracks.html', {'title': 'Tracks', 'tracks': tracks, 'active': 'tracks'})


class GetTracksView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True)
        data = serialize('geojson', tracks, geometry_field='geom')
        return JsonResponse(data, safe=False)


class GetPoisView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        pois = POIModel.objects.filter(user=user, is_active=True)
        data = serialize('geojson', pois, geometry_field='geom')
        return JsonResponse(data, safe=False)


class TrackChangeStatusView(View):
    @staticmethod
    def post(request, id):
        track = TrackModel.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
        if track.user == user:
            track.public = not track.public
            track.save()
            return JsonResponse({})
        else:
            return HttpResponseForbidden()


class GetTracksTableView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True)
        return render(request, 'partials/_tracks-table.html', {'tracks': tracks})


class TrackEditView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        track = TrackModel.objects.get(id=id)
        if track.is_active and track.user == user:
            form = TrackEditForm(initial={
                'name': track.name,
                'description': track.description,
                'activity': track.activity,
                'geom': track.geom
            })
            timedelta = (track.finish_date - track.start_date)
            time = {
                'days': timedelta.days,
                'hours': timedelta.seconds // 3600,
                'minutes': timedelta.seconds % 3600 // 60,
                'seconds': timedelta.seconds % 3600 % 60
            }
            return render(request, 'track_edit.html',
                          {'title': track.name, 'form': form, 'track': track, 'time': time})  # Fixme (track, times)
        else:
            return HttpResponseForbidden()

    @staticmethod
    def post(request, id):
        form = TrackEditForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            track = TrackModel.objects.get(id=id)
            if track.user == user:
                from sys import stderr
                print(form.cleaned_data['activity'], file=stderr)
                activity = TagModel.objects.get(name=form.cleaned_data['activity'])
                track.name = form.cleaned_data['name']
                track.description = form.cleaned_data['description']
                # track.length = calculate()
                # track.speed = track.length / time?
                # track.altitude_gain = calculate()
                # track.altitude_loss = calculate()
                track.activity = activity
                track.geom = form.cleaned_data['geom']
                track.save()
                return HttpResponseRedirect(reverse('tracks'))
            return HttpResponseForbidden()
        track = TrackModel.objects.get(id=id)
        timedelta = (track.finish_date - track.start_date)
        time = {
            'days': timedelta.days,
            'hours': timedelta.seconds // 3600,
            'minutes': timedelta.seconds % 3600 // 60,
            'seconds': timedelta.seconds % 3600 % 60
        }
        return render(request, 'track_edit.html',
                      {'title': track.name, 'form': form, 'track': track, 'time': time})  # Fixme (track, time)
