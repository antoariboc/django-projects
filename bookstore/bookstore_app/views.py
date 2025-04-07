from django.shortcuts import render

# Create your views here.

def BookDetailView(request):
    return render(request, 'bookstore_app/book_detail.html')

def BookListView(request):
    return render(request, 'bookstore_app/book_list.html')

# Libros


# Autores

def CreateAuthorView(request):
    pass

# Generos

# Reviews