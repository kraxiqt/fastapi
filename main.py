from fastapi import FastAPI, APIRouter

app = FastAPI()

@app.get('/')
async def func():
    return 'Hello I Grey!'
