from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   
]
router = routers.DefaultRouter()
router.register('formadepagos',views.FormaDePagoViewSet,'formadepagos')
router.register('ivas',views.IvaViewSet,'ivas')
router.register('tarjetas',views.TarjetaViewSet,'tarjetas')
router.register('facturas',views.FacturaViewSet,'facturas')
urlpatterns = urlpatterns + router.urls


