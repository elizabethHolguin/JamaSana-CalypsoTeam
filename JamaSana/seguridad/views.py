from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import FormaDePago
from .models import Iva
from .models import Tarjeta
from .models import Factura

from .serializers import FormaDePagoSerializer
from .serializers import IvaSerializer
from .serializers import TarjetaSerializer
from .serializers import FacturaSerializer
# Create your views here.

class FormaDePagoViewSet(viewsets.ModelViewSet):
    queryset = FormaDePago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormaDePagoSerializer

class IvaViewSet(viewsets.ModelViewSet):
    queryset = Iva.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IvaSerializer


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TarjetaSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaSerializer