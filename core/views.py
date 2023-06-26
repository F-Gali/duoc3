from django.shortcuts import render, HttpResponse, redirect,reverse
from crud.models import *
from crud.forms import *
# Create your views here.

def root(request):
    return redirect('home')

def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')


def contact(request):
    form = MensajeForm()
    context = { 'form' : form }
    if request.method == 'POST':
        form = MensajeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home') + '?exito')
        else:
            return redirect(request.path + '?error')
    return render(request,'core/contact.html',context)

def articles(request):
    context = {'articulos':Articulo.objects.all()}
    return render(request,'core/articles.html',context)

def articles_by_company(request,compania):
    context = {'articulos':Articulo.objects.filter(id_compania=compania)}
    return render(request,'core/articles.html',context)
  
def articulo_completo(request,id_articulo):
    try:
        articulo = Articulo.objects.get(id=id_articulo)
        if articulo:
            form = ComentarioForm()
            context = {'articulo': articulo ,'comentario' : Comentario.objects.filter(id_articulo=id_articulo),'cantidadComentarios':Comentario.objects.filter(id_articulo=id_articulo).count(),'form':form}
            if request.method == 'POST':
                form = ComentarioForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect(request.path + '?exito')
                else:
                    return redirect(request.path + '?error')
            return render(request,'core/article.html',context)
        else:
            return redirect(reverse('articles') + '?NO_EXIST')
    except:
        return redirect(reverse('articles') + '?NO_EXIST')

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

# IGNORAR ESTO DE ABAJO, HACIENDO PRUEBAS
# def compania(request, id):
#     return HttpResponse( "nombre de la huea %s" % id)