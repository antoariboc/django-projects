from django.db import models
from django.conf import settings

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()
    
    def __str__(self):
        return str(self.name) if self.name else "Unnamed"

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return str(self.name) if self.name else "Unnamed"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    published_date = models.DateField()
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user.username} - {self.book.title} ({self.rating}/5)"