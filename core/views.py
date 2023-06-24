from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def root(request):
    return redirect('home')

def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

# IGNORAR ESTO DE ABAJO, HACIENDO PRUEBAS
# def compania(request, id):
#     return HttpResponse( "nombre de la huea %s" % id)