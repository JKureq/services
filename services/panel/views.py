from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'panel/index.html')

def panel(request):
    return render(request, 'panel/panel.html')