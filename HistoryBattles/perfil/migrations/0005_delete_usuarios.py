# Generated by Django 4.1.5 on 2023-07-13 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_remove_usuarios_descripcion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
