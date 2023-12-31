from django.db import models
from django.utils.timezone import datetime


class Compania(models.Model):
    nombre = models.CharField(max_length=64)
    creacion = models.DateTimeField(verbose_name='Fecha Registro', auto_now_add=True)
    def __str__(self):
        return str(self.nombre)

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255,default='Anonimo')
    html_body = models.CharField(max_length=4096)
    headerImage = models.ImageField(verbose_name='ImagenHeader',upload_to='articles',null=True,blank=True)
    articleImage = models.ImageField(verbose_name='ImagenArticulo',upload_to='articles',null=True,blank=True)
    id_compania = models.ForeignKey(Compania, on_delete=models.CASCADE)
    creacion = models.DateTimeField(verbose_name='Fecha Registro', auto_now_add=True)
    actualizacion = models.DateTimeField(verbose_name='Fecha Actualización', auto_now=True)
    def __str__(self):
        return str(self.titulo)

# RIP Contraseña y fecha nacimiento porque no tienen sentido
class Mensaje(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    mensaje = models.CharField(max_length=100)
    creacion = models.DateTimeField(verbose_name='Fecha Registro', auto_now_add=True)

class Comentario(models.Model):
    autor = models.CharField(max_length=100,default='Anonimo')
    mensaje = models.CharField(max_length=100)
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    creacion = models.DateTimeField(verbose_name='Fecha Registro', auto_now_add=True)

# Nota
# Admin de django
# john_romero_carmack
# pass -> 123