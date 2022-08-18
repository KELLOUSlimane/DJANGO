#from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request) :

    date = datetime.today()
    
    #return HttpResponse("<h1> Bonjour, bienvunue sur mon site </h1>")
    return render(request, "premier_site.html", context= {"date" : date }) 