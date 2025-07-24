from flask import Flask, jsonify
import random

app = Flask(__name__)
@app.route("/metrics")
def metrics():
    return f"# HELP my_app_random Random number\n# TYPE my_app_random gauge\nmy_app_random {random.random()}"
@app.route("/")
def home():
    return "Hello from monitored microservice!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)