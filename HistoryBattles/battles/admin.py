from django.contrib import admin
from .models import Batalla, EjercitoVencedor, EjercitoVencido

# Register your models here.

class BatallaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Batalla, BatallaAdmin)

admin.site.register(EjercitoVencedor)

admin.site.register(EjercitoVencido)

