from django.shortcuts import render, redirect
from .models import admin_staff
from django.contrib import messages

# Create your views here.
def index(request):
     admin_users = admin_staff.objects.all()

     Context = {
          'admin_users': admin_users
     }
     return render(request, 'admin_staff/index.html', Context)


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

# Add or Save funtion
def edit_user(request, id):
     adminusers = admin_staff.objects.get(pk=id)
     context ={
          'adminusers': adminusers,
          'values' : adminusers,
     }
     if request.method=='GET':
     
       
        return render(request, 'admin_staff/edituser.html', context)
        
     if request.method=='POST':
          admin_user = request.POST['admin_user']
          admin_password = request.POST['admin_password']
          admin_name = request.POST['admin_name']
          admin_address = request.POST['admin_address']
          admin_phone = request.POST['admin_phone']
          admin_group = request.POST['admin_group']
          
          adminusers.admin_user = admin_user
          adminusers.admin_password = admin_password
          adminusers.admin_name = admin_name
          adminusers.admin_address = admin_address
          adminusers.admin_phone = admin_phone
          adminusers.admin_group = admin_group

          adminusers.save()
          messages.success(request, 'User has been edited successfully!,')

          return redirect('admin_staff')

# Delete function
def delete_user(request, id):
    adminusers = admin_staff.objects.get(pk=id)
    adminusers.delete()
    messages.success(request, 'The user has been succussfuly blocked!,') 
     
    return redirect('admin_staff')
          

