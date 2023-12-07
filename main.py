from fastapi import FastAPI, HTTPException
from db import *
from models import *
import requests
import json


app = FastAPI()

#request


r=requests.get('https://fakerapi.it/api/v1/custom?_quantity=50&id=uuid&postingdate=date&entrytype=word&documentno=buildingNumber&itemno=postcode&quantity=number&costamountactual=number&costamountexpected=number')
dict=r.json()
data_item=dict['data']
#print(data_item)



r=requests.get('https://fakerapi.it/api/v1/custom?_quantity=50&id=uuid&postingdate=date&documentno=word&type=word&no=word&operationno=word&itemno=word&description=word&quantity=number&outputquantity=number&scrapquantity=number&directcost=number')
dict=r.json()
data_capacity=dict['data']
print(data_capacity)

# Route to create an item record
@app.post("/item/", response_model=Item)
def create_item(item: Item):
    cursor = conn.cursor()
    query = "INSERT INTO item_ledger_entry (id, postingdate, entrytype, documentno, itemno, quantity, costamountactual, costamountexpected) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (item.id, item.postingdate, item.entrytype, item.documentno, item.itemno, item.quantity, item.costamountactual, item.costamountexpected))
    conn.commit()
    item.id = cursor.lastrowid
    cursor.close()
    return item

# Route to create a capacity record
@app.post("/capacity", response_model=Capacity)
def create_item(capacity: Capacity):
    cursor = conn.cursor()
    query = "INSERT INTO capacity_ledger_entry (id, postingdate, documentno, type, no, operationno, itemno,	description, quantity, outputquantity, scrapquantity, directcost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (capacity.id, capacity.postingdate, capacity.documentno, capacity.type, capacity.no, capacity.operationno, capacity.itemno, capacity.description, capacity.quantity, capacity.outputquantity, capacity.scrapquantity, capacity.directcost))
    conn.commit()
    capacity.id = cursor.lastrowid
    cursor.close()
    return capacity

#route to create all items
@app.post("/items", response_model=Item)
def create_items(data_item:list[Item]):
    for x in data_item:
        create_item(x)
    return data_item

#route to create all items
@app.post("/capacities", response_model=Capacity)
def create_items(data_capacity:list[Capacity]):
    for x in data_capacity:
        create_item(x)
    return data_capacity


# Route to read all items
@app.get("/items")
def read_items():
    cursor = conn.cursor()
    query = "SELECT * FROM item"
    cursor.execute(query)
    item = cursor.fetchall()
    cursor.close()
    return item
    #if item is None:
        #raise HTTPException(status_code=404, detail="Item not found")
    #return {"id": item[0], "name": item[1], "description": item[2]}