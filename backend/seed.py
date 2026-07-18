from backend.database import db
from backend.models import User, Device, Sensor, Vulnerability


def seed_data():
    if User.query.first() is not None:
        return

    default_user = User(
        username="tamil",
        email="tamil@example.com",
        password="velu"
    )

    device1 = Device(
        device_name="PLC Controller",
        device_type="PLC",
        ip_address="192.168.1.10",
        mac_address="00:1A:C2:7B:00:47",
        status="Online",
        location="Factory Floor",
    )

    sensor1 = Sensor(
        sensor_name="Temperature Sensor",
        sensor_type="Temperature",
        sensor_value=72.4,
        unit="°C",
        device=device1,
    )

    vulnerability1 = Vulnerability(
        vulnerability_name="Open Port 8080",
        severity="Medium",
        description="Publicly accessible service with weak authentication.",
        recommendation="Restrict access and enable strong authentication."
    )

    db.session.add(default_user)
    db.session.add(device1)
    db.session.add(sensor1)
    db.session.add(vulnerability1)
    db.session.commit()
