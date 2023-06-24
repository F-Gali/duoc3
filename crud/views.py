from django.shortcuts import render, redirect, reverse  

from .models import *
from .forms import *
# Create your views here.
def root(request):
    return redirect(listado_articulos)

def listado_articulos(request):
    context = {'articulos':Articulo.objects.all()}
    return render(request,'crud/articulos.html',context)

def crear_articulo(request):
    return render(request,'crud/nuevo_articulo.html')

def editar_articulo(request,idArticulo):
    try:
        articulo = Articulo.objects.get(id = idArticulo)
        form = ArticuloForm(instance=articulo)
        if request.method == 'POST':
            form = ArticuloForm(request.POST, request.FILES, instance=articulo)
            if form.is_valid():
                form.save()
                return redirect(reverse('lista-articulos') + '?UPDATED')
            else:
                return redirect(reverse('editar-articulo') + idArticulo)

        context = {'form':form}
        return render(request,'crud/editar_articulo.html',context)
    except:
        return render(request,'crud/editar_articulo.html' + '?NO_EXIST')
