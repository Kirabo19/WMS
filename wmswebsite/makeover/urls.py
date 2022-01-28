from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='makeover'),

   # path('add-Sys',views.add_system, name='add-sys')
]