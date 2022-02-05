from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="customer"),
    path('add_customer',views.add_customer, name="add_customer"),
    path('edit_customer/<int:id>',views.edit_customer, name="edit_customer")
]