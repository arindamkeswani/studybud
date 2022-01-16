from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Front-end developers'},
# ]


def home(request):  # request refers to HTTP request object
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'room': room}
    return render(request, 'base/room.html',context)


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

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) #Adding instance to specify which data needs to be updated. Otherwise a new row will be added
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method=='POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':room} )