from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('allconfiguraciones', views.configuracionAll),
    path('configuracion/<int:pk>', views.configuracion),
    path('allperfiles', views.perfilAll),
    path('perfil/<int:pk>', views.perfil),
    path('allperfilesE)', views.perfilEAll)
]
router = routers.DefaultRouter()
router.register('configuraciones',views.ConfiguracionViewSet,'configuraciones')
router.register('perfiles',views.PerfilViewSet,'perfiles')
router.register('perfilesE', views.PerfilEViewSet,'perfilesE')
urlpatterns = urlpatterns + router.urls

