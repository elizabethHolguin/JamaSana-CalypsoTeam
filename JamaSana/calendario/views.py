from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Calendario
from .models import Dias
from .models import Detalle_dias

from .serializers import CalendarioSerializer
from .serializers import DiasSerializer
from .serializers import Detalle_diasSerializer
# Create your views here.

class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CalendarioSerializer

class DiasViewSet(viewsets.ModelViewSet):
    queryset = Dias.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DiasSerializer


class Detalle_diasViewSet(viewsets.ModelViewSet):
    queryset = Detalle_dias.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Detalle_diasSerializer