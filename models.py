from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index= True)
    username= Column(String, index=True, nullable=False)
    email= Column(String,nullable= False,unique= True)
    password= Column(String,nullable= False)
    is_active= Column(Boolean, default=True)
    posts = relationship("Post", back_populates= "owner")
    
class Post(Base):
    __tablename__= 'posts'
    id= Column(Integer,primary_key=True, index=True)
    title= Column(String,index=True,nullable=False)
    content= Column(String,nullable=False)
    published= Column(Boolean,default=True)
    owner_id= Column(Integer,ForeignKey("users.id"))
    owner= relationship("User", back_populates= "posts")









