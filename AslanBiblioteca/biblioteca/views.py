from django.shortcuts import render
from .models import Libro, Autor, Categoria, NavItem
from django.core.paginator import Paginator

def index(request):
    navitems = NavItem.objects.all()
    return render(request, 'biblioteca/index.html', {'navitems':navitems})

def libros(request):
    libros_list = Libro.objects.all()
    paginator = Paginator(libros_list, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    navitems = NavItem.objects.all()
    
    return render(request, 'biblioteca/libros.html', {'page_obj': page_obj, 'navitems': navitems})

def autores(request):
    navitems = NavItem.objects.all()
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autores.html',{'autores':autores, 'navitems':navitems})

def categorias(request):
    navitems = NavItem.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'biblioteca/categorias.html',{'categorias':categorias, 'navitems':navitems})
