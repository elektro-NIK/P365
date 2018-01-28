from django.shortcuts import render
from django.views import View


class StoriesView(View):
    @staticmethod
    def get(request):
        return render(request, 'stories.html', {'title': 'Stories', 'active': 'stories'})
