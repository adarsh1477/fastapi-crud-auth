from fastapi import HTTPException,status
from .. import models,schemas
from sqlalchemy.orm import Session
from ..hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_all(db: Session):
    user = db.query(models.User).all()
    return user


def show_specific(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    return user

def update(id:int, request : schemas.User, db):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    
    data = request.dict()
    data["password"] = Hash.encrypt(request.password)

    user.update(data)
    db.commit()
    return user.first()


def delete(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    user.delete(synchronize_session=False)

    db.commit()
    return "User Deleted"