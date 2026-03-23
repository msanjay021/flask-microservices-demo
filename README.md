# Flask Microservices Example

## Purpose
Built as part of backend learning and microservices practice.

This project demonstrates a simple microservices architecture using Flask.

## Services

### 1. Greeting Service (Port 5001)
- Endpoint: `/hello`
- Method: GET

### 2. Math Service (Port 5002)
- Endpoint: `/sum`
- Method: POST

## How to Run

### Install dependencies
pip install flask requests

### Run services

Terminal 1:
cd greeting_service
python app.py

Terminal 2:
cd math_service
python app.py

## Example Requests

GET:
http://127.0.0.1:5001/hello?name=Sanjay

POST:
curl -X POST http://127.0.0.1:5002/sum \
-H "Content-Type: application/json" \
-d '{"a": 10, "b": 20}'
