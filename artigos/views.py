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

    if request.user != artigo.autor:
        return redirect("artigos")

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

    if request.user != artigo.autor:
        return redirect("artigos")
    
    artigo.delete()
    return redirect("artigos")


@login_required
def like(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)

    return redirect("artigos")


@login_required
def comentar_artigo(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    comentarios = artigo.comentarios.all()

    form = ComentarioForm()

    if request.POST:
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)

            if form.is_valid():
                comentario = form.save(commit=False)

                comentario.artigo = artigo
                comentario.autor = request.user

                comentario.save()

                return redirect("artigos")
            
    context = {"artigo":artigo, "comentarios": comentarios, "form":form}

    return render(request, "artigos/comentar_artigo.html", context)


@login_required
def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)

    if request.user != comentario.autor:
        return redirect("artigos")

    if request.POST:
        form = ComentarioForm(request.POST or None, request.FILES, instance = comentario)

        if form.is_valid():
            form.save()
            return redirect("artigos")
    else:
        form = ComentarioForm(instance=comentario)

        context = {"form":form, "comentario":comentario}
        return render(request, "artigos/edita_comentario.html", context)


@login_required
def apagar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)

    if request.user != comentario.autor:
        return redirect("artigos")

    comentario.delete()
    return redirect("artigos")