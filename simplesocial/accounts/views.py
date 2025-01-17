from django.shortcuts import render
from django.urls import reverse_lazy  #if someone is logged in or out where they shoudl actually go
from django.views.generic import CreateView


from . import forms

#create your views here

class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url =reverse_lazy('login')
	template_name = 'accounts/signup.html'