from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name='dispatch')
class StoriesView(View):
    @staticmethod
    def get(request):
        return render(request, 'stories.html', {'title': 'Stories', 'active': 'stories'})
