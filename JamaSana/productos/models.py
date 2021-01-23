from django.db import models
from django.forms import ModelForm
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_perfil = models.ForeignKey("general.Perfil", on_delete = models.CASCADE)

    class CategoriaForm(ModelForm):
        class Meta:
            ordering = ["nombre"]
            verbose_name = "Categoria"

    def __str__(self):
        return self.nombre

class Comidas(models.Model):
    nombre =  models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    calorias_totales = models.FloatField()
    macronutrientes = models.CharField(max_length=1000)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey("usuarios.Vendedor", on_delete=models.CASCADE)
    imagen = models.ImageField()
    direccion_envio = models.CharField(max_length=500)

    class ComidasForm(ModelForm):
        class Meta:
            ordering = ["nombre","descripcion"]
            verbose_name = "Comidas"

    def __str__(self):
        return self.nombre + ' - ' + self.descripcion



class Pedido(models.Model):
    id_cliente = models.ForeignKey("usuarios.Cliente", on_delete=models.CASCADE)
    fecha_emitido = models.DateTimeField('Fecha de emisión')
    estado = models.IntegerField(default=0)
    
    class PedidoForm(ModelForm):    
        class Meta:
            ordering = ["id_cliente"]
            verbose_name = "Pedido"

    def __str__(self):
        return self.id_cliente

class DetallePedido(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_emitido = models.DateTimeField('Fecha de emisión')
    id_comida = models.ForeignKey("productos.Comidas", on_delete=models.CASCADE)
    id_dias = models.ForeignKey("calendario.Dias", on_delete=models.CASCADE)
    hora_entrega = models.TimeField()
    estado_pedido = models.IntegerField(default=0)

    class DetallePedidoForm(ModelForm):
        class Meta:
            ordering = ["id_comida"]
            verbose_name = "Detalle Pedidos"
       
    def __str__(self):
        return self.id_comida


