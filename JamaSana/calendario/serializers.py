from rest_framework import serializers
from .models import Calendario
from .models import Dias
from .models import Detalle_dias

class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario
        fields = ('id','id_cliente')

class DiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dias
        fields = ('id','id_calendario')

class Detalle_diasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_dias
        fields = ('id','id_dias','hora_entrega','id_comida')


