from django.shortcuts import render
from django.urls import reverse_lazy
#reverse_lazy is used when we have to go somewere after login or logout
from . import forms
#  . import means "within the directory where this file belongs" i,e.
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "all_accounts/signup.html"
