from django.shortcuts import render
from .models import Licenciatura, UC, Projeto, Tecnologia, Docente, Competencia, Formacao

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


def docentes_view(request, id):

    licenciatura = Licenciatura.objects.get(id=id)
    ucs = licenciatura.uc.all()
    docentes = Docente.objects.filter(ucs__in = ucs)

    return render(request, "portfolio/docentes.html", {"licenciatura":licenciatura, "ucs":ucs, "docentes":docentes})


def competencias_view(request):

    competencias = Competencia.objects.all()

    return render(request, "portfolio/competencias.html", {"competencias":competencias})


def formacoes_view(request):

    formacoes = Formacao.objects.all()

    return render(request, "portfolio/formacoes.html", {"formacoes":formacoes})