from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Categoria
from .models import Comidas
from .models import Pedido
from .models import DetallePedido

from .serializers import CategoriaSerializer
from .serializers import ComidasSerializer
from .serializers import PedidoSerializer
from .serializers import DetallePedidoSerializer
# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer

class ComidasViewSet(viewsets.ModelViewSet):
    queryset = Comidas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComidasSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DetallePedidoSerializer