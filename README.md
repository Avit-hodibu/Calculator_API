# FastAPI Calculator API

A simple web-based calculator built using FastAPI. It supports basic operations like add, subtract, multiply, divide, power, square root, summation, and average.

## Features

- Web frontend using HTML forms
- REST API endpoints
- Pytest for testing
- Docker and Docker Compose support

## Project Structure

calculator\
├── main.py
├── main_tests/
  


## Run Locally

### Github
```git clone https://github.com/Avit-hodibu/Calculator_API```


### Using Python
In terminal:

```pip install -r requirements.txt
uvicorn app.main:app --reload ```

Access the calculator at: [http://localhost:8000](http://localhost:8000)

### Using Docker
In Termainal:
```docker-compose up --build```

## Run Tests

```
pytest tests/
```