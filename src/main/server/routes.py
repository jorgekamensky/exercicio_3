from flask import request, jsonify, Blueprint
from src.controllers.calculator_1_controller import Calculator1Controller
from src.controllers.calculator_2_controller import Calculator2Controller
from src.controllers.calculator_3_controller import Calculator3Controller
##from .server import app
from src.main.adapter.request_adapter import request_adapter

calculator_routes_bp = Blueprint("api_routes", __name__)

@calculator_routes_bp.route("/calculator_1", methods=["POST"])
def calculator_1_function():
    calculator_1 = Calculator1Controller()

    http_request = request_adapter(request)
    response = calculator_1.execute(http_request)

    return jsonify(response.body), response.status_code

@calculator_routes_bp.route("/calculator_2", methods=["POST"])
def calculator_2_function():
    calculator_2 = Calculator2Controller()

    http_request = request_adapter(request)
    response = calculator_2.execute(http_request)

    return jsonify(response.body), response.status_code

@calculator_routes_bp.route("/calculator_3", methods=["POST"])
def calculator_3_function():
    calculator_3 = Calculator3Controller()

    http_request = request_adapter(request)
    response = calculator_3.execute(http_request)

    return jsonify(response.body), response.status_code