from fastapi import FastAPI
from schemas import *
app = FastAPI()

@app.get('/')
async def home():
    return {'msg': 'home'}

@app.post('/v1/calcweeks')
async def calcweeks(request: Request):
    d1 = request.conceiving_date
    d2 = request.last_date
    delta = d2 - d1
    weeks = delta.days//7
    days = delta.days%7
    response = Response(conceiving_date=d1, last_date=d2, weeks=weeks, days=days)
    return {'response': response}

