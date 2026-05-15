from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def is_autor(user):
    return user.groups.filter(name="autores").exists()

def artigos_view(request):

    artigos = Artigo.objects.all()

    return render(request, "artigos/artigos.html", {"artigos":artigos, "autor":is_autor(request.user)})


@login_required
def novo_artigo_view(request):

    form = ArtigoForm(request.POST or None, request.FILES)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect("artigos")

    return render(request, "artigos/novo_artigo.html", {"form":form})


@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)

        if form.is_valid():
            form.save()
            return redirect("artigos")
    else:
        form = ArtigoForm(instance = artigo)

        context = {"form":form, "artigo":artigo}
        return render(request, "artigos/edita_artigo.html", context)
    

@login_required
def apaga_artigo_view(request, artigo_id):

    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect("artigos")