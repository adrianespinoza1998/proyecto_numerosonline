from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre:models.CharField(max_length=20)
    ap_paterno:models.CharField(max_length=20)
    ap_materno:models.CharField(max_length=20)
    rut:models.CharField(max_length=9)
    correo:models.CharField(max_length=50)
    contrasena:models.CharField(max_length=50)

class Notaria(models.Model):
    nombre_notaria:models.CharField(max_length=20)
    direccion:models.CharField(max_length=20)
    telefono:models.IntegerField

class Turno(models.Model):
    numero_turno:models.IntegerField