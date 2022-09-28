from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/health", methods=['GET'])
def health_check():
    result = {
        'health':'All good!'
    }
    return jsonify(result)

@app.route("/add", methods=['GET', 'POST'])
def add():
    n1 = request.args.get('n1', default=1.0, type=float)
    n2 = request.args.get('n2', default=1.0, type=float)
    result = {
        'sum' : float(n1+n2)
    } 
    return jsonify(result)

@app.route("/subtract", methods=['GET', 'POST'])
def subtract():
    n1 = request.args.get('n1', default=1.0, type=float)
    n2 = request.args.get('n2', default=1.0, type=float)
    if n1 < n2:
        n1, n2 = n2, n1
    result = {
        'diff' : float(n1-n2)
    } 
    return jsonify(result)

@app.route("/multiply", methods=['GET', 'POST'])
def multiply():
    n1 = request.args.get('n1', default=1.0, type=float)
    n2 = request.args.get('n2', default=1.0, type=float)
    result = {
        'product' : float(n1*n2)
    } 
    return jsonify(result)

@app.route("/divide", methods=['GET', 'POST'])
def divide():
    n1 = request.args.get('n1', default=1.0, type=float)
    n2 = request.args.get('n2', default=1.0, type=float)
    result = {
        'quotient' : float(n1//n2)
    } 
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

# Sample cURL request : curl -X GET "http://192.168.39.156:80/add?n1=4.25&n2=7.65"