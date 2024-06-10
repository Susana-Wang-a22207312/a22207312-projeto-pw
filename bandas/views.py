from django.shortcuts import render, redirect
from .models import Banda, Album,Musica,Membro
from django.contrib.auth.decorators import login_required
from .forms import BandaForm, AlbumForm, MusicaForm

def index_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome'),
    }
    return render(request, "bandas/index.html",context)


def bandas_view(request, banda_id):
    context = {
      'banda': Banda.objects.get(id=banda_id),
   }
    return render(request, "bandas/bandas.html",context)

def album_view(request, album_nome):
    context = {
      'album': Album.objects.get(titulo=album_nome),
   }
    return render(request, "bandas/album.html", context)

def musica_view(request,musica_nome):
    context = {
      'musica': Musica.objects.get(titulo=musica_nome),
   }
    return render(request, "bandas/musica.html",context)

def membro_view(request, membro_nome):
    context = {
      'membro': Membro.objects.get(nome=membro_nome),
   }
    return render(request, "bandas/membro.html",context)

@login_required
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    form = BandaForm(request.POST or None, request.FILES or None, instance=banda)
    if form.is_valid():
        form.save()
        return redirect('bandas:banda', banda_id=banda.id)

    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('index')

@login_required
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.banda = banda
        album.save()
        return redirect('index')

    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/novo_album.html', context)

@login_required
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    form = AlbumForm(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form, 'album': album}
    return render(request, 'bandas/edita_album.html', context)

@login_required
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('index')

@login_required
def nova_musica_view(request, album_id):
    album = Album.objects.get(id=album_id)
    form = MusicaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        musica = form.save(commit=False)
        musica.album = album
        musica.save()
        return redirect('index')

    context = {'form': form, 'album': album}
    return render(request, 'bandas/nova_musica.html', context)

@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    form = MusicaForm(request.POST or None, request.FILES or None, instance=musica)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form, 'musica': musica}
    return render(request, 'bandas/edita_musica.html', context)

@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('index')