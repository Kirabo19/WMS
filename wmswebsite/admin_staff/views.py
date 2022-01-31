from django.shortcuts import render, redirect
from .models import admin_staff
from django.contrib import messages

# Create your views here.
def index(request):
     return render(request, 'admin_staff/index.html')


def add_user(request):  

    if request.method == 'GET':   
     return render(request, 'admin_staff/adduser.html')

    if request.method == 'POST':
        admin_user = request.POST['admin_user']
        admin_password = request.POST['admin_password']
        admin_name = request.POST['admin_name']
        admin_address = request.POST['admin_address']
        admin_phone = request.POST['admin_phone']
        admin_group = request.POST['admin_group']

    admin_staff.objects.create(admin_user=admin_user,admin_password=admin_password, admin_name=admin_name, admin_address=admin_address, 
    admin_phone=admin_phone, admin_group= admin_group ) 

    messages.success(request, 'New user has been added successfully!') 
    return redirect('admin_staff')   
