import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')

    # Call math service
    response = requests.post(
        "http://127.0.0.1:5002/sum",
        json={"a": 5, "b": 3}
    )

    sum_result = response.json().get("result")

    return jsonify({
        "message": f"Hello, {name}!",
        "sum_from_math_service": sum_result
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)