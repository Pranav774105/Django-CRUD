from django.db import models

# Create your models here.

class Order(models.Model):
    oid = models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length=20)
    prod_quan = models.IntegerField()
    del_date = models.DateField()
    del_address = models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=20)
