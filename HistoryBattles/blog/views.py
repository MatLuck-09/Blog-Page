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
        form = RecomendacionForm(request.POST, request.FILES)
        if form.is_valid():
            recomendacion = form.save(commit=False)
            recomendacion.usuario = request.user
            recomendacion.save()
            return redirect('Blog')
    else:
        form = RecomendacionForm()
    recomendaciones = Recomendacion.objects.all()
    return render(request, 'blog/blog.html', {'form': form, 'recomendaciones': recomendaciones, "avatar":avatar})


def recomendacion_view(request):
    recomendaciones = Recomendacion.objects.all()

    return render(request, 'blog/blog.html', {'recomendaciones': recomendaciones})