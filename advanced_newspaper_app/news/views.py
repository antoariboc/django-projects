from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article 

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'