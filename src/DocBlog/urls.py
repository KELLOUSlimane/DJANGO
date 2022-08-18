"""DocBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from .views import index
from blog.views import blog_index, article
urlpatterns = [
    path('', index, name='index'),
    #path('blog/',"urls.py"),
    path('blog/', blog_index, name='blog_index'),
    path('blog/article<str:num>', article, name='article'),
    #path('blog/article02', article02),
    #path('blog/article03', article03),
    path('admin/', admin.site.urls),
]
