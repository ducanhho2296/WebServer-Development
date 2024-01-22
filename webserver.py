from fastapi import FastAPI, HTTPException
from models import Item, Movie
from crud import add_item, search_items, search_movies
from typing import List


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/add-item/")
async def add_item_endpoint(item: Item):
    add_item(item)
    return {"message": "Item added successfully"}

@app.post("/search-items/")
async def search_items_endpoint(query: str):
    items = search_items(query)
    if not items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items

#db Movies
@app.get("/search-movies/", response_model=List[Movie])
async def search_movies_endpoint(title: str):
    movies = search_movies(title)
    print(movies)
    if not movies:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movies



#open http://127.0.0.1:8000/docs 