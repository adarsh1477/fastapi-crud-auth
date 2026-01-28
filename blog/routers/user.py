from fastapi import APIRouter,Depends
from .. import schemas,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import userRepo

router=APIRouter(
    prefix='/Users',
    tags=['User']
)

@router.get('',response_model=list[schemas.User])
def get_all_user(db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return userRepo.show_all(db)


@router.post('',response_model=schemas.ShowUsers)
def create_user(request:schemas.User ,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return userRepo.create(request,db)


@router.get('/{id}',response_model=schemas.ShowUsers)
def get_user(id:int, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return userRepo.show_specific(id,db)


@router.put('/{id}')
def update_user(id,request:schemas.User, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return userRepo.update(id,request,db)

@router.delete('/{id}')
def delete_User(id: int, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return userRepo.delete(id,db)