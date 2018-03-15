from django.forms import ModelForm, CharField
from leaflet.forms.widgets import LeafletWidget

from P365.settings import MAX_LENGTH
from .models import POIModel, RouteModel


class POIForm(ModelForm):
    class Meta:
        model = POIModel
        fields = ['name', 'description', 'geom']
        widgets = {'geom': LeafletWidget()}

    tag = CharField(max_length=MAX_LENGTH['tag'])


class RouteForm(ModelForm):
    class Meta:
        model = RouteModel
        fields = ['name', 'description', 'geom']
        widgets = {'geom': LeafletWidget()}

    tag = CharField(max_length=MAX_LENGTH['tag'])
