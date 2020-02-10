from django.shortcuts import render

from .models import Post
from django.views.generic import ListView 
class HomePage(ListView):
    queryset = Post.objects.all()
    template_name = "pages/homepage.html"
    
    context_object_name = "posts"

