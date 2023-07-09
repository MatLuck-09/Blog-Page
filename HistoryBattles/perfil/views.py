from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserEditForm, ChangePasswordForm, AvatarForm
from django.contrib.auth import update_session_auth_hash
from .models import Avatar

# Create your views here.
@login_required
def perfilview(request):
    return render(request, 'perfil/perfil.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'perfil/perfil.html')
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, 'perfil/editar.html', {'form': form})

@login_required
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las constraseñas no coinciden")
        return render(request, "HistoryBattlesApp/home.html")
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, "perfil/changePassword.html", {"form":form})
    
@login_required
def editAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
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
            avatar = Avatar.objets.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, 'perfil/avatar.html')

def getAvatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar