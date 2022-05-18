from fastapi import FastAPI
from routers import  inference_, train_

app = FastAPI()

app.include_router(train_.router)
app.include_router(inference_.router)

@app.get("/")
async def root():
    return {"message": "Hello !"}
