from django.contrib import admin

# Register your models here.
from coder.models import *

@admin.register(Abogados)
class AbogadosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "nro_abogado")
    list_display_links = ("nombre", "apellido")
    search_fields = ("nombre", "apellido", "nro_abogado")
    list_filter = ()
    ordering = ("apellido", "nombre")
    