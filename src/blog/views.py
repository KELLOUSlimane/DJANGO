#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ClientFroms
from .models import Client
from . import models
from django import forms

# Create your views here.
def blog_index(request) : 
    #return HttpResponse("<h1> le Blog </h1>")
    return render(request, "index.html")

def article(request, num) :
    if (num ==1) : 
     
     #   submitted = False
     #   form  = ClientFroms(request.POST)
     #   if request.method == "POST" :
            
     #       if form.is_valid() :
     #           form.save()
     #           return HttpResponseRedirect('/')
     #   else :
      #      form = ClientFroms
     #       if 'submitted' in request.GET: 
      #          submitted = True
        form  = ClientFroms(request.POST)
        context = {'form' : form}
        return render(request, f"article{num}.html", context)
    else :
        return render(request, f"article{num}.html")