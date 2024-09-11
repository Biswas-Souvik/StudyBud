from django.shortcuts import render

rooms = [
    {'id': 1, 'name': "let's learn Python"},
    {'id': 2, 'name': "How I learn Python"},
    {'id': 3, 'name': "Python 201"},
]

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def room(request):
    return render(request, 'base/room.html', {'topics': rooms})