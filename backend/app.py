import os
import sys
from flask import Flask, send_from_directory
from config import Config
from database import db

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

sys.path.insert(0, FRONTEND_DIR)

from attack import attack_bp
import models

app = Flask(__name__, static_folder=None)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def serve_frontend(path):
    if path == "attack":
        path = "attack.html"
    return send_from_directory(FRONTEND_DIR, path)

if __name__ == "__main__":
    app.run(debug=True)