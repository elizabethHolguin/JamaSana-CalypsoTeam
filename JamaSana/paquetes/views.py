from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import TipoSuscripcion
from .models import Suscripcion
from .models import ClienteSuscripcion

from .serializers import TipoSuscripcionSerializer
from .serializers import SuscripcionSerializer
from .serializers import ClienteSuscripcionSerializer
# Create your views here.

class TipoSuscripcionViewSet(viewsets.ModelViewSet):
    queryset = TipoSuscripcion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoSuscripcionSerializer

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SuscripcionSerializer


class ClienteSuscripcionViewSet(viewsets.ModelViewSet):
    queryset = ClienteSuscripcion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  ClienteSuscripcionSerializer