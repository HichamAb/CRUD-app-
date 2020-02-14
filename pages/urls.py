from django.urls import path
from .views import HomePage,PostDetailView,NewPostCreateView

urlpatterns = [
    
    path('',HomePage.as_view(),name="home-page"),
    path('blogpost/new/', NewPostCreateView.as_view() , name="newpost"),
    path('blogpost/<slug:slug>/',PostDetailView.as_view(),name="post-detail"),
    

]