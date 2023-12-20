from fastapi import FastAPI, HTTPException
from db import *
from models import *
import requests
import json
from typing import List



app = FastAPI()


def clean_request(request: json):
    for i in request["value"]:
        if "@odata.etag" in i:
            del i["@odata.etag"]


# request


#r=requests.get('https://dummyjson.com/products/1')
#dict=r.json()
# data_item=dict['data']
#print(r.content)


# r=requests.get('https://fakerapi.it/api/v1/custom?_quantity=50&id=uuid&postingdate=date&documentno=word&type=word&no=word&operationno=word&itemno=word&description=word&quantity=number&outputquantity=number&scrapquantity=number&directcost=number')
# dict=r.json()
# data_capacity=dict['data']
# print(data_capacity)


# Route to create an item record
@app.post("/item/", response_model=Item)
def create_item(item: Item):
    cursor = conn.cursor()
    query = '''INSERT INTO itemledgerentries (etag, entry_no, item_no, posting_date,
     entry_type, source_no, document_no, description, 
    location_code, quantity, unit_of_measure_code, 
    item_category_code, document_type, 
    document_line_no, order_type ,
     order_no, order_line_no, cost_amount_actual, cost_amount_expected) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(
        query,
        (
            item.etag,
            item.entry_no,
            item.item_no,
            item.posting_date,
            item.entry_type,
            item.source_no,
            item.document_no,
            item.description,
            item.location_code,
            item.quantity,
            item.unit_of_measure_code,
            item.item_category_code,
            item.document_type,
            item.document_line_no,
            item.order_type,
            item.order_no,
            item.order_line_no,
            item.cost_amount_actual,
            item.cost_amount_expected
        ),
    )
    conn.commit()
    cursor.close()
    return item


# Route to create a capacity record
@app.post("/capacity", response_model=Capacity)
def create_capacity(capacity: Capacity):
    cursor = conn.cursor()
    query = """INSERT INTO capacityledgerentries (etag, entry_no, posting_date, item_no, type , no, document_no, description, routing_no,
    routing_reference_no, operation_no, output_quantity, unit_of_measure_code, 
    scrap_quantity, setup_time, run_time, stop_time, cap_unit_of_measure_code, 
    starting_time, ending_time, order_type , order_no, order_line_no, employeeno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(
        query,
        (
            capacity.etag,
            capacity.entry_no,
            capacity.posting_date,
            capacity.item_no,
            capacity.type,
            capacity.no,
            capacity.document_no,
            capacity.description,
            capacity.routing_no,
            capacity.routing_reference_no,
            capacity.operation_no,
            capacity.output_quantity,
            capacity.unit_of_measure_code,
            capacity.scrap_quantity,
            capacity.setup_time,
            capacity.run_time,
            capacity.stop_time,
            capacity.cap_unit_of_measure_code,
            capacity.starting_time,
            capacity.ending_time,
            capacity.order_type,
            capacity.order_no,
            capacity.order_line_no,
            capacity.employeeno
        ),
    )
    conn.commit()
    cursor.close()
    return capacity


# route to create all items
@app.post("/items", response_model=Item)
def create_items(data_item: list[Item]):
    for x in data_item:
        create_item(x)
    return data_item[0]


# route to create all items
@app.post("/capacities", response_model=Capacity)
def create_capacities(data_capacity: list[Capacity]):
    #ta=TypeAdapter(List[Capacity])
    #data=ta.validate_python(data_capacity)
    for x in data_capacity:
        create_capacity(x)
    return data_capacity[0]


# Route to read all items
@app.get("/items")
def read_items():
    cursor = conn.cursor()
    query = "SELECT * FROM item_ledger_entry"
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()
    return items
    # if item is None:
    # raise HTTPException(status_code=404, detail="Item not found")
    # return {"id": item[0], "name": item[1], "description": item[2]}


# Route to read all items
@app.get("/capacities")
def read_items():
    cursor = conn.cursor()
    query = "SELECT * FROM capacity_ledger_entry"
    cursor.execute(query)
    capacities = cursor.fetchall()
    cursor.close()
    return capacities