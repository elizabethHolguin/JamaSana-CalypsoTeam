from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   
]
router = routers.DefaultRouter()
router.register('calendarios', views.CalendarioViewSet,'calendarios')
router.register('dias', views.DiasViewSet,'dias')
router.register('detalle_dias', views.Detalle_diasViewSet,'detalle_dias')
urlpatterns = urlpatterns + router.urls



 