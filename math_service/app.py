from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    if a is None or b is None:
        return jsonify({"error": "Missing values"}), 400

    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(port=5002, debug=True)