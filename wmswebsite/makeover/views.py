from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'makeover/index.html')
    

def add_system(request):
    return render(request, 'makeover/add_system.html')