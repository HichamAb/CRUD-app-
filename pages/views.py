from django.shortcuts import render

from .models import Post
from django.views.generic import ListView ,DetailView
class HomePage(ListView):
    queryset = Post.objects.all()
    template_name = "pages/posts.html"
    
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    template_name = "pages/post.html"
