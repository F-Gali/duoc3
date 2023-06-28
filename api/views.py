from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from crud.models import *
from .serializers import *

from django.http.response import JsonResponse

@api_view(['GET','POST','DELETE'])
def articles_list(request):
    if request.method == 'GET':
        articulos = Articulo.objects.all()
        
        titulo = request.query_params.get('titulo',None)
        if titulo is not None:
            articulos = articulos.filter(titulo__contains=titulo)

        autor = request.query_params.get('autor',None)
        if autor is not None:
            articulos = articulos.filter(autor__contains=autor)

        id_compania = request.query_params.get('id_compania',None)
        if id_compania is not None:
            articulos = articulos.filter(id_compania__nombre__contains=id_compania)

        articulos_serializer = ArticuloSerializer(articulos,many=True)
        return Response(articulos_serializer.data)       

    
    elif request.method == 'POST':
        articulo_data = JSONParser().parse(request)
        articulo_serializer = ArticuloSerializer(data=articulo_data)
        if articulo_serializer.is_valid():
            articulo_serializer.save()
            return JsonResponse(articulo_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(articulo_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cantidad = Articulo.objects.all().delete()
        return Response({'mensajes':'Se han eliminado {} articulos de la base de datos'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,article_id):
    try:
        articulo = Articulo.objects.get(id=article_id)
    except:
        return Response({'mensaje':'El articulo {} no existen en nuestros registros'.format(article_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        articulo_serializer = ArticuloSerializer(articulo)
        return Response(articulo_serializer.data)

    elif request.method == 'PUT':
        articulo_data = JSONParser().parse(request)
        articulo_serializer = ArticuloSerializer(articulo, data=articulo_data)
        if articulo_serializer.is_valid():
            articulo_serializer.save()
            return JsonResponse(articulo_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(articulo_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        articulo.delete()
        return Response({'mensaje':'El articulo {} ha sido eliminado de la base de datos.'.format(article_id)},status=status.HTTP_204_NO_CONTENT)
