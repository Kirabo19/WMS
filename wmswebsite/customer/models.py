from email.charset import Charset
from django.db import models
from django.utils.timezone import now

# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length=225)
    customer_address = models.CharField(max_length=225)
    customer_phone = models.CharField(max_length=225)
    customer_created = models.DateField(default=now)
    customer_update = models.DateField(default=now)

def __str__(self):
    return self.customer_name   