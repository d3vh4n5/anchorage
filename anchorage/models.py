from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length= 100, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="Email")
    dni = models.IntegerField(verbose_name="DNI")

class Link(models.Model):
    # owner = models.CharField(max_length=30, onetomanyfield)
    alias = models.CharField(max_length=100, verbose_name="Alias")
    url = models.URLField(max_length=200, verbose_name="URL")
    date = models.DateField