from urllib import response
import requests 
import json
import io
from datetime import datetime
URL = "http://127.0.0.1:8000/data/"

req = requests.get(url = URL)

# Get details of response
# print(req.dir)

stream = io.BytesIO(req.content)
json_data = json.load(stream)

expired_item = []
item_shortage = []
item_unavailable = []



for item in json_data:
  if item.get('expiry_date')[:10]<str(datetime.today())[:10]:
    expired_item.append(item.get('item_code'))
  elif item.get('item_quant')<100 and item.get('item_quant')>0:
    item_shortage.append(item.get('item_code'))
  elif item.get('item_quant')==0:
    item_unavailable.append(item.get('item_code'))
  
print(expired_item)
print(item_shortage)
print(item_unavailable)