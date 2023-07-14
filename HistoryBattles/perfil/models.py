from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

class InfoPersonal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    enlace = models.URLField(max_length=200)

    def __str__(self):
        return self.enlace
    