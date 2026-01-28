from typing import List
from fastapi import APIRouter, Depends,status
from .. import schemas,oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blogRepo

router = APIRouter()

@router.get('/blog',response_model=List[schemas.ShowBlog], tags=['Blog'])
def get_all_blogs(db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
     return blogRepo.showall(db)


@router.post('/blog', tags=['Blog'])
def create(request: schemas.Blog, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.create(request,db)


@router.get('/blog/{id}', tags=['Blog'], response_model=schemas.ShowBlog)
def get_id_blog(id: int,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.show_specific(id,db)

@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
def update(id:int,request:schemas.Blog,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  return blogRepo.update(id,request,db)

@router.delete('/blog',status_code=status.HTTP_204_NO_CONTENT, tags=['Blog'])
def delete_all(db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.destroy_all(db)

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['Blog'])
def delete(id:int,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.destroy(id,db)

