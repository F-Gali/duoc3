from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
from functools import wraps
# Create your views here.

def logeado(function):
    @wraps(function)
    def wrap(request,*args,**kwargs):
        if 'usuario' not in request.session:
            messages.error(request,'ACCESO DENEGADO: DESER ESTAR LOGEADO PARA INGRESAR A ESTA PÁGINA.')
            return redirect('/home')
        else:
            return function(request,*args,**kwargs)
    return wrap

def editor(function):
    @wraps(function)
    def wrap(request,*args,**kwargs):
            if 'usuario' not in request.session:
                messages.error(request,'ACCESO DENEGADO: DESER ESTAR LOGEADO PARA INGRESAR A ESTA PÁGINA.')
                return redirect('/home')
            else:
                if request.session['usuario'].get('rol') != 'EDITOR' and request.session['usuario'].get('rol') != 'ADMIN':
                    messages.error(request,'ACCESO DENEGADO: DEBES SER UN EDITOR DE LA PÁGINA PARA INGRESAR.')
                    return redirect('/home')
                else:
                    return function(request,*args,**kwargs)
    return wrap

def admin(function):
    @wraps(function)
    def wrap(request,*args,**kwargs):
            if 'usuario' not in request.session:
                messages.error(request,'ACCESO DENEGADO: DESER ESTAR LOGEADO PARA INGRESAR A ESTA PÁGINA.')
                return redirect('/home')
            else:
                if request.session['usuario'].get('rol') != 'ADMIN':
                    messages.error(request,'ACCESO DENEGADO: DEBES SER UN ADMINISTRADOR DE LA PÁGINA PARA INGRESAR.')
                    return redirect('/home')
                else:
                    return function(request,*args,**kwargs)
    return wrap

def alreadyLoged(function):
    @wraps(function)
    def wrap(request,*args,**kwargs):
        if 'usuario' in request.session:
            messages.error(request,'ACCESO DENEGADO: YA ESTÁS LOGEADO.')
            return redirect('/home')
        else:
            return function(request,*args,**kwargs)
    return wrap

@alreadyLoged
def home(request):
    return render(request,'login/login.html')

def register(request):
    if request.method == 'GET':
        return redirect('/login/')
    else:
        if request.method == 'POST':
            print("entro uwu")
            errors = User.objects.validador_campos(request.POST)

            if len(errors) > 0:
                print("Se produjo un error en el registro")
                for key, value in errors.items():
                    messages.error(request,value)

                #Si se produce un error pero no queremos perder los datos....
                request.session['registro_nombre'] = request.POST['first_name']
                request.session['registro_apellido'] = request.POST['last_name']
                request.session['registro_email'] = request.POST['email']
                request.session['level_mensaje'] = 'alert-danger'
                

            else:
                request.session['registro_nombre'] = ""
                request.session['registro_apellido'] = ""
                request.session['registro_email'] = ""

                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

                obj = User.objects.create(first_name=first_name, last_name=last_name,email=email,password=password_hash)
                messages.success(request, "Usuario registrado con éxito!!!!")
                request.session['level_mensaje'] = 'alert-success'
            
            return redirect('/login/')

        return render(request, 'login/login.html')
            
            
def login(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        if request.method == 'POST':
            
            user = User.objects.filter(email=request.POST['email_login']) #Buscamos el correo ingresado en la BD             
            
            if user : #Si el usuario existe

                usuario_registrado = user[0]
                
                if bcrypt.checkpw(request.POST['password_login'].encode(), usuario_registrado.password.encode()): 
                    usuario = {
                        'id':usuario_registrado.id,
                        'first_name':usuario_registrado.first_name,
                        'last_name':usuario_registrado.last_name,
                        'email':usuario_registrado.email,
                        'rol':usuario_registrado.rol,
                    }

                    request.session['usuario'] = usuario
                    messages.success(request,"INGRESO EXITOSO")
                    return redirect('/home')
                else:
                    messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                    return redirect('/login/')
            else:
                messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                return redirect('/login/')
            

def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return redirect('/home')

