from fastapi import FastAPI
import model_test

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/item/all")
async def items_all():
    return {"message": "here are all the items"}


@app.get("/item/{item_id}")
async def item(item_id: int):
    return {"message": "here is ur item id: " + str(item_id)}
