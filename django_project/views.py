from django.shortcuts import render
from .models import exp
# Create your views here.

def index(request):
    u1=exp()
    u1.name='pizaaaaa'
    u1.price='7000'
    u1.des='awesome pizza'
    return render(request, 'index.html',{'u1':u1})
