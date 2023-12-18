from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    pass

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'  # Path to your profile template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Add user to context
        return context




def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })
