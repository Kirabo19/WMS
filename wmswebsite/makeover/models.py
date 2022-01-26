from django.db import models

# Create your models here.
class makeover(models.Model):
    website = models.CharField(max_length=250)
    description = models.TextField()
    keyword = models.TextField()
    i_email = models.EmailField()
    fb = models.CharField(max_length=250)
    tw = models.CharField(max_length=250)
    yb = models.CharField(max_length=250)

    def __str__(self):
        return self.website

