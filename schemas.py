from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username:str
    email:str
    password:str
    
class UserResponse(BaseModel):
    id:int
    username:str
    email:str
    is_active:bool
    class Config:
        from_attributes= True
    
class PostCreate(BaseModel):
    title:str
    content:str
    published: Optional[bool]=True
    
class PostResponse(BaseModel):
    id:int
    title:str
    content:str
    published:bool
    owner_id:int
    class Config:
        from_attributes= True

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None