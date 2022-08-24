from django.shortcuts import render
from .models import Familiar

# Create your views here.
def crear_familiar(request):
    familiar = Familiar.objects.create(nombre = "Matias",años = 24,fecha_de_nacimiento = "1998-06-16")
    context = {'familiar': familiar}
    return render(request,'home.html', context)

def ver_familiar(request):
    familiares = Familiar.objects.all()
    context = {'familiares': familiares}
    return render(request,'home.html', context) 