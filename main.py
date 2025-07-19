from fastapi import FastAPI
from prisma import Prisma


app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.db = Prisma()
    await app.state.db.connect()

@app.on_event("shutdown")
async def shutdown():
    if hasattr(app.state, 'db'):
        await app.state.db.disconnect() 

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    posts = await app.state.db.post.find_many()
    return {"posts": posts}


