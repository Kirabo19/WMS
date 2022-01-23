from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="System_Identity")
    path('add-Sys', views.add_sys, name="add-sys")


]