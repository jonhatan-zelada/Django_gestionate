from django.db import models
from datetime import datetime

# Create your models here.

class TipoSolicitud(models.Model):
    cod_tipo = models.CharField(max_length=8, verbose_name='Código de solicitud')
    nombre_solicitud = models.CharField(max_length=80, verbose_name='nombre de solicitud')
    descripcion_tipo=models.TextField(max_length=500,verbose_name='Descripción')
    # to show a organName field
    def __str__(self):
       return self.nombre_solicitud

  #Rename the class for visualization
    class Meta:
        verbose_name = "Tipo de Solicitudes"


class Solicitud(models.Model):
    ESTADO_SOLICITUD = (
        ('creado', 'Creado'),
        ('en_proceso', 'En_proceso'),
        ('terminado', 'Terminado'),
    )
    #primero = verbose_name = "¿Cómo podemos ayudarte?"
    tipo = models.ForeignKey(TipoSolicitud,on_delete=models.CASCADE,verbose_name="¿Cómo podemos ayudarte?")
    #segundo = verbose_name = "Si tienes alguna precisión detallala aquí"
    descripcion_sol = models.TextField(max_length=5000,null= True, blank=True,verbose_name="Si tienes alguna precisión, por favor detallala aquí")
    estado = models.CharField(max_length=15,choices=ESTADO_SOLICITUD, default='creado',verbose_name="Estado de la solicitud")
    creada = models.DateTimeField(default=datetime.now,verbose_name="Fecha de creación")
    solicitante = models.CharField(max_length=50, null= True, blank=True,verbose_name="Solicitante")

  #Rename the class for visualization
    class Meta:
        verbose_name = "Solicitudes registradas"
 
  
class TipoTema(models.Model):
    cod_tipotema = models.CharField(max_length=30, verbose_name='Código de tema')
    nombre_tema = models.CharField(max_length=100, verbose_name='Nombre de tema')
    descripcion_tipotema=models.TextField(max_length=500,verbose_name='Descripción')
    
    # to show a organName field
    def __str__(self):
       return  self.nombre_tema
  #Rename the class for visualization
    class Meta:
        verbose_name = "Tipo de Temas"

class Tema (models.Model):
    tipotema = models.ForeignKey(TipoTema,on_delete=models.CASCADE,verbose_name="¿Cómo podemos ayudarte?")
    descripcion_tema = models.TextField(max_length=5000, verbose_name='Describe tu consulta aquí')
    fechatemacreada = models.DateTimeField(default=datetime.now,verbose_name="Fecha de creación")
  #Rename the class for visualization
    class Meta:
        verbose_name = "Temas solicitados"