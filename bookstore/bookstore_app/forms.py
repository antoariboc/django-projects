from django.forms import ModelForm
from django.forms.widgets import  DateInput
from .models import Author, Genre, Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ("name","biography","birth_date",)
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }
        
class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ("name","description",)
        
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("title","description","author","genre","editor","published_date")