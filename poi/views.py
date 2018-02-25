from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views import View

from .models import POIModel


class GetPoisView(View):
    @staticmethod
    def get(request):
        user = User.objects.get(username=request.user.username)
        pois = POIModel.objects.filter(user=user, is_active=True)
        data = serialize('geojson', pois, geometry_field='geom')
        return JsonResponse(data, safe=False)
