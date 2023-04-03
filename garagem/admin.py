from django.contrib import admin

from . models import Marca, Acessorio, Categoria, Cor

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Acessorio)
