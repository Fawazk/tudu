
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
        "index":"this is index.html",
        "index2":"this is index.html"
    }
    return render(request, 'index.html',context)