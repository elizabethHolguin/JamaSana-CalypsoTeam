from rest_framework import serializers
from .models import Categoria
from .models import Comidas
from .models import Pedido
from .models import DetallePedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre','imagen')

class ComidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comidas
        fields = ('nombre','descripcion','calorias_totales','macronutrientes','id_categoria','id_vendedor',
        'imagen','direccion_envio')

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id_cliente','fecha_emitido','estado')

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ('id_pedido','fecha_emitido','id_comida','id_dias','hora_entrega','estado_pedido')
