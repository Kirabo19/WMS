from django.shortcuts import render, redirect
from .models import supplier
from django.contrib import messages


# Create your views here.
def index(request):
     suppliers = supplier.objects.all()
     supps = supplier.objects.count()
     context = {
          'suppliers': suppliers, 
          'supps': supps   
     }

     return render(request, 'supplier/index.html', context)

# Create function 
def add_supplier(request):
    if request.method == 'GET':
       return render(request, 'supplier/addsupplier.html')

    if request.method =='POST':
       supplier_name = request.POST['supplier_name']
       supplier_address = request.POST['supplier_address']
       supplier_phone = request.POST['supplier_phone']
       #supplier_created = request.POST['supplier_created']
       #supplier_updated = request.POST['supplier_updated']   

    supplier.objects.create(supplier_name=supplier_name, supplier_address=supplier_address, supplier_phone=supplier_phone)
    messages.success(request, 'New supplier has been added successfully!,')
    return redirect('supplier')

# Edit function 
def edit_supplier(request, id):

    edit_supps = supplier.objects.all()
    context = {
        'edit_supps': edit_supps
    }
    if request.method == 'GET':
       return render(request,'supplier/editsupplier.html', context)

    if request.method == 'POST': 
       supplier_name = request.POST['supplier_name']
       supplier_address = request.POST['supplier_address']
       supplier_phone = request.POST['supplier_phone']

