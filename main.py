from fastapi import FastAPI, HTTPException
from db import *
from models import *
import requests
import json
from typing import List



app = FastAPI()


# def clean_request(request: json):
#     for i in request["value"]:
#         if "@odata.etag" in i:
#             del i["@odata.etag"]


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
def create_or_update_item(item: Item):
    cursor = conn.cursor()
    query = '''INSERT INTO itemledgerentries (etag, entry_no, item_no, posting_date,
     entry_type, source_no, document_no, description, 
    location_code, quantity, unit_of_measure_code, 
    item_category_code, document_type, 
    document_line_no, order_type ,
    order_no, order_line_no, cost_amount_actual, cost_amount_expected) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE 
    item_no = VALUES(item_no), posting_date = VALUES(posting_date), entry_type = VALUES(entry_type), 
    source_no = VALUES(source_no), document_no = VALUES(document_no), description = VALUES(description), 
    location_code = VALUES(location_code), quantity = VALUES(quantity), unit_of_measure_code = VALUES(unit_of_measure_code), 
    item_category_code = VALUES(item_category_code), document_type = VALUES(document_type), 
    document_line_no = VALUES(document_line_no), order_type = VALUES(order_type), 
    order_no = VALUES(order_no), order_line_no = VALUES(order_line_no), cost_amount_actual = VALUES(cost_amount_actual), cost_amount_expected= VALUES(cost_amount_expected)'''
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
def create_or_update_capacity(capacity: Capacity):
    cursor = conn.cursor()
    query = """INSERT INTO capacityledgerentries (etag, entry_no, posting_date, item_no, type , no, document_no, description, routing_no,
    routing_reference_no, operation_no, output_quantity, unit_of_measure_code, 
    scrap_quantity, setup_time, run_time, stop_time, cap_unit_of_measure_code, 
    starting_time, ending_time, order_type , order_no, order_line_no, employeeno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE posting_date = VALUES(posting_date), item_no = VALUES(item_no), type = VALUES(type), no = VALUES(no), document_no = VALUES(document_no), description = VALUES(description), routing_no = VALUES(routing_no), routing_reference_no = VALUES(routing_reference_no), operation_no = VALUES(operation_no), output_quantity = VALUES(output_quantity), unit_of_measure_code = VALUES(unit_of_measure_code), scrap_quantity = VALUES(scrap_quantity), setup_time = VALUES(setup_time), run_time = VALUES(run_time), stop_time = VALUES(stop_time), cap_unit_of_measure_code = VALUES(cap_unit_of_measure_code), starting_time = VALUES(starting_time), ending_time = VALUES(ending_time), order_type = VALUES(order_type), order_no = VALUES(order_no), order_line_no = VALUES(order_line_no), employeeno = VALUES(emplyenoo)"""
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
        create_or_update_item(x)
    return data_item[0]


# route to create all items
@app.post("/capacities", response_model=Capacity)
def create_capacities(data_capacity: list[Capacity]):
    for x in data_capacity:
        create_or_update_capacity(x)
    return data_capacity[0]


# Route to read all items
@app.get("/items")
def read_items():
    cursor = conn.cursor()
    query = "SELECT * FROM itemledgerentries"
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()
    return items


# Route to read all items
@app.get("/capacities")
def read_items():
    cursor = conn.cursor()
    query = "SELECT * FROM capacityledgerentries"
    cursor.execute(query)
    capacities = cursor.fetchall()
    cursor.close()
    return capacities

    #provare su metabase

