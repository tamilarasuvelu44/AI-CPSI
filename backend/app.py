import os
import sys
from flask import Flask, send_from_directory

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.config import Config
from backend.database import db
from backend.attack import attack_bp
from backend.auth import auth_bp
from backend.api import api_bp
from backend.seed import seed_data
import backend.models


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(attack_bp)

    @app.route("/", defaults={"path": "index.html"})
    @app.route("/<path:path>")
    def serve_frontend(path):
        if path == "attack":
            path = "attack.html"
        return send_from_directory(FRONTEND_DIR, path)

    return app

app = create_app()

if __name__ == "__main__":
    os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True)
