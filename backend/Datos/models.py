from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario=models.IntegerField(default=0)
    nombre=models.CharField(max_length=50,default='Sin nombre')
    ap_paterno=models.CharField(max_length=50,default='Sin ap paterno')
    ap_materno=models.CharField(max_length=50,default='Sin ap materno')
    rut=models.CharField(max_length=9,default='Sin rut')
    correo=models.CharField(max_length=50,default='No hay correo')
    contrasena=models.CharField(max_length=50,default='Sin contraseña')

class Region(models.Model):
    id_region=models.IntegerField(default=0)
    nombreRegion=models.CharField(max_length=50,default='Sin nombre')

class Ciudad(models.Model):
    id_ciudad=models.IntegerField(default=0)
    id_region=models.IntegerField(default=0)
    nombreCiudad=models.CharField(max_length=50,default='Sin nombre')

class Comuna(models.Model):
    id_comuna=models.IntegerField(default=0)
    id_ciudad=models.IntegerField(default=0)
    nombreComuna=models.CharField(max_length=50,default='Sin nombre')

class Notaria(models.Model):
    id_notaria=models.IntegerField(default=0)
    id_comuna=models.IntegerField(default=0)
    nombre_notaria=models.CharField(max_length=50,default='Sin nombre')
    direccion=models.CharField(max_length=50,default='Sin dirección')
    telefono=models.IntegerField(default=0)

class Tramite(models.Model):
    id_tramite=models.IntegerField(default=0)
    nombreTramite=models.CharField(max_length=50,default='Sin nombre')

class Fila(models.Model):
    id_fila=models.IntegerField(default=0)
    id_notaria=models.IntegerField(default=0)
    id_tramite=models.IntegerField(default=0)
    nroFila=models.IntegerField(default=0)

class Ticket(models.Model):
    id_ticket=models.IntegerField(default=0)
    id_usuario=models.IntegerField(default=0)
    id_fila=models.IntegerField(default=0)

