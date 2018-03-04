import mimetypes
from os.path import splitext

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from gpx.parser.gpx2dict import gpx2dict
from hashtag.models import TagModel
from track.models import TrackModel


class GPXImportView(View):
    @staticmethod
    def post(request):
        file = request.FILES['gpx_file']
        ext = splitext(file.name)[1][1:].lower()
        mime = mimetypes.guess_type(file.name)[0]
        size = len(file)
        if ext == 'gpx' and mime is None and size < 25*1024*1024:
            res = gpx2dict(file.read().decode())
            user = User.objects.get(username=request.user.username)
            tag = TagModel.objects.get(name='None')
            for key, value in res.items():
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
                    activity=tag,
                    geom=value['geom']
                ).save()
        return HttpResponseRedirect(reverse('tracks'))
