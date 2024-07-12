from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    imagen_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    imagen_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class NavItem(models.Model):
    titulo = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo