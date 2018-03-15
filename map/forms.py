from django.forms import ModelForm, CharField
from leaflet.forms.widgets import LeafletWidget

from P365.settings import MAX_LENGTH
from .models import POIModel


class POIForm(ModelForm):
    class Meta:
        model = POIModel
        exclude = ['user', 'public', 'is_active', 'tag']
        widgets = {'geom': LeafletWidget()}

    tag = CharField(max_length=MAX_LENGTH['tag'])
