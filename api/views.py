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

@api_view(['GET','POST'])
def company_list(request):
    if request.method == 'GET':
        companias = Compania.objects.all()
        companias_serializer = CompaniaSerializer(companias,many=True)
        return Response(companias_serializer.data)

    elif request.method == 'POST':
        compania_data = JSONParser().parse(request)
        compania_serializer = CompaniaSerializer(data=compania_data)
        if compania_serializer.is_valid():
            compania_serializer.save()
            return JsonResponse(compania_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(compania_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def company_detail(request,company_id):
    try:
        compania = Compania.objects.get(id=company_id)
    except:
        return Response({'mensaje':'La compañia {} no existen en nuestros registros'.format(company_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        compania_serializer = CompaniaSerializer(compania)
        return Response(compania_serializer.data)

    elif request.method == 'PUT':
        compania_data = JSONParser().parse(request)
        compania_serializer = ArticuloSerializer(compania, data=compania_data)
        if compania_serializer.is_valid():
            compania_serializer.save()
            return JsonResponse(compania_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(compania_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        compania.delete()
        return Response({'mensaje':'La compañia {} ha sido eliminada de la base de datos.'.format(company_id)},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','DELETE'])
def messages_list(request):
    if request.method == 'GET':
        mensajes = Mensaje.objects.all()
        
        nombre = request.query_params.get('nombre',None)
        if nombre is not None:
            mensajes = mensajes.filter(nombre__contains=nombre)

        email = request.query_params.get('email',None)
        if email is not None:
            mensajes = mensajes.filter(email__contains=email)

        mensajes_serializer = MensajeSerializer(mensajes,many=True)
        return Response(mensajes_serializer.data)       

    
    elif request.method == 'POST':
        mensaje_data = JSONParser().parse(request)
        mensaje_serializer = MensajeSerializer(data=mensaje_data)
        if mensaje_serializer.is_valid():
            mensaje_serializer.save()
            return JsonResponse(mensaje_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(mensaje_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cantidad = Mensaje.objects.all().delete()
        return Response({'mensajes':'Se han eliminado {} mensajes de la base de datos'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def message_detail(request,message_id):
    try:
        mensaje = Mensaje.objects.get(id=message_id)
    except:
        return Response({'mensaje':'El mensaje {} no existen en nuestros registros'.format(message_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mensaje_serializer = MensajeSerializer(mensaje)
        return Response(mensaje_serializer.data)

    elif request.method == 'PUT':
        mensaje_data = JSONParser().parse(request)
        mensaje_serializer = ArticuloSerializer(mensaje, data=mensaje_data)
        if mensaje_serializer.is_valid():
            mensaje_serializer.save()
            return JsonResponse(mensaje_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(mensaje_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mensaje.delete()
        return Response({'mensaje':'El articulo {} ha sido eliminado de la base de datos.'.format(message_id)},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST','DELETE'])
def comments_list(request):
    if request.method == 'GET':
        comentarios = Comentario.objects.all()
        
        autor = request.query_params.get('autor',None)
        if autor is not None:
            comentarios = comentarios.filter(titulo__contains=autor)

        id_articulo = request.query_params.get('id_articulo',None)
        if id_articulo is not None:
            comentarios = comentarios.filter(id_articulo__titulo__contains=id_articulo)

        comentarios_serializer = ComentarioSerializer(comentarios,many=True)
        return Response(comentarios_serializer.data)       

    
    elif request.method == 'POST':
        comentario_data = JSONParser().parse(request)
        comentario_serializer = ArticuloSerializer(data=comentario_data)
        if comentario_serializer.is_valid():
            comentario_serializer.save()
            return JsonResponse(comentario_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(comentario_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cantidad = Comentario.objects.all().delete()
        return Response({'mensajes':'Se han eliminado {} comentarios de la base de datos'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def comment_detail(request,comment_id):
    try:
        comentario = Comentario.objects.get(id=comment_id)
    except:
        return Response({'mensaje':'El comentario {} no existen en nuestros registros'.format(comment_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comentario_serializer = ComentarioSerializer(comentario)
        return Response(comentario_serializer.data)

    elif request.method == 'PUT':
        comentario_data = JSONParser().parse(request)
        comentario_serializer = ArticuloSerializer(comentario, data=comentario_data)
        if comentario_serializer.is_valid():
            comentario_serializer.save()
            return JsonResponse(comentario_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(comentario_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comentario.delete()
        return Response({'mensaje':'El comentario {} ha sido eliminado de la base de datos.'.format(comment_id)},status=status.HTTP_204_NO_CONTENT)
