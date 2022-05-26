from enum import unique
from wsgiref import validate
from .models import Items, List, Invoice
from rest_framework import serializers


####################     ITEM SERIALIZER     ####################
class Item_Serialiser(serializers.ModelSerializer):  
  class Meta:
    model = Items
    fields = ['item_code','item_name','item_quant','item_price','expiry_date']
    ordering = ["item_code"]

  def create(self,validate_data):
    return Items.objects.create(**validate_data)

  def update(self, instance, validated_data):
    instance.item_name = validated_data['item_name']
    instance.item_quant = validated_data['item_quant']
    instance.item_price = validated_data['item_price']
    instance.expiry_data = validated_data['expiry_date']
    instance.save()
    return instance


####################     LIST SERIALIZER     ####################
class List_Serialiser(serializers.ModelSerializer):
  class Meta:
      model = List
      fields = ['item_code','item_quant','price_per_unit','item_name','item_price']
      ordering = ['item_code']

  def create(self,validate_data):
    return List.objects.create(**validate_data) 
  
  # def update(self, instance, validated_data):
  #   instance.item_quant = validated_data['item_quant']
  #   instance.item_price = validated_data['item_price']
  #   instance.save()
  #   return instance


####################     INVOICE SERIALIZER     ####################
class Invoice_Serialiser(serializers.ModelSerializer):
  items = List_Serialiser(many=True, read_only=True)

  class Meta:
    model = Invoice
    fields = ['UID','cust_name','address','items']


  def create(self,validate_data):
    return Invoice.objects.create(**validate_data)
  
  # def update(self, instance, validated_data):
  #   instance.cust_name = validated_data['cust_name']
  #   instance.address = validated_data['address']
  #   instance.save()
  #   return instance
