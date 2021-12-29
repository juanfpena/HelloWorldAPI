from fastapi import FastAPI
from dateutil import parser
import datetime
from fastapi.middleware.cors import CORSMiddleware
from .functionalities.calculator import calcFunc
from .functionalities.date_fmt import date_fmt


app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', tags=['MAIN'])
async def main():
    return [{"ping": "pong"}, {"ping": "pong"}, {"ping": "pong"}, {"ping": "pong"}]


@app.post('/services/calculator', tags=['calculator'])
async def calculator(calc_json: dict) -> dict:
    """Returns solved equation."""

    operator = calc_json['operation']
    value_1 = int(calc_json['a'])
    value_2 = int(calc_json['b'])

    result = calcFunc(value_1=value_1, value_2=value_2, operator=operator)

    return {"result": result}


@app.post('/services/date-fmt', tags=['date-fmt'])
async def dateCalculator(date_json: dict) -> dict:
    """Adds time delta to provided date."""

    current_date = parser.parse(date_json['date'])
    delta = int(date_json['days'])

    string = date_fmt(date=current_date, days=delta)

    return {"date": string}
