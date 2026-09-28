from django.contrib import admin
from .models import Juegos

class JuegosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'fecha_lanzamiento')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_lanzamiento',)
    ordering = ('nombre',)

admin.site.register(Juegos, JuegosAdmin)

