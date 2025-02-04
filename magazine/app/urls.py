from django.urls import path
from . import views

app_name = 'app' # importante para namespacing

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # <int:pk> para capturar la clave primaria
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),
]