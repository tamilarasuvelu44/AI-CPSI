import random

def simulate_attack(attack, device):
    risk = random.randint(50, 100)
    if risk > 80:
        status = "Critical"
    elif risk > 60:
        status = "Warning"
    else:
        status = "Safe"

    recommendations = [
        "Update firmware",
        "Enable Firewall",
        "Close unused ports",
        "Change default passwords",
        "Monitor network traffic"
    ]

    return {
        "attack": attack,
        "device": device,
        "status": status,
        "risk_score": risk,
        "recommendation": recommendations[:3]
    }
