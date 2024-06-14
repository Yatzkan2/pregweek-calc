from pydantic import BaseModel
from datetime import date, timedelta

class Request(BaseModel):
    conceiving_date: date 
    last_date: date

class Response(Request):
    weeks: int
    days: int