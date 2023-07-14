from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

<<<<<<< HEAD
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

=======
>>>>>>> c2415f5749d574ffd48becf5b61d1308080324ba
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
<<<<<<< HEAD
        related_name='customuser_set'
=======
        related_name='customuser_set'  # Agrega el atributo related_name
>>>>>>> c2415f5749d574ffd48becf5b61d1308080324ba
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
<<<<<<< HEAD
        related_name='customuser_set'
    )

    def __str__(self):
        return self.username
=======
        related_name='customuser_set'  # Agrega el atributo related_name
    )

    def __str__(self):
        return self.username
>>>>>>> c2415f5749d574ffd48becf5b61d1308080324ba
