from pydantic import BaseModel, Field, TypeAdapter
# Pydantic model to define the schema of the data
class Item(BaseModel):
    etag:str = Field(alias="@odata.etag", default=None)
    id:str
    postingdate:str
    entrytype:str
    costamountactual:float
    costamountexpected:float
    documentno:str

class Capacity(BaseModel):
    etag:str = Field(alias="@odata.etag", default=None)
    id:str
    postingdate:str
    orderno:str
    type:str
    no:str
    operationno:str
    itemno:str
    description:str
    quantity:float
    outputquantity:float
    scrapquantity:float
    directcost:float	