from django.db import models
from django.utils.timezone import now

# Create your models here.
class supplier(models.Model):
    supplier_name = models.CharField(max_length=225)
    supplier_address = models.CharField(max_length=225)
    supplier_phone = models.CharField(max_length=225)
    supplier_created = models.DateField(default=now)
    supplier_updated = models.DateField(default=now)

def __str__(self):
        return self.supplier_name 