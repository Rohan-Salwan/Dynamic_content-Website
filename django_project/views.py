from django.shortcuts import render
from .models import exp
# Create your views here.

def index(request):
    u1=exp()
    u1.name='virgin sala'
    u1.price='7000'
    u1.des='awesome pizza'
    return render(request, 'index.html',{'u1':u1})

def login(request):
    na=request.GET['fname']
    naa=request.GET['lname']
    re=na+naa
    return render(request, 'result.html', {"result":re})

    
