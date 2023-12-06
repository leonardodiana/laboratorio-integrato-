from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import *
import requests
import json

app = FastAPI()

#request


r=requests.get('https://fakerapi.it/api/v1/custom?_quantity=50&id=uuid&postingdate=date&entrytype=word&documentno=buildingNumber&itemno=postcode&quantity=number&costamountactual=number&costamountexpected=number')
dict=r.json()
data=dict['data']
print(data)

# Pydantic model to define the schema of the data
class Item(BaseModel):
    id:str
    postingdate:str
    entrytype:str
    documentno:str
    itemno:str
    quantity:int
    costamountactual:int
    costamountexpected:int

# Route to create an item
@app.post("/item/", response_model=Item)
def create_item(item: Item):
    cursor = conn.cursor()
    query = "INSERT INTO item_ledger_entry (id, postingdate, entrytype, documentno, itemno, quantity, costamountactual, costamountexpected) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (item.id, item.postingdate, item.entrytype, item.documentno, item.itemno, item.quantity, item.costamountactual, item.costamountexpected))
    conn.commit()
    item.id = cursor.lastrowid
    cursor.close()
    return item

#route to create all items
@app.post("/items", response_model=Item)
def create_items(data:list[Item]):
    for x in data:
        create_item(x)
    return data


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