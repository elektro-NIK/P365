from django.http import HttpResponse
from django.views import View


class TagView(View):
    def get(self, request, slug):
        return HttpResponse(slug)
