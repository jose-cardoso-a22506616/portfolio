from django.urls import path
from . import views


urlpatterns = [
    path('', views.licenciatura_view),
    path('licenciaturas/', views.licenciatura_view, name="licenciaturas"),
    path("uc/<int:id>", views.uc_view, name="uc"),
    path("projetos/", views.projeto_view, name="projetos"),
]