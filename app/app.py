from flask import Flask, request, jsonify
from utils import add

app = Flask(__name__)

@app.route("/")
def health_check():
    return "App is running!"

# /add?a=2&b=3
@app.route("/add")
def add_operation():
    a = request.args.get("a")
    b = request.args.get("b")

    if a is None or b is None:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        result = add(int(a), int(b))
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)