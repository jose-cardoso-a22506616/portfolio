from django.urls import path
from . import views


urlpatterns = [
    path('', views.licenciatura_view),
    path('licenciaturas/', views.licenciatura_view, name="licenciaturas"),
    path("ucs/", views.uc_view, name="ucs"),
    path("projetos/", views.projeto_view, name="projetos"),
]