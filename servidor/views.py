# coding: utf-8
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import requests
import random

from utils.decorators import render_with, ajax_request
from servidor.models import PeticionPartida, Partida, UsuarioBarquitos

TABLERO_ALEATORIO = []
#TABLERO_ALEATORIO.append('1101001111 0001000000 1001011101 1000000001 1000000000 1000010001 0000010001 1100000001 0000000000 0000011111')
#TABLERO_ALEATORIO.append('0010111101 0010000001 0000000000 0000000111 0000000000 1001100100 1000000101 1000000101 1000000001 1011101101')

TABLERO_ALEATORIO.append('0000000000000000000000000000010111110001010000000101000000010100000001000000000101100000010000000000')
TABLERO_ALEATORIO.append('0000001000000000100000001110000000001000000000000000011111000000000000000000000000000000001110011100')
TABLERO_ALEATORIO.append('0000000000000000000000000000000000000000011100000100000000011111000101000000010100000000010000011100')
TABLERO_ALEATORIO.append('0000000001000000000100000000011000000001101111100000000001000000000100000000010000111000000000000000')
TABLERO_ALEATORIO.append('0000000000000111100000010010000001001000000000100000000000000000011100000000000001111100000000000000')
TABLERO_ALEATORIO.append('0000000000011100000000000000000000000000000000000000000000000111101000000000100011111111000000000000')
TABLERO_ALEATORIO.append('0000000000111000000000100000000010000000001000000000101111000000000100111000010000000001000000000000')
TABLERO_ALEATORIO.append('0000011100000000000000001110100000000010001111100000000000000000000000000000000000001111000000000000')
TABLERO_ALEATORIO.append('0010000000001000000011100000000000000000000111000000000000001111000000000000000000000000000001111100')
TABLERO_ALEATORIO.append('0000100000000010000000001000001111000000000000000010101111101010000000001000000000000000000000000000')

TABLERO_ALEATORIO.append('0000000000000000000000000000010111110001010000000101000000010100000001000000000101100000010000000000'[::-1])
TABLERO_ALEATORIO.append('0000001000000000100000001110000000001000000000000000011111000000000000000000000000000000001110011100'[::-1])
TABLERO_ALEATORIO.append('0000000000000000000000000000000000000000011100000100000000011111000101000000010100000000010000011100'[::-1])
TABLERO_ALEATORIO.append('0000000001000000000100000000011000000001101111100000000001000000000100000000010000111000000000000000'[::-1])
TABLERO_ALEATORIO.append('0000000000000111100000010010000001001000000000100000000000000000011100000000000001111100000000000000'[::-1])
TABLERO_ALEATORIO.append('0000000000011100000000000000000000000000000000000000000000000111101000000000100011111111000000000000'[::-1])
TABLERO_ALEATORIO.append('0000000000111000000000100000000010000000001000000000101111000000000100111000010000000001000000000000'[::-1])
TABLERO_ALEATORIO.append('0000011100000000000000001110100000000010001111100000000000000000000000000000000000001111000000000000'[::-1])
TABLERO_ALEATORIO.append('0010000000001000000011100000000000000000000111000000000000001111000000000000000000000000000001111100'[::-1])
TABLERO_ALEATORIO.append('0000100000000010000000001000001111000000000000000010101111101010000000001000000000000000000000000000'[::-1])

@login_required
@csrf_exempt
@ajax_request
def tramitar_peticiones_partidas(request):
    
    resultado = []
    
    for respuesta in request.GET:
        peticion_partida = PeticionPartida.objects.filter(oponente=request.user, id=request.GET[respuesta])
        
        for pet in peticion_partida:
            if (respuesta == "Aceptar"):
                pet.estado = 1
                partida = Partida()
                partida.usuario = pet.usuario
                partida.oponente = pet.oponente
                partida.tablero1 = random.choice(TABLERO_ALEATORIO)
                partida.tablero2 = random.choice(TABLERO_ALEATORIO)
                partida.turno = 1
                partida.save()

            elif (respuesta == "Rechazar"):
                pet.estado = 2

            pet.save()
            resultado.append((
                pet.usuario.user.username,
                pet.get_estado(),
            ))

    return resultado

@login_required
@csrf_exempt
@ajax_request
def peticion_nueva_partida(request):
    
    resultado = []
    respuesta = "NO"
    
    if request.method == 'POST':
        
        peticion_en_espera = False
        mismo_usuario = False
        hay_partida = False
        
        pet_partida_aux = PeticionPartida.objects.filter(usuario = request.user, oponente = request.POST["oponente"])
        for pet in pet_partida_aux:
            if pet.estado == 0:
                peticion_en_espera = True
                respuesta = u'Ya existe una petición'
        
        if not peticion_en_espera:
            pet_partida_aux2 = PeticionPartida.objects.filter(oponente = request.user, usuario = request.POST["oponente"])
            for pet in pet_partida_aux2:
                if pet.estado == 0:
                    peticion_en_espera = True
                    respuesta = u'Ya existe una petición'
        
        if str(request.user.id) == request.POST["oponente"]:
            mismo_usuario = True
            respuesta = "No te puedes retar a ti mismo"
        
        partida_aux = Partida.objects.filter(usuario = request.user, oponente = request.POST["oponente"])
        partida_aux2 = Partida.objects.filter(oponente = request.user, usuario = request.POST["oponente"])
        
        if len(partida_aux) > 0 or len(partida_aux2) > 0:
            hay_partida = True
            respuesta = "Ya existe una partida entre vosotros"
        
        if not (hay_partida or peticion_en_espera or mismo_usuario):
            pet_partida = PeticionPartida()
            pet_partida.usuario = UsuarioBarquitos.objects.filter(user=request.user)[0]
            pet_partida.oponente = UsuarioBarquitos.objects.filter(user=request.POST["oponente"])[0]
            
            if not peticion_en_espera:
                pet_partida_aux = PeticionPartida.objects.filter(oponente = request.user, usuario = request.POST["oponente"])
                for pet in pet_partida_aux:
                    if pet.estado == 1 or pet.estado == 2:
                        pet.delete()
                pet_partida_aux = PeticionPartida.objects.filter(usuario = request.user, oponente = request.POST["oponente"])
                for pet in pet_partida_aux:
                    if pet.estado == 1 or pet.estado == 2:
                        pet.delete()
            
            pet_partida.save()
            respuesta = u'Se ha enviado la petición'
        
        resultado.append(respuesta)

    return resultado

@login_required
@csrf_exempt
@ajax_request
def obtener_tableros(request, partida):
    par = Partida.objects.get(id=partida)
    tableros = []
    tablero_ataque = []
    tablero = []
    
    jugador = 0
    if par in Partida.objects.filter(usuario=request.user):
        jugador = 1
        
        if par.tablero1.find('1')<0:
            tableros.append('pierdes')
            usuario = par.usuario
            usuario.perdidas += 1
            usuario.save()
            oponente = par.oponente
            oponente.ganadas += 1
            oponente.save()
            par.delete()
            return tableros
        elif par.tablero2.find('1')<0:
            tableros.append('ganas')
            usuario = par.usuario
            usuario.ganadas += 1
            usuario.save()
            oponente = par.oponente
            oponente.perdidas += 1
            oponente.save()
            par.delete()
            return tableros
        
    elif par in Partida.objects.filter(oponente=request.user):
        jugador = 2
        
        if par.tablero2.find('1')<0:
            tableros.append('pierdes')
            usuario = par.usuario
            usuario.ganadas += 1
            usuario.save()
            oponente = par.oponente
            oponente.perdidas += 1
            oponente.save()
            par.delete()
            return tableros
        elif par.tablero1.find('1')<0:
            tableros.append('ganas')
            usuario = par.usuario
            usuario.perdidas += 1
            usuario.save()
            oponente = par.oponente
            oponente.ganadas += 1
            oponente.save()
            par.delete()
            return tableros
    
    if jugador == 1:
        for casilla in par.tablero1_ataque:
            tablero_ataque.append(casilla)
        for casilla in par.tablero1:
            tablero.append(casilla)
    elif jugador == 2:
        for casilla in par.tablero2_ataque:
            tablero_ataque.append(casilla)
        for casilla in par.tablero2:
            tablero.append(casilla)
    
    tableros.append(tablero_ataque)
    tableros.append(tablero)
    if par.turno == jugador-1:
        tableros.append('turno')
    
    return tableros

@login_required
@csrf_exempt
@ajax_request
def atacar(request,partida):
    par = Partida.objects.get(id=partida)
    respuesta = []
    
    if request.method == 'POST':
        x = int(request.GET["x"])
        y = int(request.GET["y"])
        pos = x*10 + y
        
        jugador = 0
        if par in Partida.objects.filter(usuario=request.user):
            jugador = 1
            if par.turno != jugador-1:
                respuesta.append('no es tu turno')
                return respuesta
            #si el otro tiene mar, me pongo agua
            if par.tablero2[pos] == '0':
                
                lista = list(par.tablero2)
                lista[pos] = '3';
                par.tablero2 = "".join(lista)
                
                lista = list(par.tablero1_ataque)
                lista[pos] = '3';
                par.tablero1_ataque = "".join(lista)
                
                par.turno = 1
                par.save()
                respuesta.append('ok')
            #si el otro tiene barco, me pongo tocado
            elif par.tablero2[pos] == '1':
                
                lista = list(par.tablero2)
                lista[pos] = '2';
                par.tablero2 = "".join(lista)
                
                lista = list(par.tablero1_ataque)
                lista[pos] = '2';
                par.tablero1_ataque = "".join(lista)
                
                par.turno = 1
                par.save()
                
                usuario = par.usuario
                usuario.puntuacion += 1
                usuario.save()
                
                respuesta.append('ok')
            else:
                respuesta.append('no')
            
        elif par in Partida.objects.filter(oponente=request.user):
            jugador = 2
            if par.turno != jugador-1:
                respuesta.append('no es tu turno')
                return respuesta
            #si el otro tiene mar, me pongo agua
            if par.tablero1[pos] == '0':
                
                lista = list(par.tablero1)
                lista[pos] = '3';
                par.tablero1 = "".join(lista)
                
                lista = list(par.tablero2_ataque)
                lista[pos] = '3';
                par.tablero2_ataque = "".join(lista)
                
                par.turno = 0
                par.save()
                respuesta.append('ok')
            #si el otro tiene barco, me pongo tocado
            elif par.tablero1[pos] == '1':
                
                lista = list(par.tablero1)
                lista[pos] = '2';
                par.tablero1 = "".join(lista)
                
                lista = list(par.tablero2_ataque)
                lista[pos] = '2';
                par.tablero2_ataque = "".join(lista)
                
                par.turno = 0
                par.save()
                
                usuario = par.oponente
                usuario.puntuacion += 1
                usuario.save()
                
                respuesta.append('ok')
            else:
                respuesta.append('no')
        
    return respuesta

@login_required
@csrf_exempt
@ajax_request
def abandonar(request,partida):
    par = Partida.objects.get(id=partida)
    respuesta = []
    jugador = 0
    if par in Partida.objects.filter(usuario=request.user):
        usuario = par.usuario
        usuario.ganadas += 1
        oponente = par.oponente
        oponente.perdidas += 1
        par.delete()
        respuesta.append("ok")
    elif par in Partida.objects.filter(oponente=request.user):
        usuario = par.oponente
        usuario.ganadas += 1
        oponente = par.usuario
        oponente.perdidas += 1
        par.delete()
        respuesta.append("ok")
    return respuesta
