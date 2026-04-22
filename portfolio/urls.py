from django.urls import path
from . import views


urlpatterns = [
    path('licenciaturas/', views.licenciatura_view, name="licenciaturas"),
    path("ucs", views.uc_view, name="ucs")
]