from pydantic import BaseModel
from typing import List

class BaseBlog(BaseModel):
    title : str
    body: str

class Blog(BaseBlog):
    class Config():
        orm_mode = True

class Student(BaseModel):
    Roll_no : int
    House : str
    Standard : str

class User(BaseModel):

    name : str
    email : str
    password: str

    class Config():
        orm_mode = True
    

class ShowStudents(BaseModel):
    Roll_no : int
    House : str
    class Config():
        orm_mode = True

class ShowUsers(BaseModel):
    name : str
    email : str
    blogs : List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title : str
    body : str

    creator: ShowUsers
    class Config():
        orm_mode = True

class Login(BaseModel):

    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
