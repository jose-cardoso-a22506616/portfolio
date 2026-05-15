from django.urls import path
from . import views

urlpatterns = [
    path("", views.artigos_view, name="artigos"),
    path("novo/", views.novo_artigo_view, name="novo_artigo"),
    path("edita/<int:artigo_id>", views.edita_artigo_view, name="edita_artigo"),
    path("apaga/<int:artigo_id>", views.apaga_artigo_view, name="apaga_artigo"),
]