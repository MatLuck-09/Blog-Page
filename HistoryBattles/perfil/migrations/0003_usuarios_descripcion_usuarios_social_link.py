# Generated by Django 4.1.5 on 2023-07-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='social_link',
            field=models.URLField(blank=True),
        ),
    ]
