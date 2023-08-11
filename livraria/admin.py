from django.contrib import admin

from .models import Categoria
from .models import Editora
from .models import Autor
from .models import Livro
from .models import Compra, ItensCompra

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
# admin.site.register(Compra)
# admin.site.register(ItensCompra)


class ItensCompraInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]
