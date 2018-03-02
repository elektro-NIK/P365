import mimetypes
from os.path import splitext

import gpxpy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from hashtag.models import TagModel
from track.models import TrackModel


class GPXImportView(View):
    @staticmethod
    def get(_):
        return HttpResponseRedirect(reverse('tracks'))

    def post(self, request):
        file = request.FILES['gpx_file']
        ext = splitext(file.name)[1][1:].lower()
        mime = mimetypes.guess_type(file.name)[0]
        size = len(file)
        if ext == 'gpx' and mime is None and size < 25*1024*1024:
            res = self.parse_gpx(file.read().decode())
            user = User.objects.get(username=request.user.username)
            for key, value in res.items():
                TrackModel(name=key, user=user,
                           start_date=value['start_date'], finish_date=value['finish_date'],
                           length=value['length'], speed=value['speed'],
                           altitude_gain=value['altitude_gain'], altitude_loss=value['altitude_loss'],
                           activity=TagModel.objects.get(name='None'), geom=value['geom']).save()
            return render(request, 'import.html', {'title': 'Import GPX', 'gpx': None})
        else:
            return render(request, 'import.html', {'title': 'Import GPX'})

    @staticmethod
    def parse_gpx(file):
        gpx = gpxpy.parse(file)
        res = dict()
        for track in gpx.tracks:
            # print(track.name)
            # print(track.get_duration())
            name = track.name
            geom = 'MULTILINESTRING Z ('
            for segment in track.segments:
                geom += '('
                for point in segment.points:
                    geom += '{} {} {}, '.format(point.longitude, point.latitude, point.elevation)
                geom = geom[:-2] + '), '
            geom = geom[:-2] + ')'
            res[name] = {
                'start_date': track.get_time_bounds().start_time,
                'finish_date': track.get_time_bounds().end_time,
                'length': track.length_3d() / 1000,
                'speed':  track.length_3d() / 1000 / (track.get_duration() / 3600),
                'altitude_gain': track.get_uphill_downhill().uphill,
                'altitude_loss': track.get_uphill_downhill().downhill,
                'geom': geom
            }
        return res
