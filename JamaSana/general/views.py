from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Configuracion
from .models import Perfil

from .serializers import ConfiguracionSerializer
from .serializers import PerfilSerializer
# Create your views here.

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConfiguracionSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PerfilSerializer

