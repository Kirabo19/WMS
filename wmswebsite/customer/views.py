from django.shortcuts import render, redirect
from .models import customer
from django.contrib import messages

# Create your views here.
def index(request):
    customers = customer.objects.all()
    supps = customer.objects.count()
    context = {
        'customers' : customers,
        'supps' : supps
    }
    return render (request, 'customer/index.html',context)

# Add function 
def add_customer(request):
 

  if request.method == 'GET':
     return render(request, 'customer/addcustomer.html')
  if request.method =='POST':
     customer_name = request.POST['customer_name']
     customer_address = request.POST['customer_address'] 
     customer_phone = request.POST['customer_phone']

  customer.objects.create(customer_name=customer_name, customer_address=customer_address, customer_phone=customer_phone)
  messages.success(request,'New customer has been added successfully!,')   
  return redirect('customer')

# Edit function
def edit_customer(request, id):
   edit_custs = customer.objects.get(pk=id)
   context = {
      'edit_custs' : edit_custs,
      'values' : edit_custs
   }
   if request.method =='GET':
    return render(request,'customer/editcustomer.html', context)
   if request.method =='POST':
    customer_name = request.POST['customer_name']
    customer_address = request.POST['customer_address']
    customer_phone = request.POST['customer_phone']
  
    edit_custs.customer_name = customer_name
    edit_custs.customer_address = customer_address
    edit_custs.customer_phone = customer_phone

    edit_custs.save()
    messages.success(request, 'Customer has been edited succesfully!,')

    return redirect('customer')
