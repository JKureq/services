from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'register/register.html',{
                'form': form
            })
    else:
        form = CreateUserForm()
        return render(request, 'register/register.html', {
            'form': form
        })
        