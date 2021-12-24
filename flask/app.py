from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/services/calculator', methods=['PUT'])
def calculator(arguments: dict) -> dict:
    """Returns solved equation."""

    operator = arguments['operation']
    value_1 = arguments['a']
    value_2 = arguments['b']

    if operator == 'sum':
        result = value_1 + value_2

    elif operator == 'sub':
        result = value_1 - value_2

    elif operator == 'mul':
        result = value_1 * value_2

    elif operator == 'div':
        result = value_1 / value_2

    return {"result": result}


if __name__ == '__main__':
    app.run(debug=True)
