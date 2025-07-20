from fastapi import FastAPI
from prisma import Prisma
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model for Post
class CreatePost(BaseModel):

    title: str
    content: Optional[str] = None
    published: bool = False

# Database connection setup
@app.on_event("startup")
async def startup():
    app.state.db = Prisma()
    await app.state.db.connect()

@app.on_event("shutdown")
async def shutdown():
    if hasattr(app.state, 'db'):
        await app.state.db.disconnect() 


# Endpoint definitions
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    posts = await app.state.db.post.find_many()
    return {"posts": posts}


# create posts
@app.post("/posts")
async def create_post(post_data: CreatePost):
    post = await app.state.db.post.create(
        data=post_data.model_dump(exclude_none=True)  # Use model_dump to convert Pydantic model to dict
    )
    return {"post": post}
