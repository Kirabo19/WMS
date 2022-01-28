from django.shortcuts import render
from models import makeover


# Create your views here.
def index(request):
    update_make = makeover.objects.all()
    
    return render(request, 'makeover/index.html') 

def add_system(request):
    return render(request, 'makeover/add_system.html')