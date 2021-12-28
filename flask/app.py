from flask import Flask, json, request, render_template, jsonify
from dateutil import parser
import datetime
from functionalities.calculator import calculator_func
from functionalities.datefmt import dateCalculator_func

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services/calculator', methods=['POST', 'GET'])
def calculator() -> dict:
    """Returns solved equation."""

    data = request.get_json()

    if request.method == 'GET':
        return render_template('calculator.html')

    if request.method == 'POST':

        operator = data['operation']
        value_1 = data['a']
        value_2 = data['b']

        result = calculator_func(
            num_a=value_1, num_b=value_2, operator=operator)

        return jsonify({"result": result})


@app.route('/services/date-fmt', methods=['POST', 'GET'])
def dateCalculator() -> dict:
    """Adds time delta to provided date."""

    data = request.get_json()

    if request.method == 'GET':
        pass

    if request.method == 'POST':

        current_date = parser.isoparse(data['date'])
        delta = int(data['days'])

        string = dateCalculator_func(current_date=current_date, days=delta)

        return jsonify({"date": string})


if __name__ == '__main__':
    app.run(debug=True)
