from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   
]
router = routers.DefaultRouter()
router.register('tipoSuscripciones', views.TipoSuscripcionViewSet,'tipoSuscripciones')
router.register('suscripciones', views.SuscripcionViewSet,'suscripciones')
router.register('clienteSuscripciones', views.ClienteSuscripcionViewSet,'clienteSuscripciones')
urlpatterns = urlpatterns + router.urls

