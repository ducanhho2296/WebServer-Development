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

def get_all_items():
    db = get_database()
    return db['items'].find({})

def search_items(query: str):
    db = get_database()
    items = db['items'].find({"name": {"$regex": query}})
    return list(items)

def get_item_by_id(item_id: str):
    db = get_database()
    return db['items'].find_one({'_id': item_id})

#movies
def search_movies(title: str):
    db = get_database()
    movies = db['movies'].find({"title":{"$regex": title, "$options": "i"}})
    return list(movies)


if __name__ == '__main__':
    print(search_movies('Inception'))