from django.contrib import admin

# Register your models here.
# from django.db import models


# from django.contrib import admin
# from .models import Platform, VideoGame

# # Register your models here.
# class PlatformAdmin(admin.ModelAdmin):
#     readonly_fields = ('id','created_at','updated_at')
#     list_display = ('id','platform')
#     ordering = ('platform',)

# class VideoGameAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at','updated_at')
#     list_display = ('idVideogame','title','studio','platform','value','stock')
#     ordering = ('title',)

# admin.site.register(Platform,PlatformAdmin)
# admin.site.register(VideoGame,VideoGameAdmin)

from django.db import models
from django.contrib import admin
from .models import Compania, Articulo, Mensaje, Comentario

class CompaniaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'creacion')
    list_display = ('id', 'nombre')
    ordering = ('nombre',)

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('id','creacion','actualizacion')
    list_display = ('id', 'titulo', 'id_compania')
    ordering = ('id',)

class MensajeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'creacion')
    list_display = ('id', 'nombre', 'mensaje')
    ordering = ('creacion',)

class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'creacion')
    list_display = ('id', 'autor', 'mensaje','id_articulo')
    ordering = ('creacion',)

# class Compania(models.Model):
#     nombre = models.CharField(max_length=64)
#     creacion = models.DateTimeField(verbose_name='Fecha Registro', auto_now_add=True)

# class Articulo(models.Model):
#     titulo = models.CharField(max_length=255)
#     html_body = models.CharField(max_length=4096)
#     id_compania = models.ForeignKey(Compania, on_delete=models.CASCADE)
#     creacion = models.DateTimeField(verbose_name='Fecha Registro', auto_now_add=True)
#     actualizacion = models.DateTimeField(verbose_name='Fecha Actualización', auto_now=True)

# # RIP Contraseña y fecha nacimiento porque no tienen sentido
# class Mensaje(models.Model):
#     nombre = models.CharField(max_length=15)
#     apellido = models.CharField(max_length=32)
#     rut = models.IntegerField(default=0, null=False)
#     email = models.CharField(max_length=32)
#     mensaje = models.CharField(max_length=100)

admin.site.register(Compania, CompaniaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Comentario, ComentarioAdmin)