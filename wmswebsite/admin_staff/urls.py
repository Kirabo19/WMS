from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="admin_staff"),

    path('/add-user',views.add_user, name="add-user"),

    path('edituser/<int:id>',views.edit_user, name="edituser")
]