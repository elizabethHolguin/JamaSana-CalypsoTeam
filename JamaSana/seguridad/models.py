from django.db import models
from django.forms import ModelForm
# Create your models here.
class FormaDePago(models.Model):
    forma_pago = models.CharField(max_length=250)

    class FormaDePagoForm(ModelForm):
        class Meta:
            ordering = ["forma_pago"]
            verbose_name = "Forma de pago"

    def __str__(self):
        return self.forma_pago
    
class Iva(models.Model):
    porcentaje = models.FloatField()
    nombre_impuesto = models.CharField(max_length=300)

    class IvaForm(ModelForm):
        class Meta:
            ordering = ["nombre_impuesto"]
            verbose_name = "Iva"

    def __str__(self):
        return self.nombre_impuesto

class Tarjeta(models.Model):
    nombre_propietario = models.CharField(max_length=200)
    tipo_tarjeta = models.CharField(max_length=200)
    fecha_caducidad = models.DateField()
    direccion_facturacion = models.CharField(max_length=350)
    cvv = models.IntegerField(default=0)
    numero_tarjeta = models.CharField(max_length=16)

    class TarjetaForm(ModelForm):
        class Meta:
            ordering = ["nombre_propietario","numero_tarjeta"]
            verbose_name = "Tarjeta"

    def __str__(self):
        return self.nombre_propietario + ' . ' + self.numero_tarjeta

class Factura(models.Model):
    id_suscripcion = models.ForeignKey("paquetes.Suscripcion", on_delete=models.CASCADE)
    id_forma_pago = models.ForeignKey(FormaDePago, on_delete=models.CASCADE)
    id_iva = models.ForeignKey(Iva, on_delete=models.CASCADE)
    monto = models.FloatField()

    class FacturaForm(ModelForm):
        class Meta:
            ordering = ["id_iva"]
            verbose_name = "Factura"

    def __str__(self):
        return self.id_iva