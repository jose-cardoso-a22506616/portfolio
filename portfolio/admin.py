from django.contrib import admin
from .models import *

# Register your models here.
class UCAdmmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    ordering = ("nome",)
    search_fields = ("nome",)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(UC, UCAdmmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)