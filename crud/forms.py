from django import forms
from django.forms import ModelForm
from .models import *

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'titulo',
            'html_body',
            'id_compania'
        ]
        labels = {
            'titulo':'Titulo',
            'html_body':'Cuerpo del articulo',
            'id_compania':'Compania'
        }
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'html_body':forms.TextInput(attrs={'class':'form-control'}),
            'id_compania':forms.Select(attrs={'class':'form-control'})
        }

class PlatformForm(ModelForm):
    pass
