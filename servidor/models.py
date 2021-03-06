from django.db import models
from django.contrib.auth.models import User

ROL = (
    (0, 'Administrador'),
    (1, 'Usuario'),
)

TABLERO_VACIO = "0"*100

class UsuarioBarquitos(models.Model):
    user = models.ForeignKey(User, unique=True)
    puntuacion = models.IntegerField(default=0)
    rol = models.IntegerField(choices=ROL, default=1)
    desde = models.DateTimeField(auto_now_add=True)
    ganadas = models.IntegerField(default=0)
    perdidas = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s" % (self.user)

TURNO = (
    (0, 'Primero'),
    (1, 'Segundo'),
)

class Partida(models.Model):
    usuario = models.ForeignKey(UsuarioBarquitos, related_name="useruno_partida_set")
    oponente = models.ForeignKey(UsuarioBarquitos, related_name="userdos_partida_set")
    tablero1 = models.CharField(max_length=100, blank=True, null=True, default=TABLERO_VACIO)
    tablero1_ataque = models.CharField(max_length=100, blank=True, null=True, default=TABLERO_VACIO)
    tablero2 = models.CharField(max_length=100, blank=True, null=True, default=TABLERO_VACIO)
    tablero2_ataque = models.CharField(max_length=100, blank=True, null=True, default=TABLERO_VACIO)
    turno = models.IntegerField(choices=TURNO, default=1)
    
    class Meta:
        unique_together = (('usuario', 'oponente'),)
        
    def __unicode__(self):
        return "%s VS. %s" % (self.usuario, self.oponente)

ESTADO_PETICION_PARTIDA = (
    (0, 'Esperando'),
    (1, 'Aceptada'),
    (2, 'Rechazada'),
)

class PeticionPartida(models.Model):
    usuario = models.ForeignKey(UsuarioBarquitos, related_name="useruno_peticion_partida_set")
    oponente = models.ForeignKey(UsuarioBarquitos, related_name="userdos_peticion_partida_set")
    estado = models.IntegerField(choices=ESTADO_PETICION_PARTIDA, default=0)
    fecha_peticion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = (('usuario', 'oponente'),)
        
    def __unicode__(self):
        return "%s VS %s" % (self.usuario, self.oponente)
    
    def get_estado(self):
        return ESTADO_PETICION_PARTIDA[self.estado][1]

