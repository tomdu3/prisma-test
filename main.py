from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root() -> Union[str, dict]:
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    return {"item_id": item_id, "query": q}


