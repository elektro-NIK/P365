from django.shortcuts import render
from django import views
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import UploadGPXForm
from .models import TrackModel


class UploadGPXView(views.View):
    def get(self, request):
        form = UploadGPXForm()
        return render(request, 'uploadGPX.html', {'form': form})

    def post(self, request):
        form = UploadGPXForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['gpx_file'].read().decode()
            import gpxpy
            gpx = gpxpy.parse(file)
            import sys
            print(f'Waypoints: {len(gpx.waypoints)}', file=sys.stderr)
            print(f'Tracks: {len(gpx.tracks)}', file=sys.stderr)
            print(f'Routes: {len(gpx.routes)}', file=sys.stderr)
            # TrackModel(name='123', desc='12345', user=User.objects.get(username='elektronik'), geom=track).save()
        return HttpResponseRedirect(reverse('upload'))
