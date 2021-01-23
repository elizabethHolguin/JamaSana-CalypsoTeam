from django.contrib import admin
from .models import Comidas, Categoria, Pedido, DetallePedido
# Register your models here.


admin.site.register(Comidas)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
