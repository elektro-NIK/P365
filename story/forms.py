from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from calendar_year.models import EventModel
from map.models import TrackModel
from .models import StoryModel


class StoryForm(ModelForm):
    class Meta:
        model = StoryModel
        exclude = ('user',)
        widgets = {
            'text': SummernoteWidget(),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['track'].queryset = TrackModel.objects.filter(user=user, is_active=True)
            self.fields['event'].queryset = EventModel.objects.filter(user=user, is_active=True)

    def clean(self):
        # Bad way to fix one-to-one field without changing error. FIXME!
        return self.cleaned_data
