# Utitlity Library
import io
import json
import random
from datetime import date
from urllib import response
from urllib.request import Request
from xhtml2pdf import pisa
import requests
import socket

# Django Libraries
from django.http import JsonResponse,HttpResponse,Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.views.generic import ListView

# Rest Framework Libraries
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Importing Custom Functions
from .serializers import Item_Serialiser, Invoice_Serialiser
from .models import Items, Invoice, List


# HOME PAGE VIEW
def index(request):
  context = {'data':'hello'}
  return render(request,'index.html',context)

def delete(request):
  Invoice.objects.all().delete()
  msg = {'Response':"Data of Invoice Deleted"}
  return JsonResponse(msg)

class invoiceList(ListView):
  model = Invoice
  context_object_name = 'invoice_list'
  template_name = "main.html"
  queryset = Invoice.objects.all()
  # def get_queryset(self):
  #   return Invoice.objects.all()

def download(request,*args,**kwargs):
  pk = kwargs.get('pk')
  try:
    HOSTNAME = request.get_host()
  except:
    HOSTNAME = 'localhost'
  invoice = requests.get('http://'+HOSTNAME+'/invoice/'+pk)
  template_path = 'generate_pdf.html'
  context = {'invoice':invoice.json()}
  response = HttpResponse(content_type = 'application/pdf')
  response['Content-Disposition'] = 'filename="report.pdf"'

  template = get_template(template_path)
  html = template.render(context)

  pisa_status = pisa.CreatePDF(html,dest=response)
  if(pisa_status.err):
    return HttpResponse('ERROR!!!')
  return response


# HANDLING DATA API
class data(APIView):

  # GET request for data
  def get(self,request,*args,**kwargs):
    if(len(kwargs)>0):
      print(kwargs['pk'])
      items = Items.objects.get(item_code = int(float(kwargs['pk'])))
      serialize = Item_Serialiser(items)
    else:
      items = Items.objects.all()
      serialize = Item_Serialiser(items,many=True)
    return Response(serialize.data)


  # POST request for data (ie adding new items)
  @csrf_exempt
  def post(self,request,*args,**kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serialise = Item_Serialiser(data = python_data)
    if serialise.is_valid():
      serialise.save()
      msg = {'Response' : 'Data Saved'}
      return Response(msg)
    return Response(serialise.errors)

  # PUT request for data
  @csrf_exempt
  def put(self,request,*args,**kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    instance = Items.objects.get(item_code = python_data.get('item_code'))
    serialise = Item_Serialiser(instance,data = python_data)
    if serialise.is_valid():
      serialise.save()
      msg = {'Response' : 'Data Saved'}
      return Response(msg)
    return Response(serialise.errors)


# HANDLING INVOICE API
class invoice(APIView):

  # GET request for invoice
  def get(self,request,*args,**kwargs):
    if(len(kwargs)>0):
      invoice = Invoice.objects.get(UID = kwargs['pk'])
      serialize = Invoice_Serialiser(invoice)
    else:
      invoice = Invoice.objects.all()
      serialize = Invoice_Serialiser(invoice,many=True)
    return Response(serialize.data)
    # return JsonResponse(serialize.data,safe=False)
    # return HttpResponse(serialize.data)
  

  # POST request for invoice
  @csrf_exempt
  def post(self,request,*args,**kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)

    # Generate Unique Invoice ID
    name = python_data['cust_name']
    address = python_data['address']
    inv_id = ''.join(address.split(' '))[:3]+str(date.today().year)+str(random.randint(100,100000))
    info = {'UID':inv_id, 'cust_name' : name, 'address': address}
    invoice = Invoice.objects.create(**info)
    
    for item in python_data['items']:

      # Check if Item is available
      item_available = Items.objects.get(item_code = item['item_code'])
      if int(item_available.item_quant)<int(item['item_quant']):
        return Response({'Response':f"Item {item_available.item_code} Unavailable"})
      Items.objects.filter(item_code = item_available.item_code).update(item_quant=item_available.item_quant-int(item['item_quant']))

      # Calculate Total Price
      item['item_price'] = int(item['item_quant'])*int(item_available.item_price)
      item['price_per_unit'] = int(item_available.item_price)
      item['item_name'] = item_available.item_name
      item['invoice_id'] = invoice
      List.objects.create(**item)
    
    # Saving valid invoice
    serialiser = Invoice_Serialiser(data = invoice.__dict__)
    if serialiser.is_valid():
      serialiser.save()
      msg = {'Response' : 'Data Saved'}
      return Response(msg)
    return Response(serialiser.errors)

  
  # PUT request for invoice
  @csrf_exempt
  def put(self,request,*args,**kwargs):

    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)

    # Generate Unique Invoice ID
    inv_id = python_data.get('UID')

    #deleting Previous Data
    Invoice.objects.get(UID=inv_id).delete()


    # Creating new instance
    info = {'UID':inv_id, 'cust_name' : python_data['cust_name'], 'address': python_data['address']}
    invoice = Invoice.objects.create(**info)
    
    for item in python_data['items']:

      # Check if Item is available
      item_available = Items.objects.get(item_code = item['item_code'])
      if int(item_available.item_quant)<int(item['item_quant']):
        return Response({'Response':f"Item {item_available.item_code} Unavailable"})
      Items.objects.filter(item_code = item_available.item_code).update(item_quant=item_available.item_quant-int(item['item_quant']))

      # Calculate Total Price
      item['item_price'] = int(item['item_quant'])*int(item_available.item_price)
      item['price_per_unit'] = int(item_available.item_price)
      item['item_name'] = item_available.item_name
      item['invoice_id'] = invoice
      List.objects.create(**item)
    
    # Saving Valid Put request
    serialiser = Invoice_Serialiser(data = invoice.__dict__)
    if serialiser.is_valid():
      serialiser.save()
      msg = {'Response' : 'Data Saved'}
      return Response(msg)
    return Response(serialiser.errors)













'''
Code under Development:->
serialiser = Invoice_Serialiser(invoice,python_data)

prev_list = List.objects.filter(invoice_id = id)
new_list = [list_item for list_item in python_data['items']]

for item in python_data['items']:
  print(item)
  prev_item = List.objects.get(list_id = item.get('list_id'))
  item['item_price'] = int(item['item_quant'])*int(prev_item.item_price)
  item_serialise = List_Serialiser(prev_item,item)
  if item_serialise.is_valid():
    item_serialise.save()
    msg = {'Response','Item Updated'}
    return Response(msg)
  else:
    return Response(serialiser.errors)

if serialiser.is_valid():
  serialiser.save()
  msg = {'Response' : 'Data Saved'}
  return Response(msg)
# return HttpResponse(request,serialiser.errors)
# return JsonResponse(serialiser.errors,safe= False)
return Response(serialiser.errors)
'''
