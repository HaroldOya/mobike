from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Bici
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *


# Create your views here.
def inicio(request):
    return render(request, 'mobike/inicio.html')

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)    


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "mobike/inicio.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

    
def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()        
  
    return render(request, 'mobike/registro.html', { 'form': form })  


def bici_list(request):
    bici = Bici.objects.order_by('codigo')     
    return render(request, 'mobike/arrendar.html', { 'bici': bici } )      


  


