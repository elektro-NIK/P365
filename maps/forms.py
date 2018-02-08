from django import forms

from leaflet.forms.widgets import LeafletWidget

from maps.models import TrackModel


class TrackEditForm(forms.ModelForm):
    class Meta:
        model = TrackModel
        fields = ('name', 'description', 'start_date', 'finish_date', 'activity', 'geom')
        widgets = {'geom': LeafletWidget()}
