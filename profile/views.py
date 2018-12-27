from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from map.models import TrackModel, RouteModel
from story.models import StoryModel
from .forms import SignUpForm
from .models import ProfileModel


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html', {'title': 'Index'})


class LoginView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user:profile', kwargs={'username': request.user}))
        else:
            form = AuthenticationForm()
            nexturl = request.GET.get('next') or ''
            return render(request, 'login.html', {'title': 'Login', 'form': form, 'next': nexturl})

    @staticmethod
    def post(request):
        form = AuthenticationForm(data=request.POST)
        nexturl = request.GET.get('next')
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            login(request, user)
            return HttpResponseRedirect(nexturl or reverse('user:profile', kwargs={'username': request.user}))
        else:
            return render(request, 'login.html', {'title': 'Login', 'form': form, 'next': nexturl})


class SignUpView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user:profile', kwargs={'username': request.user}))
        else:
            form = SignUpForm()
            nexturl = request.GET.get('next') or ''
            return render(request, 'register.html', {'title': 'Sign Up', 'form': form, 'next': nexturl})

    @staticmethod
    def post(request):
        form = SignUpForm(data=request.POST)
        nexturl = request.GET.get('next')
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            if user:
                login(request, user)
            return HttpResponseRedirect(nexturl or reverse('user:profile', kwargs={'username': user.username}))
        else:
            return render(request, 'register.html', {'title': 'Sign Up', 'form': form, 'next': nexturl})


class ProfileRedirect(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return HttpResponseRedirect(reverse('user:profile', kwargs={'username': request.user}))


class ProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, username):
        profile = get_object_or_404(ProfileModel, user__username=username)
        if request.user.username == username:
            counter = {
                'tracks': TrackModel.objects.filter(user__username=username, is_active=True).count(),
                'routes': RouteModel.objects.filter(user__username=username, is_active=True).count(),
                'stories': StoryModel.objects.filter(user__username=username, is_active=True).count(),
            }
        else:
            counter = {
                'tracks': TrackModel.objects.filter(user__username=username, public=True, is_active=True).count(),
                'routes': RouteModel.objects.filter(user__username=username, public=True, is_active=True).count(),
                'stories': StoryModel.objects.filter(user__username=username, is_active=True).count(),
            }
        return render(request, 'profile.html', {'title': 'Profile', 'profile': profile, 'counter': counter})
