# Union to use different data types like strings or list
from typing import Union

from fastapi import FastAPI
#BaseModel from pydantic is used to define data objects
from pydantic import BaseModel

# Declare the data object with it's component and type
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int

# Save items from POST method in the memory
items = {}
app = FastAPI()

# get method
@app.get("/")
async def root():
    return {"message": "API is running"}
# This allows sending of data (our TaggedItem) via POST to API
@app.post("/items/")
async def create_item(item: TaggedItem):
    items[item.item_id] = item
    return item

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int =1):
    try:
        item = items[item_id]
    except:
        return "Item not found"
    return {"fetch": f"Fetched {item.name} with qty of {count}."}