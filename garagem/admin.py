from django.contrib import admin

from . models import Categoria, Veiculo, Acessorio, Cor, Marca, Modelo

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Acessorio)
admin.site.register(Veiculo)
admin.site.register(Modelo)
