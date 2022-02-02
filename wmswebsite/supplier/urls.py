from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="supplier"),

    path('add_supplier',views.add_supplier, name="add_supplier"),
    
    path('edit_supplier',views.edit_supplier, name="edit_supplier")
  
]