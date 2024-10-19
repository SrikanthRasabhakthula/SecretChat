from django.shortcuts import render, redirect
from .models import Room, Messages
from django.http import HttpResponse, JsonResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        return HttpResponse("Room does not exist")
    
    return render(request, 'room.html', {
        'room': room,
        'username': username,
        'room_details': room_details,
    })


def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room_name).exists(): 
        return redirect(f'/{room_name}/?username={username}')
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect(f'/{room_name}/?username={username}')


from django.shortcuts import get_object_or_404

def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')
    
    # Fetch the Room instance using room_id
    room = get_object_or_404(Room, id=room_id)

    # Create a new message
    new_message = Messages.objects.create(value=message, user=username, room=room)

    return HttpResponse('Message sent successfully')



def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Messages.objects.filter(room=room_details.id)
    return JsonResponse({'messages': list(messages.values())})

