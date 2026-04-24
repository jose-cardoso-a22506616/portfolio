from django.urls import path
from . import views


urlpatterns = [
    path('', views.licenciatura_view),
    path('licenciaturas/', views.licenciatura_view, name="licenciaturas"),
    path("uc/<int:id>", views.uc_view, name="uc"),
    path("projetos/", views.projeto_view, name="projetos"),
    path("tecnologias/", views.tecnologias_view, name="tecnologias"),
    path("docentes/<int:id>", views.docentes_view, name="docentes"),
    path("competencias/", views.competencias_view, name="competencias"),
    path("formacoes/", views.formacoes_view, name="formacoes"),
    path("tfcs/", views.tfcs_view, name="tfcs"),
    path("makingof/", views.makingof_view, name="makingof"),
]