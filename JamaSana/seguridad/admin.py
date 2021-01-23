from django.contrib import admin
from .models import FormaDePago, Tarjeta, Factura, Iva
# Register your models here.


admin.site.register(FormaDePago)
admin.site.register(Tarjeta)
admin.site.register(Factura)
admin.site.register(Iva)
