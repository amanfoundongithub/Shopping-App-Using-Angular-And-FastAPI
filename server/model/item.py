from pydantic import BaseModel


class ItemBase(BaseModel):
    itemName : str
    itemCode : str

    itemQuantity : int

    itemPrice : float

    itemType : str
    
    itemSeller : str

    itemDescription : str = ""
    
    itemPic : str = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmVq-OmHL5H_5P8b1k306pFddOe3049-il2A&s"
    

class ItemCreate(ItemBase):
    pass 