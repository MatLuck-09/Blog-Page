from django import forms
from .models import Recomendacion

class RequestForms(forms.Form):
    nombre = forms.CharField(label='Nombre de la batalla', max_length=50)

class RecomendacionForm(forms.ModelForm):
    class Meta:
        model = Recomendacion
        fields = ['contenido']
    
