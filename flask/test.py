
from app import app
import unittest


class TestSuite(unittest.TestCase):

    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 404)

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
        response = tester.put("/services/calculator",
                              json=self.calculator_data)
        self.assertEqual(response.status_code, 500)
        self.assertDictEqual(response.json(), self.calculator_response)

    date_data = {
        "date": "2020-01-01T00:00:00",
        "days": 2
    }
    date_response = {
        "date": "2020-01-03"
    }

    def test_date(self):
        tester = app.test_client(self)
        response = tester.put("/services/date-fmt", json=self.date_data)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), self.date_response)


if __name__ == "__main__":
    unittest.main()
