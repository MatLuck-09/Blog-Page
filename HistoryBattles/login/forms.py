from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')