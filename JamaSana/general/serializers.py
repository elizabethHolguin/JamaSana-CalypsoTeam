from rest_framework import serializers
from .models import Configuracion
from .models import Perfil
from .models import PerfilE
from .models import PerfilParametrizado
from .models import CategoriasPerfilParametrizado

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ('id',
        'dolares_por_kilometros',
        'valor_comida',
        'direccion_fija',
        'no_comidas_por_semana',
        'no_de_comida_por_dia')

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id',
        'nombre',
        'peso_inicio',
        'peso_meta',
        'id_cliente')

class PerfilESerializer(serializers.ModelSerializer):

    class Meta:
        model=PerfilE
        fields=('id',
        'nombre',
        'imagen')

class PerfilParametrizadoSerializer(serializers.ModelSerializer):

    class Meta:
        model=PerfilParametrizado
        fields=('id',
        'nombre',
        'peso_mode_comparator',
        'peso_minimo',
        'peso_maximo',
        'altura_mode_comparator',
        'altura_minimo',
        'altura_maximo',
        'imc_mode_comparator',
        'imc_minimo',
        'imc_maximo')

class CategoriasPerfilParametrizadoSerializer(serializers.ModelSerializer):

    class Meta:
        model=CategoriasPerfilParametrizado
        fields=('id',
        'perfil_parametrizado',
        'categoria')
