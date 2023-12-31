from datetime import datetime
from typing import List
from pydantic import BaseModel

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime


# class UserBase(BaseModel):
#     email:str
#     username:str


# class PostBase(BaseModel):
#     description: str | None = None
#     title: str 
#     content: str

# class PostCreate(PostBase):
#     pass

# class PostDb(PostBase):
#     id: str
#     published_date: datetime
#     tags: List = []
    
#     class Config:
#         orm_mode = True

