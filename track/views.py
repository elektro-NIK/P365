from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from hashtag.models import TagModel
from track.forms import TrackEditForm
from track.models import TrackModel


def calculate_length(line):
    line.srid = 4326
    line.transform(3035)
    return line.length / 1000


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
        tracks = TrackModel.objects.filter(user=user, is_active=True).order_by('-start_date')
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
                                                       'time': (track.finish_date - track.start_date)})
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
                # track.speed = track.length / ((track.finish_date - track.start_date).total_seconds() // 3600)
                # Fix me: altitude
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
                                                   'time': (track.finish_date - track.start_date)})


class TrackView(View):
    @staticmethod
    def get(request, id):
        user = User.objects.get(username=request.user.username)
        track = TrackModel.objects.get(id=id)
        if track.public or track.user == user:
            return render(request, 'track.html', {'title': track.name,
                                                  'track': track,
                                                  'time': (track.finish_date - track.start_date)})
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


class TracksView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True).order_by('-start_date')
        return render(request, 'tracks.html', {'title': 'Tracks', 'tracks': tracks, 'active': 'tracks'})


class GetTracksView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        tracks = TrackModel.objects.filter(user=user, is_active=True)
        data = serialize('geojson', tracks, geometry_field='geom')
        return JsonResponse(data, safe=False)
