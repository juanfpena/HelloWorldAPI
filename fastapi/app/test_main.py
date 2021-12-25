from app import app
from fastapi.testclient import TestClient

client = TestClient(app=app)


def test_put_calculator():
    response = client.put(
        '/services/calculator', json={"a": 1, "b": 2, "operation": "mul"}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 2}


def test_put_dateCalculator():
    response = client.put(
        '/services/date-fmt', json={"date": "2020-01-01T00:00:00", "days": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"date": "2020-01-03T00:00:00"}
