from django.contrib import admin
from .models import Suscripcion, TipoSuscripcion, ClienteSuscripcion
# Register your models here.

admin.site.register(Suscripcion)
admin.site.register(TipoSuscripcion)
admin.site.register(ClienteSuscripcion)
