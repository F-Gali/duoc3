from django.shortcuts import render, redirect, reverse  

from .models import *
# Create your views here.
def root(request):
    return redirect(listado_articulos)

def listado_articulos(request):
    context = {'articulos':Articulo.objects.all()}
    return render(request,'crud/articulos.html',context)

def crear_articulo(request):
    return render(request,'crud/nuevo_articulo.html')

def editar_articulo(request):
    return render(request,'crud/editar_articulo.html')
