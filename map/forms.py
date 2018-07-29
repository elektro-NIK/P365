from django.contrib.gis.geos import Point, LineString
from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget

from google_api.elevation import get_elevation
from .models import POIModel, RouteModel


class POIForm(ModelForm):
    class Meta:
        model = POIModel
        fields = ['name', 'description', 'geom']
        # fields = ['name', 'description', 'tag', 'geom']
        widgets = {'geom': LeafletWidget()}

    def clean_geom(self):
        return Point(*get_elevation(self.cleaned_data['geom']))


class RouteForm(ModelForm):
    class Meta:
        model = RouteModel
        fields = ['name', 'description', 'geom']
        # fields = ['name', 'description', 'tag', 'geom']
        widgets = {'geom': LeafletWidget()}

    def clean_geom(self):
        return LineString(*get_elevation(self.cleaned_data['geom']))
