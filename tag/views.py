from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class TagCloudView(View):
    @staticmethod
    def get(request):
        return HttpResponseNotFound(404)


class TagView(View):
    @staticmethod
    def get(request, tag):
        return HttpResponseNotFound(tag)
