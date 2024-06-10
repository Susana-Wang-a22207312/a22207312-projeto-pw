from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Autor, Artigo, Comentario, Rating
from .forms import AutorForm, ArtigoForm, ComentarioForm, RatingForm

def index_view(request):
    context = {
        'artigos': Artigo.objects.all().order_by('titulo'),
        'autores': Autor.objects.all().order_by('nome'),
    }
    return render(request, "artigos/index.html", context)

def artigo_view(request, artigo_nome):
    context = {
        'artigo': Artigo.objects.get(titulo=artigo_nome),
    }
    return render(request, "artigos/artigo.html", context)

def autor_view(request, autor_nome):
    context = {
        'autor': Autor.objects.get(nome=autor_nome),
    }
    return render(request, "artigos/autor.html", context)

@login_required
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos:artigo', artigo_id=artigo.id)

    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('index')

@login_required
def novo_autor_view(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)

@login_required
def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form, 'autor': autor}
    return render(request, 'artigos/edita_autor.html', context)

@login_required
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('index')

@login_required
def novo_comentario_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        comentario.save()
        return redirect('index')

    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/novo_comentario.html', context)

@login_required
def edita_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    form = ComentarioForm(request.POST or None, instance=comentario)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form, 'comentario': comentario}
    return render(request, 'artigos/edita_comentario.html', context)

@login_required
def apaga_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('index')

@login_required
def novo_rating_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    form = RatingForm(request.POST or None)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.artigo = artigo
        rating.save()
        return redirect('index')

    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/novo_rating.html', context)

@login_required
def edita_rating_view(request, rating_id):
    rating = Rating.objects.get(id=rating_id)
    form = RatingForm(request.POST or None, instance=rating)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form, 'rating': rating}
    return render(request, 'artigos/edita_rating.html', context)

@login_required
def apaga_rating_view(request, rating_id):
    rating = Rating.objects.get(id=rating_id)
    rating.delete()
    return redirect('index')
