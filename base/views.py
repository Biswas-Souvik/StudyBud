from django.shortcuts import render

rooms = [
    {'id': 1, 'name': "let's learn Python"},
    {'id': 2, 'name': "How I learn Python"},
    {'id': 3, 'name': "Python 201"},
]

# Create your views here.
def home(request):
    
    return render(request, 'base/home.html', {'topics': rooms})


def room(request, id):

    topic = None
    for room in rooms:
        if room['id'] == id:
            topic = room
            break

    return render(request, 'base/room.html', topic)