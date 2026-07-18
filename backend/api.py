from flask import Blueprint, jsonify
from backend.models import Device, Sensor, Vulnerability, Report
from backend.database import db

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/dashboard_metrics", methods=["GET"])
def dashboard_metrics():
    try:
        devices = Device.query.count()
        sensors = Sensor.query.count()
        vulnerabilities = Vulnerability.query.count()
        reports = Report.query.count()
    except Exception:
        # DB not available or incompatible SQLAlchemy — return safe defaults
        devices = 0
        sensors = 0
        vulnerabilities = 0
        reports = 0

    return jsonify({
        "connected_devices": devices,
        "active_sensors": sensors,
        "vulnerabilities": vulnerabilities,
        "reports": reports,
        "threats_detected": 12,
        "critical_alerts": 3,
        "system_health": 98
    })

@api_bp.route("/api/threats", methods=["GET"])
def threats():
    return jsonify({
        "threats": [
            {"device": "Temperature Sensor", "level": "High", "probability": "92%", "recommendation": "Update firmware and isolate the device."},
            {"device": "PLC Controller", "level": "Medium", "probability": "74%", "recommendation": "Review firewall rules and confirm access control."}
        ]
    })

@api_bp.route("/api/digital_twin", methods=["GET"])
def digital_twin():
    try:
        devices = Device.query.limit(5).all()
        twin_devices = []
        for device in devices:
            twin_devices.append({
                "name": device.device_name,
                "type": device.device_type,
                "ip": device.ip_address,
                "status": device.status,
                "location": device.location
            })

        sensors = Sensor.query.limit(10).all()
        twin_sensors = []
        for sensor in sensors:
            twin_sensors.append({
                "name": sensor.sensor_name,
                "type": sensor.sensor_type,
                "value": sensor.sensor_value,
                "unit": sensor.unit,
                "device": sensor.device.device_name if sensor.device else "Unknown"
            })
    except Exception:
        twin_devices = [
            {"name": "PLC Controller", "type": "PLC", "ip": "192.168.1.10", "status": "Online", "location": "Factory Floor"}
        ]
        twin_sensors = [
            {"name": "Temperature Sensor", "type": "Temperature", "value": 72.4, "unit": "°C", "device": "PLC Controller"}
        ]

    return jsonify({"devices": twin_devices, "sensors": twin_sensors})

@api_bp.route("/api/reports", methods=["GET"])
def reports():
    report_list = [
        {"name": "Weekly Security Summary", "generated_on": "2026-07-01", "status": "Completed"},
        {"name": "Network Audit", "generated_on": "2026-06-28", "status": "Review"}
    ]
    try:
        db_reports = Report.query.limit(5).all()
        for report in db_reports:
            report_list.append({"name": report.report_name, "generated_on": report.generated_on.strftime("%Y-%m-%d"), "status": "Saved"})
    except Exception:
        # fall back to static list
        pass

    return jsonify({"reports": report_list})

@api_bp.route("/api/settings", methods=["GET"])
def settings():
    return jsonify({
        "account_email": "tamil@example.com",
        "notifications": True,
        "auto_updates": True,
        "data_retention_days": 90
    })
