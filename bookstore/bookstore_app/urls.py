from django.urls import path
from . import views
urlpatterns = [
    path('book_add/', views.AddBookView, name='bookstore_app.book_add'),
    path('book_list/', views.BookListView, name='bookstore_app.book_list'),
    path('book_detail/<int:id>', views.BookDetailView, name='bookstore_app.book_detail'),
    path('book_detail/<int:id>/edit', views.BookEditView, name='bookstore_app.book_edit'),
    path('book_detail/<int:id>/delete', views.BookDeleteView, name='bookstore_app.book_delete'),
    path('author_add/', views.AddAuthorView, name='bookstore_app.author_add'),
    path('author_list/', views.AuthorListView, name='bookstore_app.author_list'),
    path('author_detail/<int:id>', views.AuthorDetailView, name='bookstore_app.author_detail'),
    path('author_detail/<int:id>/edit', views.AuthorEditView, name='bookstore_app.author_edit'),
    path('author_detail/<int:id>/delete', views.AuthorDeleteView, name='bookstore_app.author_delete'),
    path('genre_add/', views.AddGenreView, name='bookstore_app.genre_add'),
    path('genre_list/', views.GenreListView, name='bookstore_app.genre_list'),
    path('genre_detail/<int:id>', views.GenreDetailView, name='bookstore_app.genre_detail'),
    path('genre_detail/<int:id>/edit', views.GenreEditView, name='bookstore_app.genre_edit'),
    path('genre_detail/<int:id>/delete', views.GenreDeleteView, name='bookstore_app.genre_delete'),
]