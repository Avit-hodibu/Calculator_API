from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>Calculator Interface</h1>" in response.text

def test_add():
    response = client.get("/add", params={"num1": 5, "num2": 3})
    assert response.status_code == 200
    assert "Addition Result: 8.0" in response.text

def test_subtract():
    response = client.get("/subtract", params={"num1": 10, "num2": 4})
    assert response.status_code == 200
    assert "Subtraction Result: 6.0" in response.text

def test_multiply():
    response = client.get("/multiply", params={"num1": 7, "num2": 6})
    assert response.status_code == 200
    assert "Multiplication Result: 42.0" in response.text

def test_divide():
    response = client.get("/divide", params={"num1": 8, "num2": 2})
    assert response.status_code == 200
    assert "Division Result: 4.0" in response.text

def test_divide_by_zero():
    response = client.get("/divide", params={"num1": 8, "num2": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Division by zero is not allowed"

def test_power():
    response = client.get("/power/2/3")
    assert response.status_code == 200
    assert "Power Result: 8.0" in response.text

def test_sqrt():
    response = client.get("/sqrt/16")
    assert response.status_code == 200
    assert "Square Root Result: 4.0" in response.text

def test_sqrt_negative():
    response = client.get("/sqrt/-4")
    assert response.status_code == 400
    assert response.json()["detail"] == "Negative numbers not allowed for square root"

def test_sum_numbers():
    response = client.get("/sum", params={"numbers": "1,2,3,4"})
    assert response.status_code == 200
    assert "Summation Result: 10.0" in response.text

def test_average():
    response = client.get("/average", params={"numbers": "2,4,6,8"})
    assert response.status_code == 200
    assert "Average Result: 5.0" in response.text