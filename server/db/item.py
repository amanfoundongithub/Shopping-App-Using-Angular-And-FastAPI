from db.connection import create_connection

from model.item import ItemCreate

def createItem(item : ItemCreate):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = f"INSERT INTO items (itemName, itemCode, itemQuantity, itemPrice, itemType, itemDescription, itemSeller, itemPic)\
            values ('{item.itemName}', '{item.itemCode}', '{item.itemQuantity}', '{item.itemPrice}', '{item.itemType}'\
            , '{item.itemDescription}', '{item.itemSeller}', '{item.itemPic}')\
            RETURNING id;"
            cursor.execute(query) 
            item_id = cursor.fetchone()[0]
            connection.commit()
            print(f"Item {item.itemName} added to the database") 
            return item_id
        except Exception as e:
            print(f"Error : {e}")
            raise ConnectionError(e) 
        finally:
            cursor.close()
            connection.close()

def findItemsBySeller(seller_id : str):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = f"SELECT * from items where itemSeller='{seller_id}';"
            cursor.execute(query)
            items = cursor.fetchall()
            for i in range(len(items)):
                items[i] = list(items[i])
                items[i][3] = float(items[i][3])
            return items 
        except Exception as e:
            print(f"Error : {e}")
            raise ConnectionError(e)
        finally:
            connection.close() 
