from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView
from .models import MyUser
from django.http import HttpResponse

class CreateUserView(CreateView):
    model = MyUser
    fields = ['email', 'password', 'first_name', 'last_name', 'location']
    success_url = 'create-done'

class CreateDoneView(TemplateView):
    template_name ='create_done.html'

    
        

