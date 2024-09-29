from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Modelo del perfil de usuario
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    foto_perfil = models.ImageField(upload_to='perfil_fotos/', blank=True)  # Necesitarás Pillow para manejar imágenes

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
# Modelo del perfil de receta dulce
class RecetaDulce(models.Model):
    nombre_persona = models.CharField(max_length=100)
    nombre_receta = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_subida = models.DateField()
    edad= models.IntegerField()
    

    def __str__(self):
        return self.nombre_receta

# Modelo del perfil de receta salada
class RecetaSalada(models.Model):
    nombre_persona = models.CharField(max_length=100)
    nombre_receta = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_subida = models.DateField()
    edad= models.IntegerField()

    def __str__(self):
        return self.nombre_receta

# Modelo del perfil de receta bebida
class RecetaBebida(models.Model):
    nombre_persona = models.CharField(max_length=100)
    nombre_receta = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_subida = models.DateField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre_receta


