from django.shortcuts import render
#from .models import admin_staff
#from django.contrib import messages

# Create your views here.
def index(request):
     return render(request, 'admin_staff/index.html') 
     