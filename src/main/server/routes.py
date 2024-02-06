from flask import request, jsonify
from src.controllers.calculator_1_controller import Calculator1Controller
from .server import app
from src.main.adapter.request_adapter import request_adapter


@app.route("/", methods=["POST"])
def calculator_function():
    calculator_1 = Calculator1Controller()

    http_request = request_adapter(request)
    response = calculator_1.execute(http_request)

    return jsonify(response.body), response.status_code