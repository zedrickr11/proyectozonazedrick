from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class Genero(models.Model):
    nombre  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_inicio = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    nombre  =   models.CharField(max_length=30)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Artista = models.ForeignKey(Artista, blank=True, null=True,  on_delete=models.CASCADE)
    Genero = models.OneToOneField(Genero, blank=True, null=True,  on_delete=models.CASCADE)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
    duracion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Vocalista(models.Model):
    nombre  =   models.CharField(max_length=30)
    apellido  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    residencia  =   models.CharField(max_length=30)
    email  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo  =   models.CharField(max_length=30)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)
    num_pista = models.IntegerField()
    duracion = models.CharField(max_length=30)
    fecha_creacion = models.DateField(blank=True, null=True)
    Vocalista = models.ManyToManyField(Vocalista, through='Participacion')

    def __str__(self):
        return self.titulo

class Participacion (models.Model):
    Vocalista = models.ForeignKey(Vocalista, on_delete=models.CASCADE)
    Cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

class ParticipacionInLine(admin.TabularInline):
    model = Participacion
    extra = 1

class VocalistaAdmin(admin.ModelAdmin):
    inlines = (ParticipacionInLine,)

class CancionAdmin (admin.ModelAdmin):
    inlines = (ParticipacionInLine,)
