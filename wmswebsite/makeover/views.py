from django.shortcuts import render, redirect
from .models import makeover
from django.contrib import messages



# Create your views here.
def index(request):
    
    if request.method == 'GET':
       return render(request, 'makeover/index.html') 
     
    if request.method == 'POST':
       website = request.POST['website']
       description = request.POST['description']
       keyword = request.POST['keyword']
       i_email = request.POST['i_email']
       fb = request.POST['fb']
       tw = request.POST['tw']
       yb = request.POST['yb']

  
    makeover.objects.create(website=website, description=description, keyword=keyword, i_email=i_email,fb=fb, tw=tw, yb=yb )
    messages.success(request,'Data has Successfully been edited!')
    return redirect('makeover')