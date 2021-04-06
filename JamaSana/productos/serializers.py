from rest_framework import serializers
from .models import Categoria
from .models import Comidas
from .models import Pedido
from .models import DetallePedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre','imagen')

class ComidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comidas
        fields = ('id','nombre','descripcion','precio','calorias_totales','macronutrientes','id_categoria','id_vendedor',
        'imagen','estado')

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id','id_cliente','fecha_emitido','estado')

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ('id','id_pedido','fecha_emitido','id_comida','id_dias','hora_entrega','estado_pedido')
