from django.shortcuts import render, redirect
from .models import Licenciatura, UC, Projeto, Tecnologia, Docente, Competencia, Formacao, Tfc, MakingOf
from .forms import ProjetoForm

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


def tfcs_view(request):

    tfcs = Tfc.objects.all()

    return render(request, "portfolio/tfcs.html", {"tfcs":tfcs})


def makingof_view(request):
    
    makingofs = MakingOf.objects.all()

    return render(request, "portfolio/makingof.html", {"makingofs":makingofs})



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