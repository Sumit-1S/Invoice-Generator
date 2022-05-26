# Task 1: Invoice Generator
>This project is a invoice generator using different API calls as per the need. It includes adding and updating information about the items available in warehouse. It also creates invoice for the purchase made by a customer consisting of all the details of the purchased items. The invoice can be downloaded in the form of PDF for further reference.
## DATABASE
>The database consists of three different schemas ie: Item, Invoice, List.

>Items: This schema consists of details of all the registered items in the warehouse. It consists of: 
>
> - Item_code (Primary Key)
> - Item_name 
> - Item_quantity
> - Item_price
> - Expiry_date.

>Invoice: This schema consists of details regarding the Invoice that is generated. It consists of 
>
> - UID (Primary Key) : It is generated using the combination of Address, Year, Random 4 digit number
> - cust_name
> - address.

>List: This schema is used to store the information regarding the items purchased under a given Invoice. It consists of 
> - invoice_id (Foreign Key to Invoice.UID)
> - list_id (Primary Key)
> - item_name
> - item_code
> - item_quant
> - price_per_unit
> - item_price (item_price = price_per_unit*item_quant)

## DATA
>These API links are used to fetch, add, update the information of items available.

> GET API: 
> - '/data/' : is used to fetch data of all the items in the database
> - '/data/Item_code' : is used to fetch data of certain item having item code as "Item_code"

> POST API:
> 
> This link helps to add data to the database. It takes json string as input and adds data about an item in the database.
>
>It follows the following format:
>*{
        "item_code":"",
        "item_name":"",
        "item_quant":"",
        "item_price":
   }*
   
> PUT API
> 
> This link helps to update data in the database. It takes json string as input and updates data about an item in the database.
>
>It follows the following format:
>*{
        "item_code":"",
        "item_name":"",
        "item_quant":"",
        "item_price":
      }*

## INVOICE
>These API links are used to fetch, add, update the information of invoice available.

> GET API: 
> - '/invoice/' : is used to fetch data of all the invoices in the database
> - '/invoice/UID' : is used to fetch data of certain invoice having Invoice ID as "UID"

> POST API:
>
> This link helps to add invoice to the database. It takes json string as input and adds data about an invoice in the database.
>
>It follows the following format:
>*{
        "cust_name":"",
        "address":"",
        "items":[
            { 
                "item_code": "", 
                "item_quant": ""
            }, 
            ....
        ]
    }*
    
> PUT API:
>
> This link helps to update invoice in the database. It takes json string as input and updates data about an invoice in the database.
>
>It follows the following format:
>*{
        "UID": "",
        "cust_name":"",
        "address":"",
        "items":[
            { 
                "item_code": "", 
                "item_quant": ""
            }, 
            ....
        ]
    }*
## INVOICE PDF
>The invoice stored in database can be downloaded in the form of PDF using the api link
>
>*/invoice/download/pdf/* :-> Shows list of all the invoices present
>
>*/invoice/download/pdf/UID* :-> Generates the invoice in form of PDF which can be saved to a local device.
>
>For generating the PDF *xhtml2pdf* library has been used in views


# Task 2: Automated code for finding list of items expired or having a shortage
## app.py
> This consists of code which can be scheduled at 12:00 AM which returns 3 list consisting of Items_Expired, Items_having_shoratge, Items_Unavailable.
