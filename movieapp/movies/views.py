from django.shortcuts import render
from .models import Category,Movie

def home(request):
    data = {
        "categories":Category.objects.all(),
        "films":Movie.objects.filter(home = True)
    }
    return render(request,"index.html",data)

def movies(request):
    data = {
        "categories":Category.objects.all(),
        "films":Movie.objects.all()
    }
    return render(request,"movies.html",data)

def details(request,id):
    data = {
        "film":Movie.objects.get(pk=id)
    }
    return render(request,"details.html",data)