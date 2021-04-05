from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('allcalendario', views.calendarioAll),
    path('calendario/<int:pk>', views.calendario),
    path('alldia', views.diasAll),
    path('dia/<int:pk>', views.dia),
    path('alldetalledia', views.detalleDiaAll),
    path('detalledia/<int:pk>', views.detalleDia),
]
router = routers.DefaultRouter()
router.register('calendarios', views.CalendarioViewSet,'calendarios')
router.register('dias', views.DiasViewSet,'dias')
router.register('detalle_dias', views.Detalle_diasViewSet,'detalle_dias')
urlpatterns = urlpatterns + router.urls



 