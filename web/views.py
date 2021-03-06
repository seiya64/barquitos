# coding: utf-8
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from servidor.models import PeticionPartida, UsuarioBarquitos, Partida
from django.contrib.auth.models import User
from web.forms import NuevaPartidaForm

import requests

from utils.decorators import render_with, ajax_request

@render_with('base.html')
def home(request):
    return {'titulo': 'Home de los barquitos'}

@render_with('web/nuevo_usuario.html')
def nuevo_usuario(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usu = form.save()
            usuario = UsuarioBarquitos()
            usuario.user = usu
            usuario.save()
            return HttpResponseRedirect(reverse('auth_login'))
    else:
        form = UserCreationForm()
    
    return {'titulo': 'Nuevo Usuario', 'form': form}
    
@login_required
@render_with('web/peticiones.html')
def peticiones(request):
    peticiones = PeticionPartida.objects.filter(oponente=request.user).order_by('-id')
    peticiones_eviadas = PeticionPartida.objects.filter(usuario=request.user).order_by('-id')
    return {'titulo': 'Peticiones', 'peticiones': peticiones, 'peticiones_enviadas':peticiones_eviadas}

@login_required
@render_with('web/nueva_partida.html')
def nueva_partida(request):
    
    form = NuevaPartidaForm()
        
    return {'titulo': 'Nueva partida', 'form': form}

@login_required
@render_with('web/partidas_empezadas.html')
def partidas_empezadas(request):
    partidas_mias = Partida.objects.filter(usuario=request.user)
    partidas_otros = Partida.objects.filter(oponente=request.user)
    return {'titulo': 'Partidas en curso','partidas1':partidas_mias,'partidas2':partidas_otros,}

@login_required
@render_with('web/partida.html')
def partida(request, partida):
    try:
        par = Partida.objects.get(id=partida)
        jugador = 0
        if par in Partida.objects.filter(usuario=request.user):
            jugador = 1
        elif par in Partida.objects.filter(oponente=request.user):
            jugador = 2
        
        if jugador != 0:
            return {'partida':par, 'jugador':jugador}
        else:
            raise Http404
    except:
        raise Http404

@render_with('web/clasificacion.html')
def clasificacion(request):
    usuarios = UsuarioBarquitos.objects.filter(puntuacion__gt=0).order_by('-puntuacion')
    return {'titulo': 'Clasificación','usuarios':usuarios,}
