from django.contrib import admin
from django.utils.html import mark_safe
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen_preview')

    def imagen_preview(self, obj):
        if obj.imagen:
            return mark_safe(
                f'<img src="{obj.imagen.url}" width="100" height="100" style="object-fit: cover;" />'
            )
        return "Sin imagen"

    imagen_preview.short_description = "Imagen"
