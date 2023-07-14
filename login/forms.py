from django import forms
from django.forms import ModelForm
from .models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'rol'
        ]
        labels = {
            'id':'ID',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Email',
            'password':'Contraseña',
            'rol':'Rol'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'rol':forms.TextInput(attrs={'class':'form-control'})
        }