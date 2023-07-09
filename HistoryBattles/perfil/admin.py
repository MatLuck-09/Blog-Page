from django.contrib import admin
from .models import Usuarios, Avatar

# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Usuarios, UsuariosAdmin)

admin.site.register(Avatar)