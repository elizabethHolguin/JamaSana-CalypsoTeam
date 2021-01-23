from rest_framework import serializers
from .models import Cliente
from .models import Administrador
from .models import Vendedor

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido',' email','usuario','contraseña','direccion','fecha_nacimiento','id_tarjeta')

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('usuario','contraseña')

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('usuario','contraseña')
