from django.urls import path
from . import views
urlpatterns = [
    path('book_detail/', views.BookDetailView, name='bookstore_app.book_detail'),
    path('book_list/', views.BookListView, name='bookstore_app.book_list'),
    path('author_create/', views.CreateAuthorView, name='bookstore_app.author_create'),
]