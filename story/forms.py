from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from story.models import StoryModel


class StoryForm(ModelForm):
    class Meta:
        model = StoryModel
        exclude = ('user',)
        widgets = {
            'text': SummernoteWidget(),
        }

    def clean(self):
        # Bad way to fix one-to-one field without changing error. FIXME!
        return self.cleaned_data
