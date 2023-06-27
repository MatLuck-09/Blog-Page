from django.shortcuts import render, redirect
from .forms import RequestForms
from battles.models import Batalla
from django.contrib import messages

# Create your views here.

def blog(request):
    if request.method == 'POST':
        form = RequestForms(request.POST)
        if form.is_valid():
            nombre_batalla = form.cleaned_data['nombre']
            try:
                batalla = Batalla.objects.get(nombre=nombre_batalla)
                messages.info(request, 'Esta batalla ya ha sido registrada.')
                return redirect('Batallas')
            except Batalla.DoesNotExist:
                error_msg = "No se encontró ninguna batalla con ese nombre."
                form.add_error('nombre', error_msg)
    else:
        form = RequestForms()
    return render(request, 'blog/blog.html', {'form': form})
