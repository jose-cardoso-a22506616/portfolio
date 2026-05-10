from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.contrib.auth.models import Group
import os

def is_gestor(user):
    return user.groups.filter(name="gestor-portfolio").exists()
    
# VIEWS
def licenciatura_view(request):

    licenciaturas = Licenciatura.objects.prefetch_related("uc").all()

    return render(request, "portfolio/licenciatura.html", {"licenciaturas":licenciaturas})


def uc_view(request, id):

    uc = UC.objects.get(id=id)
    

    return render(request, "portfolio/uc.html", {"uc":uc})


def projeto_view(request):

    projetos = Projeto.objects.prefetch_related("tecnologia")

    return render(request, "portfolio/projetos.html", {"projetos":projetos, "gestor":is_gestor(request.user)})


def tecnologias_view(request):

    tecnologias = Tecnologia.objects.prefetch_related("formacao")

    return render(request, "portfolio/tecnologias.html", {"tecnologias":tecnologias, "gestor":is_gestor(request.user)})


def docentes_view(request, id):

    licenciatura = Licenciatura.objects.get(id=id)
    ucs = licenciatura.uc.all()
    docentes = Docente.objects.filter(ucs__in = ucs)

    return render(request, "portfolio/docentes.html", {"licenciatura":licenciatura, "ucs":ucs, "docentes":docentes})


def competencias_view(request):

    competencias = Competencia.objects.all()

    return render(request, "portfolio/competencias.html", {"competencias":competencias, "gestor":is_gestor(request.user)})


def formacoes_view(request):

    formacoes = Formacao.objects.all()

    return render(request, "portfolio/formacoes.html", {"formacoes":formacoes, "gestor":is_gestor(request.user)})


def tfcs_view(request):

    tfcs = Tfc.objects.all()

    return render(request, "portfolio/tfcs.html", {"tfcs":tfcs})


def makingof_view(request):
    
    makingofs = MakingOf.objects.all()

    return render(request, "portfolio/makingof.html", {"makingofs":makingofs})


def about_view(request):
    tecnologias = Tecnologia.objects.all()
    makingofs = MakingOf.objects.all()

    path = os.path.join(settings.BASE_DIR, "portfolio/static/portfolio/about/mvt.md")

    with open(path, "r", encoding="utf-8") as f:
        mvt = f.read()

    context = {"tecnologias":tecnologias, "makingofs":makingofs, "mvt":mvt}

    return render(request, "portfolio/about.html", context)



# CRUD

def novo_projeto_view(request):

    form = ProjetoForm(request.POST or None, request.FILES)
    
    if form.is_valid():
        form.save()
        return redirect('projetos')

    return render(request, "portfolio/novo_projeto.html", {"form":form})


def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect("projetos")
    else:
        form = ProjetoForm(instance = projeto)

        context = {"form":form, "projeto":projeto}
        return render(request, "portfolio/edita_projeto.html", context)
    

def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect("projetos")


def novo_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return redirect("tecnologias")
    
    return render(request, "portfolio/novo_tecnologia.html", {"form":form})


def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)

    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect("tecnologias")
    else:
        form = TecnologiaForm(instance=tecnologia)

    context = {"form":form, "tecnologia":tecnologia}
    return render(request, "portfolio/edita_tecnologia.html", context)


def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    tecnologia.delete()
    return redirect("tecnologias")


def novo_competencia_view(request):
    form = CompetenciaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("competencias")
    
    return render(request, "portfolio/novo_competencia.html", {"form":form})


def edita_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)

    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)

        if form.is_valid():
            form.save()
            return redirect("competencias")
    else:
        form = CompetenciaForm(instance=competencia)

    context = {"form":form, "competencia":competencia}
    return render(request, "portfolio/edita_competencia.html", context)


def apaga_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)
    competencia.delete()
    return redirect("competencias")


def novo_formacao_view(request):
    form = FormacaoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("formacoes")
    
    return render(request, "portfolio/novo_formacao.html", {"form":form})


def edita_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)

    if request.POST:
        form = FormacaoForm(request.POST or None, request.FILES, instance=formacao)

        if form.is_valid():
            form.save()
            return redirect("formacoes")
    else:
        form = FormacaoForm(instance=formacao)

    context = {"form":form, "formacao":formacao}
    return render(request, "portfolio/edita_formacao.html", context)


def apaga_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)
    formacao.delete()
    return redirect("formacoes")