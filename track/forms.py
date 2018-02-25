from django import forms

from leaflet.forms.widgets import LeafletWidget

from .models import TrackModel


class TrackEditForm(forms.ModelForm):
    class Meta:
        model = TrackModel
        fields = ('name', 'description', 'activity', 'geom')
        widgets = {'geom': LeafletWidget()}
