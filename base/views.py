from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Feed, Message
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from .models import Room

# Create your views here.


@login_required(login_url="/login")
def home(request):
    sendMessage(request)
    messages = Feed.objects.all()
    return render(request, 'home.html', {'messagesList': messages})


@login_required(login_url="/login")
def room(request, pk):
    room_object = Room.objects.get(id=pk)
    send_room_msg(request, room_object)

    room_messages = Message.objects.filter(room=room_object)
    return render(request, 'room.html', {'messagesList': room_messages, 'room': room_object})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is wrong')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def sendMessage(request):
    if request.method == "POST":
        msg = request.POST.get('msg')

        current_user = request.user
        if msg != '':
            newMessage = Feed(user=current_user, text=msg)
            newMessage.save()
        else:
            file = request.FILES['docfile']
            file_name = default_storage.save(file.name, file)
            newMessage = Feed(user=current_user, text=file.name)
            newMessage.save()

    context = {}
    return render(request, 'home.html', context)


def select_room(request):
    if request.method == "POST":
        name = request.POST.get('name')
        current_user = request.user

        if name != '':
            newRoom = Room(host=current_user, name=name)
            newRoom.save()

    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'selectRoom.html', context)


def send_room_msg(request, pk):
    if request.method == "POST":
        msg = request.POST.get('msg')

        current_user = request.user
        current_room = Room.objects.get(name=pk)

        print(pk)
        if msg != '':
            newMessage = Message(user=current_user, room=current_room, text=msg)
            newMessage.save()
        else:
            file = request.FILES['docfile']
            file_name = default_storage.save(file.name, file)
            newMessage = Message(user=current_user, room=current_room, text=file.name)
            newMessage.save()

    context = {}
    return render(request, 'room.html', context)

