from django.contrib import admin
from .models import *

# Register your models here.
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("autor", "data_criacao")
    ordering = ("autor",)
    search_fields = ("autor",)

class ComentarioAdmin(admin.ModelAdmin):
    list_display=("artigo", "autor", "data_criacao")
    ordering=("artigo", "autor")
    search_fields=("artigo","autor")

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)