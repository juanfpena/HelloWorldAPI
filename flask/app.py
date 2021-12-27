from flask import Flask, request
from dateutil import parser
import datetime

app = Flask(__name__)


@app.route('/services/calculator', methods=['PUT', 'GET'])
def calculator() -> dict:
    """Returns solved equation."""

    operator = request.args.get('operation')
    value_1 = int(request.args.get('a'))
    value_2 = int(request.args.get('b'))

    if operator == 'sum':
        result = value_1 + value_2

    elif operator == 'sub':
        result = value_1 - value_2

    elif operator == 'mul':
        result = value_1 * value_2

    elif operator == 'div':
        result = value_1 / value_2

    return {"result": result}


@app.route('/services/date-fmt', methods=['PUT', 'GET'])
def dateCalculator() -> dict:
    """Adds time delta to provided date."""

    current_date = parser.isoparse(request.args.get('date'))
    delta = int(request.args.get('days'))

    end_date = current_date + datetime.timedelta(days=delta)

    string = str(end_date.isoformat())

    return {"date": string}


if __name__ == '__main__':
    app.run(debug=True)
