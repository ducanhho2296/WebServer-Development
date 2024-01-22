from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str 
    

class Movie(BaseModel):
    title:str  #seach for the name of movie