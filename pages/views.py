from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from django.views.generic import ListView ,DetailView , TemplateView,CreateView
from django.urls import reverse

class HomePage(ListView):
    queryset = Post.objects.all()
    template_name = "pages/posts.html"
    
    context_object_name = "posts"


class NewPostCreateView(LoginRequiredMixin,CreateView) : 
    model = Post
    template_name = "pages/post_new.html"  
    fields = ['title','content','status','created_on']
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    template_name = "pages/post.html"

    
