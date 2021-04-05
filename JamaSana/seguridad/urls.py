from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('allformapago', views.formaPagoAll),
    path('formapago/<int:pk>', views.formaPago),
    path('alliva', views.ivaAll),
    path('iva/<int:pk>', views.iva),
    path('alltarjeta', views.tarjetaAll),
    path('tarjeta/<int:pk>', views.tarjeta),
    path('allfactura', views.facturaAll),
    path('factura/<int:pk>', views.factura),
]
router = routers.DefaultRouter()
router.register('formadepagos',views.FormaDePagoViewSet,'formadepagos')
router.register('ivas',views.IvaViewSet,'ivas')
router.register('tarjetas',views.TarjetaViewSet,'tarjetas')
router.register('facturas',views.FacturaViewSet,'facturas')
urlpatterns = urlpatterns + router.urls


