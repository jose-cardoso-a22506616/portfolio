from django.urls import path
from . import views

urlpatterns = [
    path("", views.artigos_view, name="artigos"),
    path("novo/", views.novo_artigo_view, name="novo_artigo"),
    path("edita/<int:artigo_id>", views.edita_artigo_view, name="edita_artigo"),
    path("apaga/<int:artigo_id>", views.apaga_artigo_view, name="apaga_artigo"),
    path("like/<int:artigo_id>", views.like, name="like"),
    path("comentar/<int:artigo_id>", views.comentar_artigo, name="comentar_artigo"),
    path("edita/comentario/<int:comentario_id>", views.editar_comentario, name="edita_comentario"),
    path("apaga/comentario/<int:comentario_id>", views.apagar_comentario, name="apaga_comentario"),
]