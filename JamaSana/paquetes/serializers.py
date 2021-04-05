from rest_framework import serializers
from .models import TipoSuscripcion
from .models import Suscripcion
from .models import ClienteSuscripcion

class TipoSuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSuscripcion
        fields = ('id','nombre','duracion')

class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ('id','nombre','id_tipo_suscripcion','precio','cantidad_comidas','comidas_gratis','color')

class ClienteSuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteSuscripcion
        fields = ('id','id_cliente','id_suscripcion','comidas_consumidas','fecha_inicio','fecha_de_caducidad','fecha_facturacion',
        'comidas_disponibles','comidas_gratis_disponibles','comidas_gratis_consumidas')