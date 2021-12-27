import json
from app import app
import unittest


class TestSuite(unittest.TestCase):

    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 404)


if __name__ == "__main__":
    unittest.main()
