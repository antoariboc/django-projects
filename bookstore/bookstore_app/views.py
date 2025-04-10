from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, GenreForm, BookForm
from .models import Author, Genre, Book

# Create your views here.



# Libros

def AddBookView(request):
    
    template_data = {}
    template_data['title'] = 'Add Book'

    if request.method == 'GET':
        template_data['form'] = BookForm()
        return render(request, 'bookstore_app/book_add.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore_app.book_list')
        else:
            template_data['form'] = form
            return render(request, 'bookstore_app/book_add.html', {'template_data': template_data})


def BookListView(request):
    books = Book.objects.all()

    template_data = {}
    template_data['title'] = 'Books'
    template_data['books'] = books
    return render(request, 'bookstore_app/book_list.html', {'template_data': template_data})


def BookDetailView(request):
    book = Book.objects.get(id=id)

    template_data = {}
    template_data['title'] = book.name
    template_data['book'] = book
    return render(request, 'bookstore_app/book_detail.html', {'template_data': template_data})

def BookEditView(request, id):
    book = get_object_or_404(Book, id=id)
    
    form = BookForm(initial={
        'title' : book.title , 
        'description' : book.description,
        'author' : book.author,
        'genre' : book.genre,
        'editor': book.editor,
        'published_date' : book.published_date
    })

    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit book'
        template_data['form'] = form
        template_data['book'] = book
        return render(request, 'bookstore_app/book_edit.html', {'template_data': template_data})
    elif request.method == 'POST' and request.POST['title'] != '' and request.POST['description'] != '':
        book = Book.objects.get(id=id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.author = request.POST['author']
        book.genre = request.POST['genre']
        book.editor = request.POST['editor']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('bookstore_app.author_detail', id = book.id)
    else:
        return redirect('bookstore_app.author_detail', id=id)
    
def BookDeleteView(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('bookstore_app.book_list')

# Autores

def AddAuthorView(request):
    
    template_data = {}
    template_data['title'] = 'Add Author'

    if request.method == 'GET':
        template_data['form'] = AuthorForm()
        return render(request, 'bookstore_app/author_add.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        form = AuthorForm(request.POST)
        print("Form is valid?", form.is_valid())
        print("Form errors:", form.errors)
        if form.is_valid():
            form.save()
            return redirect('bookstore_app.author_list')
        else:
            template_data['form'] = form
            return render(request, 'bookstore_app/author_add.html', {'template_data': template_data})

def AuthorListView(request):
    authors = Author.objects.all()

    template_data = {}
    template_data['title'] = 'Authors'
    template_data['authors'] = authors
    return render(request, 'bookstore_app/author_list.html', {'template_data': template_data})
    
def AuthorDetailView(request, id):
    author = Author.objects.get(id=id)

    template_data = {}
    template_data['title'] = author.name
    template_data['author'] = author
    return render(request, 'bookstore_app/author_detail.html', {'template_data': template_data})

def AuthorEditView(request, id):
    author = get_object_or_404(Author, id=id)
    
    form = AuthorForm(initial={
        'name' : author.name , 
        'biography' : author.biography,
        'birth_date' : author.birth_date
    })

    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit author'
        template_data['form'] = form
        template_data['author'] = author
        return render(request, 'bookstore_app/author_edit.html', {'template_data': template_data})
    elif request.method == 'POST' and request.POST['name'] != '' and request.POST['biography'] != '':
        author = Author.objects.get(id=id)
        author.name = request.POST['name']
        author.biography = request.POST['biography']
        author.birth_date = request.POST['birth_date']
        author.save()
        return redirect('bookstore_app.author_detail', id = author.id)
    else:
        return redirect('bookstore_app.author_detail', id=id)
    
def AuthorDeleteView(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('bookstore_app.author_list')

# Generos

def AddGenreView(request):
    
    template_data = {}
    template_data['title'] = 'Add Genre'

    if request.method == 'GET':
        template_data['form'] = GenreForm()
        return render(request, 'bookstore_app/genre_add.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore_app.genre_list')
        else:
            template_data['form'] = form
            return render(request, 'bookstore_app/genre_add.html', {'template_data': template_data})
        
def GenreListView(request):
    genres = Genre.objects.all()

    template_data = {}
    template_data['title'] = 'Genre'
    template_data['genres'] = genres
    return render(request, 'bookstore_app/genre_list.html', {'template_data': template_data})

def GenreDetailView(request, id):
    genre = Genre.objects.get(id=id)

    template_data = {}
    template_data['title'] = genre.name
    template_data['genre'] = genre
    return render(request, 'bookstore_app/genre_detail.html', {'template_data': template_data})

def GenreEditView(request, id):
    genre = get_object_or_404(Genre, id=id)
    
    form = GenreForm(initial={
        'name' : genre.name , 
        'description' : genre.description
    })

    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit genre'
        template_data['form'] = form
        template_data['genre'] = genre
        return render(request, 'bookstore_app/genre_edit.html', {'template_data': template_data})
    elif request.method == 'POST' and request.POST['name'] != '' and request.POST['description'] != '':
        genre = Genre.objects.get(id=id)
        genre.name = request.POST['name']
        genre.description = request.POST['description']
        genre.save()
        return redirect('bookstore_app.genre_detail', id = genre.id)
    else:
        return redirect('bookstore_app.genre_detail', id=id)
    
def GenreDeleteView(request, id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return redirect('bookstore_app.genre_list')

# Reviews