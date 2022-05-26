from django.urls import path, include
from .views import index,delete,download,invoiceList,data,invoice
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # url for api auth
    path('api-auth/', include('rest_framework.urls')),
    # api for getting data of an item
    path('data/<str:pk>/',data.as_view(),name='api_request'),
    # api for getting data of all items in warehouse
    path('data/',data.as_view(),name='data_request'),
    # api for getting data of an invoice
    path('invoice/<str:pk>/',invoice.as_view(),name='invoice_request'),
    # api for getting data of all invoice
    path('invoice/',invoice.as_view(),name='invoice_request'),
    # api for getting pdf of invoice of given id
    path('invoice/download/pdf/', invoiceList.as_view(), name='invoice_list'),
    path('invoice/download/pdf/<str:pk>/',download,name='invoice'),
    # delete database
    path('delete/',delete,name='delete_data'),
    # api for home page
    path('',index,name='index')
]
