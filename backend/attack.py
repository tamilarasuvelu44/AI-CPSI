from flask import Blueprint, request, jsonify
from backend.attack_ai import simulate_attack

attack_bp = Blueprint("attack", __name__)

@attack_bp.route("/api/start_attack", methods=["POST"])
def start_attack():
    data = request.get_json(force=True)
    attack = data.get("attack", "Unknown")
    device = data.get("device", "Unknown")
    result = simulate_attack(attack, device)
    return jsonify(result)
