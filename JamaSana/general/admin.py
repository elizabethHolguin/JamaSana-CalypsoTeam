from django.contrib import admin
from .models import Configuracion, Perfil, PerfilE, PerfilParametrizado, CategoriasPerfilParametrizado
# Register your models here.

admin.site.register(Configuracion)
admin.site.register(Perfil)
admin.site.register(PerfilE)
admin.site.register(PerfilParametrizado)
admin.site.register(CategoriasPerfilParametrizado)
