from flask import Flask
## from .routes import calculator_routes_bp


app = Flask(__name__)

from .routes import *
app.register_blueprint(calculator_routes_bp)