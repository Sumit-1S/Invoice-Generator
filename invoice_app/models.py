from typing import Sized
from django.db import models
from django.core.validators import MinLengthValidator

# Model for storing item availble in warehouse
class Items(models.Model):
  item_code = models.CharField(max_length=4,validators=[MinLengthValidator(4)],primary_key=True)
  item_name = models.CharField(max_length=1000,default="")
  item_quant= models.IntegerField(null=False,default=0)
  item_price= models.IntegerField(null=False,default=0)
  expiry_date = models.DateTimeField(null=False)
  def __str__(self):
    return str(self.item_code)
  

# Model for Storing Invoice Details
class Invoice(models.Model):
  UID = models.CharField(primary_key=True,max_length=20)
  cust_name = models.CharField(max_length=10000,null=False)
  address = models.TextField(max_length=1000000,null=False)
  def __str__(self):
    return str(self.UID)

# Model for Storing Items belonging to a Invoice
class List(models.Model):
  invoice_id = models.ForeignKey(Invoice,related_name='items',on_delete=models.CASCADE)
  item_name = models.CharField(max_length=1000,default="")
  list_id = models.AutoField(primary_key=True)
  item_code = models.CharField(max_length=4, null=False, default="")
  item_quant= models.IntegerField(null=False,default=0)
  price_per_unit = models.IntegerField(null=False,default=0)
  item_price = models.IntegerField(null=False,default=0)
  def __str__(self):
    return str(self.list_id)
  
  