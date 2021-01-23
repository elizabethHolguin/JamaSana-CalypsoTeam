from django.db import models
from django.forms import ModelForm
# Create your models here.

class TipoSuscripcion(models.Model):
    nombre = models.CharField(max_length=350)
    duracion = models.IntegerField(default=0)

    class TipoSuscripcionForm(ModelForm):
        class Meta:
            ordering = ["nombre"]
            verbose_name = "Tipo Suscripcion"
    
    def __str__(self):
        return self.nombre 

class Suscripcion(models.Model):
    nombre = models.CharField(max_length=200)
    id_tipo_suscripcion = models.ForeignKey(TipoSuscripcion, on_delete=models.CASCADE)
    precio = models.FloatField()
    cantidad_comidas = models.IntegerField(default=0)
    comidas_gratis = models.IntegerField(default=0)
    color = models.CharField(max_length=200)

    class SuscripcionForm(ModelForm):
        class Meta:
            ordering = ["nombre"]
            verbose_name = "Suscripcion"

    def __str__(self):
        return self.nombre

class ClienteSuscripcion(models.Model):
    id_cliente = models.ForeignKey("usuarios.Cliente", on_delete=models.CASCADE)
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    comidas_consumidas = models.IntegerField(default=0)
    fecha_inicio = models.DateField()
    fecha_de_caducidad = models.DateField()
    fecha_facturacion = models.DateField()
    comidas_disponibles = models.IntegerField(default=0)
    comidas_gratis_disponibles = models.IntegerField(default=0)
    comidas_gratis_consumidas = models.IntegerField(default=0)

    
    class ClienteSuscripcion(ModelForm):
        class Meta:
            ordering = ["id_cliente"]
            verbose_name = "Suscripcion de clientes"

    def __str__(self):
        return self.id_cliente
