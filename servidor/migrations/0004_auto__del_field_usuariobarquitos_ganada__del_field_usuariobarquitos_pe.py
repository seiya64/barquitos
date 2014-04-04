# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UsuarioBarquitos.ganada'
        db.delete_column('servidor_usuariobarquitos', 'ganada')

        # Deleting field 'UsuarioBarquitos.perdida'
        db.delete_column('servidor_usuariobarquitos', 'perdida')

        # Adding field 'UsuarioBarquitos.ganadas'
        db.add_column('servidor_usuariobarquitos', 'ganadas',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UsuarioBarquitos.perdidas'
        db.add_column('servidor_usuariobarquitos', 'perdidas',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'UsuarioBarquitos.ganada'
        db.add_column('servidor_usuariobarquitos', 'ganada',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'UsuarioBarquitos.perdida'
        db.add_column('servidor_usuariobarquitos', 'perdida',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'UsuarioBarquitos.ganadas'
        db.delete_column('servidor_usuariobarquitos', 'ganadas')

        # Deleting field 'UsuarioBarquitos.perdidas'
        db.delete_column('servidor_usuariobarquitos', 'perdidas')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'servidor.partida': {
            'Meta': {'unique_together': "(('usuario', 'oponente'),)", 'object_name': 'Partida'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oponente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userdos_partida_set'", 'to': "orm['servidor.UsuarioBarquitos']"}),
            'tablero1': ('django.db.models.fields.CharField', [], {'default': "'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tablero1_ataque': ('django.db.models.fields.CharField', [], {'default': "'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tablero2': ('django.db.models.fields.CharField', [], {'default': "'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tablero2_ataque': ('django.db.models.fields.CharField', [], {'default': "'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'turno': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'useruno_partida_set'", 'to': "orm['servidor.UsuarioBarquitos']"})
        },
        'servidor.peticionpartida': {
            'Meta': {'unique_together': "(('usuario', 'oponente'),)", 'object_name': 'PeticionPartida'},
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fecha_peticion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oponente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userdos_peticion_partida_set'", 'to': "orm['servidor.UsuarioBarquitos']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'useruno_peticion_partida_set'", 'to': "orm['servidor.UsuarioBarquitos']"})
        },
        'servidor.usuariobarquitos': {
            'Meta': {'object_name': 'UsuarioBarquitos'},
            'desde': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ganadas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perdidas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puntuacion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rol': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['servidor']