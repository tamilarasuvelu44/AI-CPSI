from flask import Blueprint, request, jsonify
from backend.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"success": False, "message": "Username and password are required."}), 400

    try:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return jsonify({"success": True, "message": "Login successful"})
    except Exception:
        # DB not available — fallback to a seeded test user
        if username == "tamil" and password == "velu":
            return jsonify({"success": True, "message": "Login successful (fallback)"})

    return jsonify({"success": False, "message": "Invalid username or password"}), 401
