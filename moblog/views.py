from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Bici

# Create your views here.
def inicio(request):
    return render(request, 'mobike/inicio.html')