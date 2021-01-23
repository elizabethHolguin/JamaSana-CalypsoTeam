from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Cliente
from .models import Administrador
from .models import Vendedor

from .serializers import ClienteSerializer
from .serializers import AdministradorSerializer
from .serializers import VendedorSerializer
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AdministradorSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VendedorSerializer