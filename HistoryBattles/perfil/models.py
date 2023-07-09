from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    created = models.DateTimeField(default=django.utils.timezone.now)
    updated = models.DateTimeField(default=django.utils.timezone.now)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
    