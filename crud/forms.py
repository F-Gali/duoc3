from django import forms
from django.forms import ModelForm
from .models import *

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'id',
            'autor',
            'titulo',
            'html_body',
            'id_compania',
            'headerImage',
            'articleImage'
        ]
        labels = {
            'id':'ID',
            'autor':'Autor',
            'titulo':'Titulo',
            'html_body':'Cuerpo del articulo',
            'id_compania':'Compania',
            'headerImage':'Imagen de cabecera',
            'articleImage':'Imagen del articulo'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.TextInput(attrs={'class':'form-control'}),
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'html_body':forms.Textarea(attrs={'class':'form-control'}),
            'id_compania':forms.Select(attrs={'class':'form-control'}),
            'headerImage':forms.FileInput(attrs={'class':'form-control'}),
            'articleImage':forms.FileInput(attrs={'class':'form-control'})
        }

class CompaniaForm(ModelForm):
    class Meta:
        model = Compania
        fields = [
            'id',
            'nombre'
        ]
        labels = {
            'id':'ID',
            'nombre':'Nombre'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }

class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = [
            'nombre',
            'apellido',
            'email',
            'mensaje'
        ]
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'email':'Email',
            'mensaje':'Mensaje'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','onBlur': 'validarNombre()','name':'nombre','id':'nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control','onblur':'validarApellido()','name':'apellido','id':'apellido'}),
            'email':forms.TextInput(attrs={'class':'form-control','onblur':'validarEmail()','name':'email','id':'email'}),
            'mensaje':forms.Textarea(attrs={'class':'form-control','name':'mensaje','id':'mensaje','cols':'30','rows':'10'})
        }
    
class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'autor',
            'mensaje'
        ]
        labels = {
            'autor':'Autor',
            'mensaje':'Mensaje'
        }
        widgets = {
            'autor':forms.TextInput(attrs={'class':'form-control'}),
            'mensaje':forms.Textarea(attrs={'class':'form-control'})
        }