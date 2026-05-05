from fastapi import FastAPI,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import engine, get_db
import models, schemas
from auth import hash_password, verify_password, create_access_token, get_current_user

models.Base.metadata.create_all(bind=engine)
app= FastAPI()

@app.post("/register",response_model=schemas.UserResponse)
def register(user:schemas.UserCreate,db:Session= Depends(get_db)):
    existing_user= db.query(models.User).filter(models.User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email Registered already")
    hashed= hash_password(user.password)
    new_user= models.User(username= user.username, password= hashed, email= user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm= Depends(),db:Session=Depends(get_db)):
    user= db.query(models.User).filter(models.User.email==form_data.username).first()
    if not user:
        raise HTTPException(status_code=400,detail="Invalid Credential")
    if not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=400,detail="Invalid Credential")
    token= create_access_token (data= {"sub":user.email})
    return {"access_token": token,"token_type": "Bearer"}

@app.get("/posts",response_model=list[schemas.PostResponse])
def get_posts(db:Session=Depends(get_db)):
    return db.query(models.Post).all()                                                                                                 

@app.get("/posts/{post_id}",response_model=schemas.PostResponse)
def get_post(post_id: int, db: Session= Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="Post is not created yet")
    return post

@app.post("/posts",response_model=schemas.PostResponse)
def create_post(post:schemas.PostCreate,db:Session=Depends(get_db),current_user= Depends(get_current_user)):
    new_post = models.Post(title=post.title, content=post.content, published=post.published, owner_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.put("/posts/{post_id}",response_model=schemas.PostResponse)
def update_post(post_id: int, updates: schemas.PostUpdate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    post= db.query(models.Post).filter(models.Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403,detail="Not authorized")
    for key,value in updates.model_dump(exclude_unset=True).items():
        setattr(post,key,value)
    db.commit()
    db.refresh(post)
    return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    post= db.query(models.Post).filter(models.Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403 ,detail="Not authorized" )
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}