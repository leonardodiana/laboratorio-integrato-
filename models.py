from pydantic import BaseModel
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

class Capacity(BaseModel):
    id:str
    postingdate:str
    documentno:str
    type:str
    no:str
    operationno:str
    itemno:str
    description:str
    quantity:int
    outputquantity:int
    scrapquantity:int
    directcost:int	