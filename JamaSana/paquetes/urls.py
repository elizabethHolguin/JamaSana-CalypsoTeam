from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('alltiposuscripciones', views.tipoSuscripcionAll),
    path('tiposuscripcion/<int:pk>', views.tipoSuscripcion),
    path('allsuscripcion', views.suscripcionAll),
    path('suscripcion/<int:pk>', views.suscripcion),
    path('allclientesuscripciones', views.clienteSuscripcionAll),
    path('clientesuscripciones/<int:pk>', views.clienteSuscripcion),
]
router = routers.DefaultRouter()
router.register('tipoSuscripciones', views.TipoSuscripcionViewSet,'tipoSuscripciones')
router.register('suscripciones', views.SuscripcionViewSet,'suscripciones')
router.register('clienteSuscripciones', views.ClienteSuscripcionViewSet,'clienteSuscripciones')
urlpatterns = urlpatterns + router.urls

