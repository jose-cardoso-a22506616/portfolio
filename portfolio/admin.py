from django.contrib import admin
from .models import *

# Register your models here.
class UCAdmmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "semestre")
    ordering = ("nome",)
    search_fields = ("nome",)

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    ordering = ("nome",)
    search_fields = ("nome",)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "mail", "site")
    ordering = ("nome",)
    search_fields = ("nome",)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "site_oficial")
    ordering = ("nome",)
    search_fields = ("nome",)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao", "repositorio")
    ordering = ("nome",)
    search_fields = ("nome",)

class CompetenciaAdmin(admin.ModelAdmin):
    list_display =("tipo", "descricao")
    ordering = ("tipo",)
    search_fields =("tipo",)

admin.site.register(UC, UCAdmmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Competencia, CompetenciaAdmin)