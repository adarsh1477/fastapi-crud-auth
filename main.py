from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return 'heyy'

@app.get('/blog')
def blog(limit = 10,published : bool = True, sort : Optional[str] = None):
    if published:
        return {"data" : f'{limit} published blogs from db'}
    else:
        return {"data" : f'{limit} blogs from db'}

@app.get('/about')
def about():
    return {"data":"about page"}

@app.get('/blog/unpublished')
def unpublished():
    return {"data": "unpublished records"}

@app.get('/blog/{id}')
def blog_show(id : int):
    return {"blog": id}

@app.get('/blog/{id}/comments')
def blog_show():
    return {"comments": "1,2,3,4"}

class Blog(BaseModel):
    title : str = "Addy book"
    author: str = "Adarsh"
    published:bool = True

@app.post('/blog')
def create_blog(request : Blog):
    return {"data": f"The blog is created with title {request.title} "
                f"by {request.author} and {request.published}"}

