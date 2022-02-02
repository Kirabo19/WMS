from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="supplier"),
    path('add_supplier',views.add_supplier, name="add_supplier")
  
]