from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from model.item import ItemCreate

from db.item import createItem, findItemsBySeller

from utils.error import create_error_response

item_router = APIRouter()

@item_router.post("/create")
async def create_item_route(item : ItemCreate):
    try:
        id = createItem(item)
        content = {
            "item" : id
        }
        return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        create_error_response(e) 
        
        
@item_router.get("/find_by_seller/{seller_id}")
async def get_seller_item(seller_id : str):
    try:
        items = findItemsBySeller(seller_id)
        content = {
            "items" : items 
        }
        return JSONResponse(content = content, status_code = status.HTTP_200_OK)
    except Exception as e:
        create_error_response(e) 