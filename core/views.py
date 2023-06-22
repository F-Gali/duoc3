from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def root(request):
    return redirect('home')

def home(request):
    return render(request,'home.html')
