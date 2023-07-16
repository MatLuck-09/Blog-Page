from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserEditForm, ChangePasswordForm, AvatarForm
from django.contrib.auth import update_session_auth_hash
from .models import Avatar
from django.contrib import messages
from .forms import InfoPersonalForm
from .models import InfoPersonal

# Create your views here.
@login_required
def perfilview(request):
    avatar = getAvatar(request)
    usuario = request.user
    informacion_personal = InfoPersonal.objects.filter(user=usuario).first()

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'perfil/perfil.html', {'form': form, 'informacion_personal': informacion_personal, 'avatar': avatar})


@login_required
def editarPerfil(request):
    avatar = getAvatar(request)
    usuario = request.user
    user_basic_info = User.objects.get(id=usuario.id)

    try:
        info_personal = InfoPersonal.objects.get(user=usuario)
    except InfoPersonal.DoesNotExist:
        info_personal = None

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        info_personal_form = InfoPersonalForm(request.POST, instance=info_personal)

        if form.is_valid() and info_personal_form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()

            info_personal = info_personal_form.save(commit=False)
            info_personal.user = usuario
            info_personal.save()

            return redirect('/perfil')
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        info_personal_form = InfoPersonalForm(instance=info_personal)

    return render(request, 'perfil/editar.html', {'form': form, 'info_personal_form': info_personal_form, 'avatar': avatar})



@login_required
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=usuario)
        if form.is_valid():
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            if new_password1 == new_password2:
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('Home')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
        else:
            messages.error(request, 'Ha ocurrido un error al cambiar la contraseña. Por favor, revisa los datos ingresados.')

    else:
        form = ChangePasswordForm(user=usuario)

    return render(request, "perfil/changePassword.html", {"form": form})
    
@login_required
def editAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'HistoryBattlesApp/home.html',{'avatar':avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, 'perfil/avatar.html', {'form': form})

def getAvatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar

