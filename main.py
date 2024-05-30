from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return {"hello":"world"}

@app.get('/item/{item_id}')
async def items(item_id):
    return {'item_id': item_id}