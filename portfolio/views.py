from django.shortcuts import render
from .models import Licenciatura, UC, Projeto, Tecnologia

# Create your views here.
def licenciatura_view(request):

    licenciaturas = Licenciatura.objects.prefetch_related("uc").all()

    return render(request, "portfolio/licenciatura.html", {"licenciaturas":licenciaturas})


def uc_view(request, id):

    uc = UC.objects.get(id=id)
    

    return render(request, "portfolio/uc.html", {"uc":uc})


def projeto_view(request):

    projetos = Projeto.objects.prefetch_related("tecnologia")

    return render(request, "portfolio/projetos.html", {"projetos":projetos})


def tecnologias_view(request):

    tecnologias = Tecnologia.objects.prefetch_related("formacao")

    return render(request, "portfolio/tecnologias.html", {"tecnologias":tecnologias})