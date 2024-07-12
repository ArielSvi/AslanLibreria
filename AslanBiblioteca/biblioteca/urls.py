from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.libros, name='libros'),
    path('autores/', views.autores, name='autores'),
    path('categorias/', views.categorias, name='categorias'),
]
