from django.contrib import admin
from .models import Administrador, Vendedor, Cliente 
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Vendedor)
admin.site.register(Cliente)
