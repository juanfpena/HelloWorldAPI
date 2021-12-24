from fastapi import FastAPI
from dateutil import parser
import datetime

app = FastAPI()


@app.put('/services/calculator', tags=['calculator'])
def calculator(calc_json: dict) -> dict:
    """Returns solved equation."""

    operator = calc_json['operation']
    value_1 = int(calc_json['a'])
    value_2 = int(calc_json['b'])

    if operator == 'sum':
        result = value_1 + value_2

    elif operator == 'sub':
        result = value_1 - value_2

    elif operator == 'mul':
        result = value_1 * value_2

    elif operator == 'div':
        result = value_1 / value_2

    return {"result": result}


@app.put('/services/date-fmt', tags=['date-fmt'])
def dateCalculator(date_json: dict) -> dict:
    """Adds time delta to provided date."""

    current_date = parser.parse(date_json['date'])
    delta = date_json['days']

    end_date = current_date + datetime.timedelta(days=delta)

    string = str(end_date)

    return {"date": string}
