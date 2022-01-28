from django.shortcuts import render
from models import makeover


# Create your views here.
def index(request):
    update_makeover = makeover.objects.all()
    context = {
        'update_makeover':update_makeover
    }
    return render(request, 'makeover/index.html', update_makeover) 

def add_system(request):
    return render(request, 'makeover/add_system.html')