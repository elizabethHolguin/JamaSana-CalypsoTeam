from django.db import models
from django.forms import ModelForm
# Create your models here.

class Calendario(models.Model):
    id_cliente = models.ForeignKey("usuarios.Cliente", on_delete=models.CASCADE)

    class CalendarioForm(ModelForm):
        class Meta:
            ordering = ["id_cliente"]
            verbose_name = "Calendario"

    def __str__(self):
        return self.id_cliente
   
class Dias(models.Model):
    id_calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)

    class DiasForm(ModelForm):
        class Meta:
            ordering = ["id_calendario"]
            verbose_name = "Calendario"

    def __str__(self):
        return self.id_calendario

class Detalle_dias(models.Model):
    id_dias = models.ForeignKey(Dias, on_delete=models.CASCADE)
    hora_entrega = models.DateTimeField('Hora de entrega')
    id_comida = models.ForeignKey("productos.Comidas", on_delete=models.CASCADE)

    class Detalle_diasForm(ModelForm):
        class Meta:
            ordering = ["id_dias"]
            verbose_name = "Detalle dias"

    def __str__(self):
        return self.id_dias