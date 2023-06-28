from dataclasses import field
from rest_framework import serializers
from crud.models import *


class CompaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compania
        fields = (
            'id','nombre','creacion'
        )

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = (
            'id','titulo','html_body','id_compania','creacion','actualizacion'
        )

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = (
            'id','nombre','apellido','email','mensaje','creacion'
        )

class ComentarioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comentario
        fields = (
            'id','autor','mensaje','id_articulo','creacion'
        )

