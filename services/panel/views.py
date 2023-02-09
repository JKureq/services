from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    if request.method == 'POST':
        logout(request)

    return render(request, 'panel/index.html')
    

def panel(request):
    return render(request, 'panel/panel.html')

