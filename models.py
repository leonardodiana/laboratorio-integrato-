from pydantic import BaseModel, Field, TypeAdapter
# Pydantic model to define the schema of the data
class Item(BaseModel):
    etag:str = Field(alias="@odata.etag", default=None)
    entry_no:int
    item_no:str
    posting_date:str 
    entry_type:str
    source_no :str
    document_no :str
    description :str
    location_code :str
    quantity:int
    unit_of_measure_code :str
    item_category_code :str 
    document_type :str 
    document_line_no:int
    order_type :str 
    order_no :str
    order_line_no:int
    cost_amount_actual:float
    cost_amount_expected:float

class Capacity(BaseModel):
    etag:str = Field(alias="@odata.etag", default=None)
    entry_no :int
    posting_date:str
    item_no:int
    type :str
    no :str
    document_no :str 
    description :str 
    routing_no :str 
    routing_reference_no:int
    operation_no :str 
    output_quantity:int
    unit_of_measure_code :str
    scrap_quantity:int
    setup_time:int 
    run_time :int 
    stop_time :int 
    cap_unit_of_measure_code:str 
    starting_time:str
    ending_time:str
    order_type :str 
    order_no:int
    order_line_no:int
    employeeno:str
        