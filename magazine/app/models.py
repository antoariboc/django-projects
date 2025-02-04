from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # unique=True para evitar categorías duplicadas

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)  # auto_now_add para la fecha de creación
    author_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts') # related_name para acceder a los posts de una categoría

    def __str__(self):
        return self.title

    def summary(self): # Método para obtener un resumen del contenido
        return self.content[:200] + "..." 