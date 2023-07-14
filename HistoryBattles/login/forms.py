from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
<<<<<<< HEAD
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
=======
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
>>>>>>> c2415f5749d574ffd48becf5b61d1308080324ba
