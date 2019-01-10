from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from story.forms import StoryForm
from story.models import StoryModel


@method_decorator(login_required, name='dispatch')
class StoriesView(View):
    @staticmethod
    def get(request):
        stories = StoryModel.objects.filter(user=request.user, is_active=True).order_by('-event__start_date')
        return render(request, 'stories.html', {'title': 'Stories', 'active': 'stories', 'stories': stories})


@method_decorator(login_required, name='dispatch')
class StoryView(View):
    @staticmethod
    def get(request, id):
        story = get_object_or_404(StoryModel, id=id)
        if (story.user == story.user or story.public) and story.is_active:
            return render(request, 'story-viewer.html', {'title': story.title, 'story': story})
        return HttpResponseForbidden()


@method_decorator(login_required, name='dispatch')
class StoryEditView(View):
    @staticmethod
    def get(request, id=None):
        story = get_object_or_404(StoryModel, id=id) if id else None
        if story and story.user != request.user and story.is_active:
            return HttpResponseForbidden()
        form = StoryForm(request.user, instance=story)
        return render(request, 'story-editor.html', {'title': story.title if story else 'New story', 'form': form})

    @staticmethod
    def post(request, id=None):
        form = StoryForm(request.user, request.POST)
        if form.is_valid():
            if id:
                story = get_object_or_404(StoryModel, id=id)
                story.title = form.cleaned_data['title']
                story.text = form.cleaned_data['text']
                story.track = form.cleaned_data['track']
                story.event = form.cleaned_data['event']
                story.tags.set(*form.cleaned_data['tags'])
            else:
                story = form.save(commit=False)
                story.user = request.user
            story.save()
            form.save_m2m() if not id else None
            return HttpResponseRedirect(reverse('story:stories'))
        return render(request, 'story-editor.html', {'title': form['title'].value(), 'form': form})


@method_decorator(login_required, name='dispatch')
class JSONStoryDeleteView(View):
    @staticmethod
    def post(request, id):
        story = get_object_or_404(StoryModel, id=id)
        if story.user == request.user and story.is_active:
            story.is_active = False
            story.save()
            return JsonResponse({'Status': 'OK'})
        return HttpResponseForbidden()
