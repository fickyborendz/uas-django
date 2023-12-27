from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())
def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())
def contacUs(request):
    template = loader.get_template('contacUs.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())



