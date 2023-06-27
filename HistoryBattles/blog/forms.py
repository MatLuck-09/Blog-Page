from  django import forms

class RequestForms(forms.Form):
    nombre = forms.CharField(label='Nombre de la batalla', max_length=50)