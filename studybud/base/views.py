from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    
]
def home(request): #request refers to HTTP request object
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')