from django.urls import path
from .views import HomePage,PostDetailView

urlpatterns = [
    
    path('',HomePage.as_view(),name="home-page"),
    path('<slug:slug>/',PostDetailView.as_view(),name="post-detail"),

]