from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def root(request):
    return redirect('home')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# IGNORAR ESTO DE ABAJO, HACIENDO PRUEBAS
# def compania(request, id):
#     return HttpResponse( "nombre de la huea %s" % id)