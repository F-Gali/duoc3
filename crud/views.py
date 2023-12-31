from django.shortcuts import render, redirect;
from django.urls import reverse;

from .models import *
from .forms import *
from functools import wraps
from django.contrib import messages
from login.views import logeado,editor,admin
from login.models import *
from login.forms import *
# Create your views here.



@editor
def root(request):
    return redirect(listado_articulos)

@editor
def listado_articulos(request):
    context = {'articulos':Articulo.objects.all()}
    return render(request,'crud/articulos.html',context)

@editor
def crear_articulo(request):
    form = ArticuloForm()
    context = { 'form' : form }
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista-articulos') + '?exito-crear-articulo')
        else:
            return redirect(request.path + '?error')
    return render(request,'crud/nuevo_articulo.html', context)

@editor
def eliminar_articulo(request,idArticulo):
        try:
            articulo = Articulo.objects.get(id = idArticulo)
            articulo.delete()
            return redirect(reverse('lista-articulos') + '?exito-eliminar-articulo')
        except:
            return redirect(reverse('lista-articulos') + '?error')

@editor
def editar_articulo(request,idArticulo):
    try:
        articulo = Articulo.objects.get(id = idArticulo)
        form = ArticuloForm(instance=articulo)
        if request.method == 'POST':
            form = ArticuloForm(request.POST, request.FILES, instance=articulo)
            if form.is_valid():
                form.save()
                return redirect(request.path + '?exito')
            else:
                return redirect(reverse('editar-articulo') + idArticulo)

        context = {'form':form}
        return render(request,'crud/editar_articulo.html',context)
    except:
        return render(request,'crud/editar_articulo.html' + '?NO_EXIST')

@editor
def mensajes(request):
    context = {'mensajes':Mensaje.objects.all()}
    return render(request,'crud/messages.html',context)

@editor
def listado_compania(request):
    context = {'companias':Compania.objects.all()}
    return render(request,'crud/companias.html',context)

@editor
def crear_compania(request):
    form = CompaniaForm()
    context = { 'form' : form }
    if request.method == 'POST':
        form = CompaniaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista-compania') + '?exito-crear-compania')
        else:
            return redirect(request.path + '?error')
    return render(request,'crud/nueva_compania.html', context)

@editor
def eliminar_compania(request,idCompania):
    try:
            compania = Compania.objects.get(id = idCompania)
            compania.delete()
            return redirect(reverse('lista-compania') + '?exito-eliminar-compania')
    except:
            return redirect(reverse('lista-compania') + '?error')
    

@editor
def editar_compania(request,idCompania):
    #try:
        compania = Compania.objects.get(id = idCompania)
        form = CompaniaForm(instance=compania)
        if request.method == 'POST':
            form = CompaniaForm(request.POST, request.FILES, instance=compania)
            if form.is_valid():
                form.save()
                return redirect(request.path + '?exito')
            else:
                return redirect(reverse('editar-compania') + idCompania)

        context = {'form':form}
        return render(request,'crud/editar_compania.html',context)
    #except:
    #   return render(request,'crud/editar_compania.html' + '?NO_EXIST') 

@editor
def listado_comentarios(request):
    context = {'comentario':Comentario.objects.all()}
    return render(request,'crud/comentarios.html',context)

@editor
def eliminar_comentario(request,idComentario):
    try:
            comentario = Comentario.objects.get(id = idComentario)
            comentario.delete()
            return redirect(reverse('lista-comentarios') + '?exito-eliminar-comentario')
    except:
            return redirect(reverse('lista-comentarios') + '?error')

@editor
def eliminar_mensaje(request,idMensaje):
    try:
            mensaje = Mensaje.objects.get(id = idMensaje)
            mensaje.delete()
            return redirect(reverse('mensajes') + '?exito-eliminar-mensaje')
    except:
            return redirect(reverse('mensajes') + '?error')

@admin
def lista_Usuarios(request):
    context = {'usuarios':User.objects.all()}
    return render(request,'crud/usuarios.html',context)

@admin
def eliminar_usuario(request,idUsuario):
    try:
            usuario = User.objects.get(id = idUsuario)
            usuario.delete()
            return redirect(reverse('lista-usuarios') + '?exito-eliminar-usuario')
    except:
            return redirect(reverse('lista-usuarios') + '?error')

@admin
def editar_usuario(request,idUsuario):
    # try:
        usuario = User.objects.get(id = idUsuario)
        form = UsuarioForm(instance=usuario)
        if request.method == 'POST':
            form = UsuarioForm(request.POST, request.FILES, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect(request.path + '?exito')
            else:
                return redirect(reverse('editar-usuario') + idUsuario)

        context = {'form':form}
        return render(request,'crud/editar_usuario.html',context)
    # except:
    #    return render(request,'crud/editar_usuario.html' + '?NO_EXIST')