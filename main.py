from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI(title="Calculator API")

@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
def home():
    return """
    <html>
        <head><title>Calculator</title></head>
        <body>
            <h1>Calculator Interface</h1>
            <form action="/add" method="get">
                <input type="number" name="num1" placeholder="First number" required>
                <input type="number" name="num2" placeholder="Second number" required>
                <button type="submit">Add</button>
            </form><br>

            <form action="/subtract" method="get">
                <input type="number" name="num1" placeholder="First number" required>
                <input type="number" name="num2" placeholder="Second number" required>
                <button type="submit">Subtract</button>
            </form><br>

            <form action="/multiply" method="get">
                <input type="number" name="num1" placeholder="First number" required>
                <input type="number" name="num2" placeholder="Second number" required>
                <button type="submit">Multiply</button>
            </form><br>

            <form action="/divide" method="get">
                <input type="number" step="any" name="num1" placeholder="First number" required>
                <input type="number" step="any" name="num2" placeholder="Second number" required>
                <button type="submit">Divide</button>
            </form><br>
            
            <form action="/power" method="get">
                <input type="number" step="any" name="base" placeholder="Base" required>
                <input type="number" step="any" name="exponent" placeholder="Exponent" required>
                <button type="submit">Power</button>
            </form><br>

            <form action="/sqrt" method="get">
                <input type="number" step="any" name="number" placeholder="Number" required>
                <button type="submit">Square Root</button>
            </form><br>

            <form action="/sum" method="get">
                <input type="text" name="numbers" placeholder="Comma-separated numbers (e.g. 1,2,3)" required>
                <button type="submit">Sum</button>
            </form><br>

            <form action="/average" method="get">
                <input type="text" name="numbers" placeholder="Comma-separated numbers (e.g. 4,5,6)" required>
                <button type="submit">Average</button>
            </form><br>
        </body>
    </html>
    """

@app.get("/add", response_class=HTMLResponse, tags=["Addition"])
def add(num1: float, num2: float):
    result = num1 + num2
    return f"<h1>Addition Result: {result}</h1>"

@app.get("/subtract", response_class=HTMLResponse, tags=["Subtraction"])
def subtract(num1: float, num2: float):
    result = num1 - num2
    return f"<h1>Subtraction Result: {result}</h1>"

@app.get("/multiply", response_class=HTMLResponse, tags=["Multiplication"])
async def multiply(num1: float, num2: float):
    result = num1 * num2
    return f"<h1>Multiplication Result: {result}</h1>"

@app.get("/divide", response_class=HTMLResponse, tags=["Division"])
async def divide(num1: float = Query(...), num2: float = Query(...)):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    result = num1 / num2
    return f"<h1>Division Result: {result}</h1>"

@app.get("/power/{base}/{exponent}", response_class=HTMLResponse, tags=["Power"])
async def power(base: float, exponent: float):
    result = base ** exponent
    return f"<h1>Power Result: {result}</h1>"

@app.get("/sqrt/{number}", response_class=HTMLResponse, tags=["Square Root"])
async def sqrt(number: float):
    if number < 0:
        raise HTTPException(status_code=400, detail="Negative numbers not allowed for square root")
    result = number ** 0.5
    return f"<h1>Square Root Result: {result}</h1>"

@app.get("/sum", response_class=HTMLResponse, tags=["Summation"])
async def sum_numbers(numbers: str = Query(...)):
    number_list = [float(x.strip()) for x in numbers.split(',')]
    result = sum(number_list)
    return f"<h1>Summation Result: {result}</h1>"

@app.get("/average", response_class=HTMLResponse, tags=["Average"])
async def average(numbers: str = Query(...)):
    number_list = [float(x.strip()) for x in numbers.split(',')]
    result = sum(number_list) / len(number_list)
    return f"<h1>Average Result: {result}</h1>"

