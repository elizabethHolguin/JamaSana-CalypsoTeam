from rest_framework import serializers
from .models import FormaDePago
from .models import Iva
from .models import Tarjeta
from .models import Factura

class FormaDePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaDePago
        fields = ('forma_pago')

class IvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iva
        fields = ('porcentaje','nombre_impuesto')

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('id_suscripcion','id_forma_pago','id_iva','monto')


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ('nombre_propietario','tipo_tarjeta','fecha_caducidad','direccion_facturacion','cvv','numero_tarjeta')