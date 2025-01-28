from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(),name="article_detail"),
    path('article/new', ArticleCreateView.as_view(),name="article_new"),
]