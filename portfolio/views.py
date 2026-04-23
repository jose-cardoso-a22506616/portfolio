from django.shortcuts import render
from .models import Licenciatura, UC, Projeto

# Create your views here.
def licenciatura_view(request):

    licenciaturas = Licenciatura.objects.prefetch_related("uc").all()

    return render(request, "portfolio/licenciatura.html", {"licenciaturas":licenciaturas})


def uc_view(request):

    ucs = UC.objects.prefetch_related("docente").select_related("projeto")
    

    return render(request, "portfolio/uc.html", {"ucs":ucs})


def projeto_view(request):

    projetos = Projeto.objects.prefetch_related("tecnologia")

    return render(request, "portfolio/projetos.html", {"projetos":projetos})
