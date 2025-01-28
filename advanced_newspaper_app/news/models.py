from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )
    
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("model_detail", args={"pk": self.pk})
    