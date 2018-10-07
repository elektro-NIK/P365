from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from story.forms import StoryForm
from story.models import StoryModel


@method_decorator(login_required, name='dispatch')
class StoriesView(View):
    @staticmethod
    def get(request):
        return render(request, 'stories.html', {'title': 'Stories', 'active': 'stories'})


@method_decorator(login_required, name='dispatch')
class StoryView(View):
    @staticmethod
    def get(request, id):
        story = get_object_or_404(StoryModel, id=id)
        if story.user == story.user or story.public:
            return render(request, 'view.html', {'title': story.name, 'story': story})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class StoryEditView(View):
    @staticmethod
    def get(request, id=None):
        story = get_object_or_404(StoryModel, id=id) if id else None
        if story and story.user != request.user:
            return HttpResponseForbidden()
        form = StoryForm(instance=story)
        return render(request, 'editor.html', {'title': story.name if story else 'New story', 'form': form})
