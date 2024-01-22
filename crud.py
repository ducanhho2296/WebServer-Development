from database import get_database
from models import Item

#CRUD (Create, Read, Update, Delete) operations for MongoDB
def add_item(item: Item):
    db = get_database()
    db['items'].insert_one(item.model_dump())

def update_item(item_id: str, item: Item):
    db = get_database()
    db['items'].update_one({'_id': item_id}, {'$set': item.model_dump()})

def delete_item(item_id: str):
    db = get_database()
    db['items'].delete_one({'_id': item_id})
