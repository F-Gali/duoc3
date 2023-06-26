from django.shortcuts import render, redirect;
from django.urls import reverse;

from .models import *
from .forms import *
# Create your views here.
def root(request):
    return redirect(listado_articulos)

def listado_articulos(request):
    context = {'articulos':Articulo.objects.all()}
    return render(request,'crud/articulos.html',context)

def crear_articulo(request):
    form = ArticuloForm()
    context = { 'form' : form }
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista-articulos') + '?exito')
        else:
            return redirect(request.path + '?error')
    return render(request,'crud/nuevo_articulo.html', context)

def eliminar_articulo(request,idArticulo):
        try:
            articulo = Articulo.objects.get(id = idArticulo)
            articulo.delete()
            return redirect(reverse('lista-articulos') + '?exito')
        except:
            return redirect(reverse('lista-articulos') + '?error')

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

def mensajes(request):
    context = {'mensajes':Mensaje.objects.all()}
    return render(request,'crud/messages.html',context)

def listado_compania(request):
    context = {'companias':Compania.objects.all()}
    return render(request,'crud/companias.html',context)

def crear_compania(request):
    form = CompaniaForm()
    context = { 'form' : form }
    if request.method == 'POST':
        form = CompaniaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista-compania') + '?exito')
        else:
            return redirect(request.path + '?error')
    return render(request,'crud/nueva_compania.html', context)

def eliminar_compania(request,idCompania):
    try:
            compania = Compania.objects.get(id = idCompania)
            compania.delete()
            return redirect(reverse('lista-compania') + '?exito')
    except:
            return redirect(reverse('lista-compania') + '?error')
    

def editar_compania(request,idCompania):
    #try:
        compania = Compania.objects.get(id = idCompania)
        form = CompaniaForm(instance=compania)
        if request.method == 'POST':
            form = CompaniaForm(request.POST, request.FILES, instance=compania)
            if form.is_valid():
                form.save()
                return redirect(reverse('lista-compania') + '?UPDATED')
            else:
                return redirect(reverse('editar-compania') + idCompania)

        context = {'form':form}
        return render(request,'crud/editar_compania.html',context)
    #except:
    #   return render(request,'crud/editar_compania.html' + '?NO_EXIST') 
    
