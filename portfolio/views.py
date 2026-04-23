from django.shortcuts import render
from .models import Licenciatura, UC

# Create your views here.
def licenciatura_view(request):

    licenciaturas = Licenciatura.objects.prefetch_related("uc").all()

    return render(request, "portfolio/licenciatura.html", {"licenciaturas":licenciaturas})


def uc_view(request):

    ucs = UC.objects.select_related("projeto").prefetch_related("docente")
    

    return render(request, "portfolio/uc.html", {"ucs":ucs})