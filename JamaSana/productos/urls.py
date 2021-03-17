from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('allcategorias', views.categorias),
    path('categoria/<int:pk>', views.categoria),
    path('allcomidas', views.comidasAll),
    path('comida/<int:pk>', views.comida),
    path('allpedidos', views.pedidosAll),
    path('pedido/<int:pk>', views.pedido),
]
router = routers.DefaultRouter()
router.register('categorias', views.CategoriaViewSet,'categorias')
router.register('comidas', views.ComidasViewSet,'comidas')
router.register('pedidos', views.PedidoViewSet,'pedidos')
router.register('detallepedidos', views.DetallePedidoViewSet,'detallepedidos')
urlpatterns = urlpatterns + router.urls


