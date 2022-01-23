from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Front-end developers'},
# ]


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) #This will add the session in the browser and DB, thus logging the user in
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist.')

    context={}
    return render(request, 'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):  # request refers to HTTP request object
    q = request.GET.get('q') if request.GET.get('q')!=None else '' #This will get the query parameter from the URL, if it exists
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        ) #Making a call upwards to the topic schema, and making sure that the topic name at least contains the query string (case insensitive)
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics':topics, 'room_count':room_count} 
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'room': room}
    return render(request, 'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method=='POST':
        # print(request.POST) #Prints a dictionary of form data sent by the user in a post request
        form=RoomForm(request.POST) #Specifying the values that the form needs to extract
        if form.is_valid():
            form.save()
            return redirect('home')


    context={'form':form}
    return render(request, 'base/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) #Adding instance to specify which data needs to be updated. Otherwise a new row will be added
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method=='POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':room} )