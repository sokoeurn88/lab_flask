from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
#    return "Hello World"
#    return {"message":"Hello World Sokoeurn"}
    return jsonify(message="Hello World Sokoeurn Chhay")