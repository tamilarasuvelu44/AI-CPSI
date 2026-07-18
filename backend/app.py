from flask import Flask
from config import Config
from database import db
import models

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "AI-CPSI Running"

if __name__ == "__main__":
    app.run(debug=True)