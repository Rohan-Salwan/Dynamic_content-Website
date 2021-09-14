from django.shortcuts import render, redirect
from .models import exp
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    meals=exp.objects.all()
    return render(request, 'index.html',{'meals':meals})

def login(request):
    if request.method=='POST':
        first=request.POST['username']
        third=request.POST['pwdd']
        jp=auth.authenticate(username=first,  password=third)
        if jp is not None:
            auth.login(request, jp)
            re="welcome"+first
            return render(request, 'result.html',{'re':re})
        else:
            return render(request, 'index.html')            
    else:
        return render(request, 'extra.html')

def register(request):
    if request.method=='POST':
        na=request.POST["fname"]
        naa=request.POST["lname"]
        naaa=request.POST["pwd"]
        naaaa=request.POST["username"]
        userr=User.objects.create_user(username=naaaa, first_name=na, last_name=naa, password=naaa)
        userr.save()
        print('User created')
        return render(request, 'index.html')
    else:
        return render(request, "base.html")

def contact(request):
    return render(request, "contact.html")
    
