from django.forms import ModelForm

from story.models import StoryModel


class StoryForm(ModelForm):
    class Meta:
        model = StoryModel
        exclude = ()
