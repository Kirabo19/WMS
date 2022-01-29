from django.shortcuts import render, redirect
from .models import makeover
from django.contrib import messages



# Create your views here.
def index(request, id):
    edit_makeover = makeover.objects.get(pk=id)
    edit_makeover = makeover.objects.all()
    context = {
       'edit_makeover': edit_makeover

    }
    if request.method == 'GET':
       return render(request, 'makeover/index.html', context) 
     
    if request.method == 'POST':
     
     edit_makeover.website = website
     edit_makeover.description = description
     edit_makeover.keyword = keyword
     edit_makeover.i_email = i_email
     edit_makeover.fb = fb
     edit_makeover.tw = tw
     edit_makeover.yb = yb

  
     edit_makeover.save()
     messages.success(request,'Data has Successfully been edited!')
     return redirect('makeover')