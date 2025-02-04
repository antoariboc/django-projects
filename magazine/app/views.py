from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Category



def post_list(request):
    posts = Post.objects.all().order_by('-published_date') # Ordenar por fecha descendente
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk): # Usar pk (primary key)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def category_posts(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = category.posts.all().order_by('-published_date')
    return render(request, 'category_posts.html', {'posts': posts, 'category': category})