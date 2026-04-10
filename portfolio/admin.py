from django.contrib import admin
from .models import *

# Register your models here.
class UCAdmmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "semestre")
    ordering = ("nome",)
    search_fields = ("nome",)

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "curso_codigo", "semestres", "curso_ects")
    ordering = ("nome", "curso_codigo")
    search_fields = ("nome", "curso_codigo")

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "employee_code","email", "degree", "regime")
    ordering = ("nome", "employee_code")
    search_fields = ("nome", "employee_code", "email")

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

class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "descricao", "data")
    ordering = ("tipo",)
    search_fields = ("tipo",)

class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    ordering = ("id",)
    search_fields = ("id", "titulo",)

class TfcsAdmin(admin.ModelAdmin):
    list_display = ("titulo", "aluno", "orientador")
    ordering = ("titulo",)
    search_fields = ("titulo",)


admin.site.register(UC, UCAdmmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(MakingOf, MakingOfAdmin)
admin.site.register(Tfc, TfcsAdmin)