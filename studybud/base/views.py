from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request): #request refers to HTTP request object
    return HttpResponse('Home page')

def room(request):
    return HttpResponse("ROOM")