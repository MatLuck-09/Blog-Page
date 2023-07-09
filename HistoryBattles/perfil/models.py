from django.db import models
import django.utils.timezone

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    created = models.DateTimeField(default=django.utils.timezone.now)
    updated = models.DateTimeField(default=django.utils.timezone.now)
    