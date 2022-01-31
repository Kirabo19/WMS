from django.db import models
from django.utils.timezone import now

# Create your models here.
class admin_staff(models.Model):
    admin_user = models.CharField(max_length=225)
    admin_password = models.CharField(max_length=225)
    admin_name =models.CharField(max_length=225)
    admin_address = models.CharField(max_length=225)
    admin_phone = models.CharField(max_length=225)
    admin_group = models.CharField(max_length=225)
    admin_date = models.DateField(default=now)
