from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class LoginView(DjangoLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Login',
    }


class SignUpView(View):
    def get(self, request):
        if request.user:
            return HttpResponseRedirect(reverse('profile', kwargs={'username': request.user.username}))
        # else:
        #     form = RegisterForm()
        #     return render(request, 'register.html', {'form': form})


class ProfileRedirect(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return HttpResponseRedirect(reverse('profile', kwargs={'username': user.username}))


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        return render(request, 'profile.html', {
            'title': 'Profile'
        })
