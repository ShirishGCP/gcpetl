from flask import Flask
app = Flask(__name__)
from src.app.routes import register_routes
register_routes(app)
