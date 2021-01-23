from django.db import models
from django.forms import ModelForm
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    direccion = models.CharField(max_length=350)
    fecha_nacimiento = models.DateField()
    id_tarjeta = models.ForeignKey("seguridad.Tarjeta", on_delete=models.CASCADE)

    class ClienteForm(ModelForm):
        class Meta:
            ordering = ["nombre","apellido"]
            verbose_name = "Cliente"
      

    def __str__(self):
        return self.nombre + ' - ' + self.apellido 
    
class Administrador(models.Model):
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)

    class AdministradorForm(ModelForm):
        class Meta:
            ordering = ["usuario"]
            verbose_name = "Administrador"
  
 
    def __str__(self):
        return self.usuario

class Vendedor(models.Model):
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)

    class VendedorForm(ModelForm):
        class Meta:
            ordering = ["usuario"]
            verbose_name = "Vendedor"

    def __str__(self):
        return self.usuario
