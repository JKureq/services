from django.shortcuts import render, redirect
from register.forms import CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
# Create your views here.


def login_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login/login.html', {
                'form': form,
                'fail': True
            })
    else:
        form = CreateUserForm()

    return render(request, 'login/login.html', {
        'form': form,
        'fail': False
    })


