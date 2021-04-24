from django.db import models
from django.forms import ModelForm
# Create your models here.
class Configuracion(models.Model):
    dolares_por_kilometros = models.FloatField()
    valor_comida = models.FloatField()
    direccion_fija = models.CharField(max_length=500)
    no_comidas_por_semana = models.IntegerField(default=0)
    no_de_comida_por_dia = models.IntegerField(default=0)

    class ConfiguracionForm(ModelForm):
        class Meta:
            ordering = ["direccion_fija"]
            verbose_name = "Configuracion"

    def __str__(self):
        return self.direccion_fija 


class Perfil(models.Model):
    nombre = models.CharField(max_length=200)
    peso_inicio = models.FloatField()
    peso_meta = models.FloatField()
    id_cliente = models.ForeignKey("usuarios.Cliente", on_delete = models.CASCADE)

    class PerfilForm(ModelForm):
        class Meta:
            ordering = ["nombre"]
            verbose_name = "Perfil"

    def __str__(self):
        return self.nombre

class PerfilE(models.Model):
    nombre=models.CharField(max_length=200)
    imagen=models.CharField(max_length=200)

    class Meta:
        verbose_name = "Perfil_E"

    def __str__(self):
        return self.nombre

