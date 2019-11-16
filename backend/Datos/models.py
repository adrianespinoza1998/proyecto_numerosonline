from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario:models.IntegerField
    nombre:models.CharField(max_length=50)
    ap_paterno:models.CharField(max_length=50)
    ap_materno:models.CharField(max_length=50)
    rut:models.CharField(max_length=9)
    correo:models.CharField(max_length=50)
    contrasena:models.CharField(max_length=50)

class Region(models.Model):
    id_region:models.IntegerField
    nombreRegion:models.CharField(max_length=50)

class Ciudad(models.Model):
    id_ciudad:models.IntegerField
    id_region:models.IntegerField
    nombreCiudad:models.CharField(max_length=50)

class Comuna(models.Model):
    id_comuna:models.IntegerField
    id_ciudad:models.IntegerField
    nombreComuna:models.CharField(max_length=50)

class Notaria(models.Model):
    id_notaria:models.IntegerField
    id_comuna:models.IntegerField
    nombre_notaria:models.CharField(max_length=50)
    direccion:models.CharField(max_length=50)
    telefono:models.IntegerField

class Tramite(models.Model):
    id_tramite:models.IntegerField
    nombreTramite:models.CharField(max_length=50)

class Fila(models.Model):
    id_fila:models.IntegerField
    id_notaria:models.IntegerField
    id_tramite:models.IntegerField
    nroFila:models.IntegerField

class Ticket(models.Model):
    id_ticket:models.IntegerField
    id_usuario:models.IntegerField
    id_fila:models.IntegerField

