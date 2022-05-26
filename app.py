from urllib import response
import requests 
import json
import io
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
  if item.item_quant<10:
    item_shortage.append(item.item_code)
  elif item.item_quant==0:
    item_unavailable.append(item.item_code)
  