from django.shortcuts import render, redirect
from .forms import RequestForms
from battles.models import Batalla
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from perfil.views import getAvatar
from .models import Recomendacion
from .forms import RecomendacionForm


# Create your views here.
@login_required
def blog(request):
    avatar = getAvatar(request)
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            recomendacion_id = request.POST.get('eliminar')
            recomendacion = Recomendacion.objects.get(id=recomendacion_id)
            if recomendacion.usuario == request.user:
                recomendacion.delete()
                messages.success(request, 'La recomendación se eliminó correctamente.')
            else:
                messages.error(request, 'No tienes permiso para eliminar esta recomendación.')
            return redirect('Blog')
        else:
            form = RecomendacionForm(request.POST, request.FILES)
            if form.is_valid():
                recomendacion = form.save(commit=False)
                recomendacion.usuario = request.user
                recomendacion.save()
                messages.success(request, 'La recomendación se creó correctamente.')
                return redirect('Blog')
    else:
        form = RecomendacionForm()
    recomendaciones = Recomendacion.objects.all()
    return render(request, 'blog/blog.html', {'form': form, 'recomendaciones': recomendaciones, 'avatar': avatar})


@login_required
def editar(request, recomendacion_id):
    recomendacion = Recomendacion.objects.get(id = recomendacion_id)
    form = RecomendacionForm(instance= recomendacion)
    if request.method == "POST":
        form = RecomendacionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(recomendacion.contenido)
            recomendacion.usuario = data['usuario']
            recomendacion.contenido = data['contenido']
            recomendacion.save()
            messages.success(request, 'La recomendación se actualizó correctamente.')
            return redirect('Blog')


    return render(request, 'blog/editar.html', {'form': form, 'recomendacion': recomendacion})

@login_required
def recomendacion_view(request):
    recomendaciones = Recomendacion.objects.all()

    return render(request, 'blog/blog.html', {'recomendaciones': recomendaciones})
