async function login() {
    let user = document.getElementById("username").value.trim();
    let pass = document.getElementById("password").value.trim();

    if (!user || !pass) {
        alert("Please enter username and password.");
        return;
    }

    try {
        let response = await fetch("/api/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username: user, password: pass})
        });
        let data = await response.json();

        if (response.ok && data.success) {
            window.location = "dashboard.html";
        } else {
            alert(data.message || "Invalid login");
        }
    } catch (error) {
        alert("Unable to connect to the server. Please try again later.");
        console.error(error);
    }
}

async function simulateAttack() {
    let attack = "Phishing";
    let device = "PLC Controller";

    try {
        let response = await fetch("/api/start_attack", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({attack: attack, device: device})
        });

        if (!response.ok) {
            throw new Error("Attack API request failed.");
        }

        let data = await response.json();
        document.getElementById("result").innerHTML = `
            <h3>Simulation Result</h3>
            <p><strong>Attack:</strong> ${data.attack}</p>
            <p><strong>Target:</strong> ${data.device}</p>
            <p><strong>Status:</strong> ${data.status}</p>
            <p><strong>Risk Score:</strong> ${data.risk_score}</p>
            <p><strong>Recommendations:</strong></p>
            <ul>${data.recommendation.map(item => `<li>${item}</li>`).join("")}</ul>
        `;
    } catch (error) {
        console.error(error);
        document.getElementById("result").innerHTML = "<p style='color:red;'>Unable to run simulation.</p>";
    }
}

async function loadDashboardMetrics() {
    try {
        let response = await fetch("/api/dashboard_metrics");
        if (!response.ok) {
            throw new Error("Failed to load dashboard metrics.");
        }
        let data = await response.json();
        document.getElementById("connectedDevices").textContent = data.connected_devices;
        document.getElementById("threatsDetected").textContent = data.threats_detected;
        document.getElementById("criticalAlerts").textContent = data.critical_alerts;
        document.getElementById("systemHealth").textContent = data.system_health + "%";
    } catch (error) {
        console.error(error);
    }
}

window.addEventListener("DOMContentLoaded", () => {
    const path = window.location.pathname.split('/').pop();
    if (path === "dashboard.html") {
        loadDashboardMetrics();
    } else if (path === "threat_detection.html") {
        loadThreats();
    } else if (path === "DigitalTwin.html") {
        loadDigitalTwin();
    } else if (path === "Reports.html") {
        loadReports();
    } else if (path === "Settings.html") {
        loadSettings();
    }
});

async function loadThreats() {
    try {
        let res = await fetch('/api/threats');
        if (!res.ok) throw new Error('Failed to load threats');
        let data = await res.json();
        const list = document.getElementById('threatList');
        list.innerHTML = '';
        data.threats.forEach(t => {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${t.device}</strong> - ${t.level} - ${t.probability}<br><em>${t.recommendation}</em>`;
            list.appendChild(li);
        });
    } catch (e) { console.error(e); }
}

async function loadDigitalTwin() {
    try {
        let res = await fetch('/api/digital_twin');
        if (!res.ok) throw new Error('Failed to load digital twin');
        let data = await res.json();
        const devList = document.getElementById('twinDevices');
        const senList = document.getElementById('twinSensors');
        if (devList) {
            devList.innerHTML = '';
            data.devices.forEach(d => devList.insertAdjacentHTML('beforeend', `<li>${d.name} (${d.type}) — ${d.status} — ${d.location}</li>`));
        }
        if (senList) {
            senList.innerHTML = '';
            data.sensors.forEach(s => senList.insertAdjacentHTML('beforeend', `<li>${s.name} (${s.type}) — ${s.value}${s.unit} — device: ${s.device}</li>`));
        }
    } catch (e) { console.error(e); }
}

async function loadReports() {
    try {
        let res = await fetch('/api/reports');
        if (!res.ok) throw new Error('Failed to load reports');
        let data = await res.json();
        const list = document.getElementById('reportList');
        if (!list) return;
        list.innerHTML = '';
        data.reports.forEach(r => list.insertAdjacentHTML('beforeend', `<li>${r.name} — ${r.generated_on} — ${r.status}</li>`));
    } catch (e) { console.error(e); }
}

async function loadSettings() {
    try {
        let res = await fetch('/api/settings');
        if (!res.ok) throw new Error('Failed to load settings');
        let data = await res.json();
        const list = document.getElementById('settingsList');
        if (!list) return;
        list.innerHTML = '';
        list.insertAdjacentHTML('beforeend', `<li>Account: ${data.account_email}</li>`);
        list.insertAdjacentHTML('beforeend', `<li>Notifications: ${data.notifications}</li>`);
        list.insertAdjacentHTML('beforeend', `<li>Auto updates: ${data.auto_updates}</li>`);
        list.insertAdjacentHTML('beforeend', `<li>Data retention (days): ${data.data_retention_days}</li>`);
    } catch (e) { console.error(e); }
}
