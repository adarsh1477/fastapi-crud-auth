from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas

def showall(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show_specific(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"no Blog with {id} exists")
    return blog


def update(id:int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} does not exist")
    blog.update(request.dict())
    db.commit()
    return 'Updation Successful'

def destroy_all(db: Session):
    blogs_delete = db.query(models.Blog).delete(synchronize_session=False)
    if blogs_delete == 0:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blogs exist to delete")
    db.commit()
    return "All blogs deleted successfully"

def destroy(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} does not exist")
    blog.delete(synchronize_session=False)
    db.commit()
    db.refresh(blog)
    return f" blog with id {id} deleted successfully"


