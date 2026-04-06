"""
Matrix-Based Force Distribution in a Multi-Link Suspension System
Flask Backend
"""

from flask import Flask
from flask_cors import CORS
from routes.simulate import simulate_bp
from routes.history import history_bp
from routes.pdf import pdf_bp
from routes.chat import chat_bp
from routes.auth import auth_bp
from db import init_db

app = Flask(__name__)
CORS(app)

init_db()

app.register_blueprint(simulate_bp, url_prefix="/api")
app.register_blueprint(history_bp, url_prefix="/api")
app.register_blueprint(pdf_bp, url_prefix="/api")
app.register_blueprint(chat_bp, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
