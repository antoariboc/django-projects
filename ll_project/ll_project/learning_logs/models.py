from django.db import models

# Create your models here.

class Topic(models.Model):
    """" Temas o topics
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # Retrona el texto
        return self.text
    
class Entry(models.Model):
    #una entrada asociada a un tema
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # Retrona el texto
        return f"{self.text[:50]}"