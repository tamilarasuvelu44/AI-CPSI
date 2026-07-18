from database import db
from datetime import datetime

# ----------------------------
# Users
# ----------------------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="User")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------
# Projects
# ----------------------------
class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    owner = db.relationship("User", backref="projects")


# ----------------------------
# Devices
# ----------------------------
class Device(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(100))
    device_type = db.Column(db.String(50))
    ip_address = db.Column(db.String(50))
    mac_address = db.Column(db.String(50))
    status = db.Column(db.String(20))
    location = db.Column(db.String(100))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    project = db.relationship("Project", backref="devices")


# ----------------------------
# Sensors
# ----------------------------
class Sensor(db.Model):
    __tablename__ = "sensors"

    id = db.Column(db.Integer, primary_key=True)
    sensor_name = db.Column(db.String(100))
    sensor_type = db.Column(db.String(50))
    sensor_value = db.Column(db.Float)
    unit = db.Column(db.String(20))
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))

    device = db.relationship("Device", backref="sensors")


# ----------------------------
# Attack Logs
# ----------------------------
class AttackLog(db.Model):
    __tablename__ = "attack_logs"

    id = db.Column(db.Integer, primary_key=True)
    attack_type = db.Column(db.String(100))
    target = db.Column(db.String(100))
    success = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------
# Risk Scores
# ----------------------------
class RiskScore(db.Model):
    __tablename__ = "risk_scores"

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float)
    level = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------
# Network Logs
# ----------------------------
class NetworkLog(db.Model):
    __tablename__ = "network_logs"

    id = db.Column(db.Integer, primary_key=True)
    source_ip = db.Column(db.String(50))
    destination_ip = db.Column(db.String(50))
    protocol = db.Column(db.String(20))
    port = db.Column(db.Integer)
    packet_size = db.Column(db.Integer)
    log_time = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------
# Vulnerabilities
# ----------------------------
class Vulnerability(db.Model):
    __tablename__ = "vulnerabilities"

    id = db.Column(db.Integer, primary_key=True)
    vulnerability_name = db.Column(db.String(150))
    severity = db.Column(db.String(50))
    description = db.Column(db.Text)
    recommendation = db.Column(db.Text)


# ----------------------------
# Reports
# ----------------------------
class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(150))
    report_path = db.Column(db.String(255))
    generated_on = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------
# Alerts
# ----------------------------
class Alert(db.Model):
    __tablename__ = "alerts"

    id = db.Column(db.Integer, primary_key=True)
    alert_type = db.Column(db.String(100))
    severity = db.Column(db.String(50))
    message = db.Column(db.Text)
    alert_time = db.Column(db.DateTime, default=datetime.utcnow)