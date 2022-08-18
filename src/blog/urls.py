from django.urls import path, include 
from .views import blog_index, article

urlpatterns = [
    path('', blog_index, name = "blog_index"),
    path('', article, name = "blog_article"),
]
