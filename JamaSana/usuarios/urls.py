from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('register', views.register),
    path('login', views.login),
    path('logout', views.logout)
]
router = routers.DefaultRouter()
router.register('clientes',views.ClienteViewSet,'clientes')
router.register('administradores',views.AdministradorViewSet,'administradores')
router.register('vendedores',views.VendedorViewSet,'vendedores')
urlpatterns = urlpatterns + router.urls

