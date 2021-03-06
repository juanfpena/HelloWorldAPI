from flask import Flask, request, render_template, jsonify
from dateutil import parser
from functionalities.calculator import calculator_func
from functionalities.datefmt import dateCalculator_func
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services/calculator', methods=['POST', 'GET'])
def calculator() -> dict:
    """Returns solved equation."""

    data = request.get_json()

    operator = data['operation']
    value_1 = data['a']
    value_2 = data['b']

    result = calculator_func(num_a=value_1, num_b=value_2, operator=operator)

    return jsonify({"result": result})


@app.route('/services/date-fmt', methods=['POST', 'GET'])
def dateCalculator() -> dict:
    """Adds time delta to provided date."""

    data = request.get_json()
    current_date = parser.isoparse(data['date'])
    delta = int(data['days'])

    string = dateCalculator_func(current_date=current_date, days=delta)

    return jsonify({"date": string})


if __name__ == '__main__':
    app.run(debug=True)
