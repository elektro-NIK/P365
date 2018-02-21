from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from hashtag.models import TagModel
from .forms import TrackEditForm
from .models import TrackModel, POIModel


def get_track_time(track):
    timedelta = (track.finish_date - track.start_date)
    return {
        'days': timedelta.days,
        'hours': timedelta.seconds // 3600,
        'minutes': timedelta.seconds % 3600 // 60,
        'seconds': timedelta.seconds % 3600 % 60
    }


def calculate_length(line):
    line.srid = 4326
    line.transform(3035)
    return line.length / 1000


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


class GetTrackView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        track = TrackModel.objects.get(id=id)
        if track.public or track.user == user:
            data = serialize('geojson', [track], geometry_field='geom')
            return JsonResponse(data, safe=False)
        return HttpResponseForbidden()


class TrackChangeStatusView(View):
    @staticmethod
    def post(request, id):
        track = TrackModel.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
        if track.user == user:
            track.public = not track.public
            track.save()
            return JsonResponse({})
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
            return render(request, 'track_edit.html', {'title': track.name,
                                                       'form': form,
                                                       'track': track,
                                                       'time': get_track_time(track)})  # Fixme (track, times)
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
                track.geom = form.cleaned_data['geom']
                track.length = calculate_length(track.geom)
                track.speed = track.length / ((track.finish_date - track.start_date).total_seconds() // 3600)
                # Fixme!:
                track.altitude_gain = 0
                track.altitude_loss = 0
                track.activity = activity
                track.save()
                return HttpResponseRedirect(reverse('tracks'))
            return HttpResponseForbidden()
        track = TrackModel.objects.get(id=id)
        return render(request, 'track_edit.html', {'title': track.name,
                                                   'form': form,
                                                   'track': track,
                                                   'time': get_track_time(track)})  # Fixme (track, time)


class TrackView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        track = TrackModel.objects.get(id=id)
        if track.public or track.user == user:
            return render(request, 'track.html', {'title': track.name,
                                                  'track': track,
                                                  'time': get_track_time(track)})
        return HttpResponseForbidden()


class TrackDeleteView(View):
    @staticmethod
    def post(request, id):
        track = TrackModel.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
        if track.user == user and not track.public:
            track.is_active = False
            track.save()
            return JsonResponse({})
        return HttpResponseForbidden()
