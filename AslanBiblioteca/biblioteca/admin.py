from django.contrib import admin
from .models import Libro, Autor, Categoria, NavItem

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'anio_publicacion', 'autor', 'categoria', 'imagen_url')

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'imagen_url')


admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria)
admin.site.register(NavItem)
