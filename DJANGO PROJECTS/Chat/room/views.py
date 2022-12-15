from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def roomview(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', context={'rooms':rooms})

def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'room_detail.html', context={'room':room})

def create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(roomview)

    else:
        form = RoomForm
        return render(request, 'create_room.html', {'form':form})   