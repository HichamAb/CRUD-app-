from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post , Category
from django.views.generic import ListView ,DetailView , TemplateView,CreateView
from django.urls import reverse

class HomePage(ListView):
    # retrive only latest published posts
   
    template_name = "pages/posts.html"
    
    context_object_name = "posts"
    def get_queryset(self):
        queryset = {"posts":Post.objects.all().order_by('-created_on').filter(status=1),
                    "categories":Category.objects.all()
        }
       
        return queryset
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_on').filter(status=1)
        context['categories']=Category.objects.all()
        # Add any other variables to the context here
        ...
        return context


class NewPostCreateView(LoginRequiredMixin,CreateView) : 
    model = Post
    template_name = "pages/post_new.html"  
    fields = ['title','categories','content','status','created_on']
    def form_valid(self,form,*args,**kwargs) : 
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    template_name = "pages/post.html"

    
