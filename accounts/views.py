from django.shortcuts import render 
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.models import User


class SignUpView(CreateView):
    form_class = UserCreationForm
    model = User
    success_url=reverse_lazy('login')
    template_name = 'accounts/signup.html'
# Create your views here.
