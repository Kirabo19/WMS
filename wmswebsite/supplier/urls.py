from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="supplier"),

    path('add_supplier',views.add_supplier, name="add_supplier"),
    
    path('edit_supplier/<int:id>',views.edit_supplier, name="edit_supplier"),

    path('delete_supplier/<int:id>',views.delete_supplier, name="delete_supplier")
  
]