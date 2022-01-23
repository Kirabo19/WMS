from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'System_Identity/index.html')

def add_sys(request):
    return render(request, 'System_Identity/add_sys.html')