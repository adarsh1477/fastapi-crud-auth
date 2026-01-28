from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import studentRepo
from .. import schemas,oauth2

router = APIRouter()


@router.get('/students',response_model=List[schemas.ShowStudents], tags=['Students'])
def get_all_students(db : Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return studentRepo.show_all(db)

@router.get('/students/{id}',status_code=200, tags=['Students'])
def get_id_student(id, response: Response,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return studentRepo.show_specific(id,db)


@router.post('/students',status_code=status.HTTP_201_CREATED, tags=['Students'])
def create(request : schemas.Student,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return studentRepo.create(request,db)


@router.put('/students/{id}', tags=['Students'])
def update_student(id: int,request : schemas.Student,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return studentRepo.update(id,request,db)


@router.delete('/students/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['Students'])
def delete(id,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return studentRepo.delete(id,db)
