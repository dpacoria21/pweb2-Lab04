from urllib.request import HTTPHandler
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html",{})

def anotherView(request):
    print(request.user)
    return HttpResponse('<h1>Solo otra pagina</h1>')

def mipageView(request,*args, **kwargs):
    return render(request, "tags.html",{})