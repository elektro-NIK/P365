from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from profile.forms import SignUpForm


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html', {'title': 'Index'})


class LoginView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('profile', kwargs={'username': request.user.username}))
        else:
            from django.contrib.auth.forms import AuthenticationForm
            form = AuthenticationForm()
            nexturl = request.GET.get('next') or ''
            return render(request, 'login.html', {'title': 'Sign Up', 'form': form, 'next': nexturl})

    @staticmethod
    def post(request):
        from django.contrib.auth.forms import AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        nexturl = request.POST['next']
        if form.is_valid():
            user = User.objects.get(username=request.POST['username'])
            login(request, user)
            return HttpResponseRedirect(nexturl or reverse('profile', kwargs={'username': user.username}))
        else:
            return render(request, 'login.html', {
                'title': 'Login',
                'form': form,
                'next': nexturl,
                'active': 'login',
            })


class SignUpView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('profile', kwargs={'username': request.user.username}))
        else:
            form = SignUpForm()
            nexturl = request.GET.get('next') or ''
            return render(request, 'register.html', {'title': 'Sign Up', 'form': form, 'next': nexturl})

    @staticmethod
    def post(request):
        form = SignUpForm(data=request.POST)
        nexturl = request.POST['next']
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password1'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(nexturl or reverse('profile', kwargs={'username': user.username}))
        else:
            return render(request, 'register.html', {
                'title': 'Sign Up',
                'form': form,
                'next': nexturl,
                'active': 'signup',
            })


class ProfileRedirect(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return HttpResponseRedirect(reverse('profile', kwargs={'username': request.user.username}))


class ProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, username):
        profile = User.objects.get(username=username)
        return render(request, 'profile.html', {'title': 'Profile', 'profile': profile})
