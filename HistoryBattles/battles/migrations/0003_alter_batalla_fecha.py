# Generated by Django 4.1.5 on 2023-06-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0002_alter_batalla_fecha_alter_batalla_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batalla',
            name='fecha',
            field=models.CharField(max_length=40),
        ),
    ]