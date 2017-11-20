from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        return render(request, 'profile.html')
