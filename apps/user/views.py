from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class RegisterUser(CreateView):
	"""docstring for RegisterUser"""
	model=User
	template_name='user/create.html'
	form_class=UserCreationForm
	success_url=reverse_lazy('mascota:mascota_list')


