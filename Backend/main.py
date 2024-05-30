from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/pastebin/')
def root():
    return 'hello world'