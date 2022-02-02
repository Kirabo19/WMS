from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'supplier/index.html')

def add_supplier(request):
    return render(request, 'supplier/addsupplier.html')