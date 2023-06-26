from django.urls import path
from .views import *

urlpatterns = [
    path('',root),
    path('articulos/', listado_articulos, name="lista-articulos"),
    path('articulos/nuevo/', crear_articulo, name="crear-articulo"),
    path('articulos/editar/<int:idArticulo>/', editar_articulo, name="editar-articulo"),
    path('articulos/eliminar/<int:idArticulo>/', eliminar_articulo, name="eliminar-articulo"),
    path('mensajes/', mensajes, name="mensajes"),
    
]