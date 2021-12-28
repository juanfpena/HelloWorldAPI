
from app import app
import unittest
from flask import jsonify
import ast


class TestSuite(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    calculator_data = {
        "a": 1,
        "b": 2,
        "operation": "mul"
    }

    calculator_response = {
        "result": 2
    }

    def test_calculator(self):
        tester = app.test_client(self)
        response = tester.post("/services/calculator",
                               json=self.calculator_data)
        response_data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(ast.literal_eval(
            response_data.decode('UTF-8')), self.calculator_response)

    date_data = {
        "date": "2020-01-01T00:00:00",
        "days": 2
    }
    date_response = {
        "date": "2020-01-03T00:00:00"
    }

    def test_date(self):
        tester = app.test_client(self)
        response = tester.post("/services/date-fmt", json=self.date_data)
        response_data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(ast.literal_eval(
            response_data.decode('UTF-8')), self.date_response)


if __name__ == "__main__":
    unittest.main()
