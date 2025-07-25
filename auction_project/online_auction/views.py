from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models

# Create your views here.

#def login(request):
    #return render(request, 'login.html')

def landing(request):
    return render(request, 'landing.html')

#def item(request):
    #return render(request, 'item.html')

def register(request):
    return render(request, 'register.html')

def auth_failed(request):
    return render(request, 'auth_failed.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('listings')
    
    if request.method == 'POST':
        usr = request.POST.get('usrnme')
        pwd = request.POST.get('pwd')
        print(usr)
        print(pwd)
        user = authenticate(request, username = usr, password = pwd)

        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('login')

    return render(request, 'login.html')



@login_required(login_url='/login/')
def Listings_view(request):
    listings = models.Listings.objects.all()
    return render(request,'listings.html',{'listings':listings})



@login_required(login_url='/login/')
def item(request,item_id):
    item = get_object_or_404(models.Listings,id=item_id)
    return render(request,'item.html',{'item':item})