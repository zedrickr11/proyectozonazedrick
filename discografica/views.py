from django.shortcuts import render, get_object_or_404, redirect, render_to_response

#librería para manejar el envío de mensajes
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from .forms import CancionForm, GeneroForm, ArtistaForm, AlbumForm, VocalistaForm
from discografica.models import Cancion, Vocalista, Participacion, Genero, Artista, Album
from django.contrib.auth.decorators import login_required
# Create your views here.

def frontend(request):
    return render(request,'registration/login.html')

@login_required
def index_genero(request):
    gen = Genero.objects.all()
    return render(request, 'discografica/index_genero.html', {'gen': gen})

@login_required
def genero_new(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid():
            genero = form.save(commit=False)
            genero.save()
            return redirect('index_genero')

    else:
        form = GeneroForm()
        return render(request, 'discografica/genero_edit.html', {'form': form})

@login_required
def genero_edit(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == "POST":
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            genero = form.save(commit=False)
            genero.save()
            return redirect('index_genero')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'discografica/genero_edit.html', {'form': form})

@login_required
def genero_show(request, pk):
    gen = get_object_or_404(Genero, pk=pk)
    return render(request, 'discografica/genero_show.html', {'g': gen})

@login_required
def genero_remove(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    genero.delete()
    return redirect('index_genero')

#===============================Artista=================================
@login_required
def artista_index(request):
    art = Artista.objects.all()
    return render(request, 'discografica/artista_index.html', {'art': art})

@login_required
def artista_new(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            artista = form.save(commit=False)
            artista.save()
            return redirect('artista_index')

    else:
        form = ArtistaForm()
        return render(request, 'discografica/artista_edit.html', {'form': form})

@login_required
def artista_edit(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == "POST":
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            artista = form.save(commit=False)
            artista.save()
            return redirect('artista_index')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'discografica/artista_edit.html', {'form': form})

@login_required
def artista_show(request, pk):
    art = get_object_or_404(Artista, pk=pk)
    return render(request, 'discografica/artista_show.html', {'a': art})

@login_required
def artista_remove(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    artista.delete()
    return redirect('artista_index')

#===============================Album=================================
@login_required
def album_index(request):
    alb = Album.objects.all()
    return render(request, 'discografica/album_index.html', {'alb': alb})

@login_required
def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.autor = request.user
            album.fecha_creacion = timezone.now()
            album.save()
            return redirect('album_index')

    else:
        form = AlbumForm()
        return render(request, 'discografica/album_edit.html', {'form': form})

@login_required
def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.autor = request.user
            album.save()
            return redirect('album_index')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'discografica/album_edit.html', {'form': form})

@login_required
def album_show(request, pk):
    alb = get_object_or_404(Album, pk=pk)
    return render(request, 'discografica/album_show.html', {'a': alb})

@login_required
def album_remove(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_index')

#===============================Cancion=================================
@login_required
def cancion_index(request):
    can = Cancion.objects.all()
    return render(request, 'discografica/cancion_index.html', {'can': can})

@login_required
def cancion_nueva(request):
    if request.method == "POST":
        formulario = CancionForm(request.POST)
        if formulario.is_valid():
            cancion = Cancion.objects.create(titulo=formulario.cleaned_data['titulo'], Album = formulario.cleaned_data['Album'], num_pista = formulario.cleaned_data['num_pista'], duracion = formulario.cleaned_data['duracion'], fecha_creacion = formulario.cleaned_data['fecha_creacion'])
            for Vocalista_id in request.POST.getlist('Vocalista'):
                participacion = Participacion(Vocalista_id=Vocalista_id, Cancion_id = cancion.id)
                participacion.save()
            return redirect('cancion_index')
    else:
        formulario = CancionForm()
    return render(request, 'discografica/cancion_editar.html', {'formulario': formulario})

@login_required
def cancion_edit(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        formulario = CancionForm(request.POST, instance=cancion)
        if formulario.is_valid():
            cancion = formulario.save(commit=False)
            cancion = Cancion.objects.create(titulo=formulario.cleaned_data['titulo'], Album = formulario.cleaned_data['Album'], num_pista = formulario.cleaned_data['num_pista'], duracion = formulario.cleaned_data['duracion'], fecha_creacion = formulario.cleaned_data['fecha_creacion'])
            for Vocalista_id in request.POST.getlist('Vocalista'):
                participacion = Participacion(Vocalista_id=Vocalista_id, Cancion_id = cancion.id)
                participacion.save()
            return redirect('cancion_index')
    else:
        formulario = CancionForm(instance=cancion)
    return render(request, 'discografica/cancion_editar.html', {'formulario': formulario})

@login_required
def cancion_show(request, pk):
    can = get_object_or_404(Cancion, pk=pk)
    return render(request, 'discografica/cancion_show.html', {'c': can})

@login_required
def cancion_remove(request, pk):
    album = get_object_or_404(Cancion, pk=pk)
    album.delete()
    return redirect('cancion_index')

#===============================Vocalista=================================
@login_required
def vocalista_index(request):
    voc = Vocalista.objects.all()
    return render(request, 'discografica/vocalista_index.html', {'voc': voc})

@login_required
def vocalista_new(request):
    if request.method == "POST":
        form = VocalistaForm(request.POST)
        if form.is_valid():
            vocalista = form.save(commit=False)
            vocalista.save()
            return redirect('vocalista_index')

    else:
        form = VocalistaForm()
        return render(request, 'discografica/vocalista_edit.html', {'form': form})

@login_required
def vocalista_edit(request, pk):
    vocalista = get_object_or_404(Vocalista, pk=pk)
    if request.method == "POST":
        form = VocalistaForm(request.POST, instance=vocalista)
        if form.is_valid():
            vocalista = form.save(commit=False)
            vocalista.save()
            return redirect('vocalista_index')
    else:
        form = VocalistaForm(instance=vocalista)
    return render(request, 'discografica/vocalista_edit.html', {'form': form})

@login_required
def vocalista_show(request, pk):
    voc = get_object_or_404(Vocalista, pk=pk)
    return render(request, 'discografica/vocalista_show.html', {'v': voc})

@login_required
def vocalista_remove(request, pk):
    vocalista = get_object_or_404(Vocalista, pk=pk)
    vocalista.delete()
    return redirect('vocalista_index')
