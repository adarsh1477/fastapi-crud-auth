from fastapi import HTTPException,status
from .. import models,schemas
from sqlalchemy.orm import Session


def show_all(db: Session):
    students = db.query(models.Student).all()
    return students

def show_specific(id:int,db: Session):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"no student with {id} exists")

        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {"detail" : f"no student with {id} exists"}
    
    return student

def create(request: schemas.Student, db: Session):
    new_student = models.Student(Roll_no=request.Roll_no, House=request.House)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def update(id:int, request: schemas.Student, db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)
    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"no student with {id} exists")
    
    student.update(request.dict())
    db.commit()
    return "Updation Successful"


def delete(id:int,db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)
    if not student.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"no student with {id} exists")
    
    student.delete(synchronize_session=False)
    db.commit()
    return f" student with id {id} deleted"