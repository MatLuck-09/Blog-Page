from django.db import models
import django.utils.timezone

# Create your models here.
class Batalla(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.CharField(max_length=40)
    lugar = models.CharField(max_length=100)
    beligerantes = models.CharField(max_length=200)
    resultado = models.CharField(max_length=100, default='Valor predeterminado')
    imagen = models.ImageField(upload_to = 'battles')
    created = models.DateTimeField(default=django.utils.timezone.now)
    updated = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.nombre


class EjercitoVencedor(models.Model):
    titulo = models.CharField(max_length=50, default='Valor predeterminado')
    batalla = models.ForeignKey(Batalla, on_delete=models.CASCADE, default=None)
    comandantes = models.CharField(max_length=200)
    fuerzas_combate = models.CharField(max_length=100)
    infanteria = models.CharField(max_length=100, blank=True)
    caballeria = models.CharField(max_length=100, blank=True)
    proyectiles = models.CharField(max_length=100, blank=True)
    tropas_elite = models.CharField(max_length=100, blank=True)
    mercenarios = models.CharField(max_length=100, blank=True)
    asedio = models.CharField(max_length=100, blank=True)
    criaturas = models.CharField(max_length=100, blank=True)
    bajas = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class EjercitoVencido(models.Model):
    titulo = models.CharField(max_length=50, default='Valor predeterminado')
    batalla = models.ForeignKey(Batalla, on_delete=models.CASCADE, default=None)
    comandantes = models.CharField(max_length=200)
    fuerzas_combate = models.CharField(max_length=100)
    infanteria = models.CharField(max_length=100, blank=True)
    caballeria = models.CharField(max_length=100, blank=True)
    proyectiles = models.CharField(max_length=100, blank=True)
    tropas_elite = models.CharField(max_length=100, blank=True)
    mercenarios = models.CharField(max_length=100, blank=True)
    asedio = models.CharField(max_length=100, blank=True)
    criaturas = models.CharField(max_length=100, blank=True)
    bajas = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
