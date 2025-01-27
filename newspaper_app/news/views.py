from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post
# Create your views here.

def newsView(request):
    return HttpResponse("Hello World")

class HomePageView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
    