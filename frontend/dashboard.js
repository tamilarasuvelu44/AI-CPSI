async function loadDashboardMetrics() {
    try {
        let response = await fetch('/api/dashboard_metrics');
        if (!response.ok) throw new Error('Failed to load dashboard metrics');
        let data = await response.json();
        document.getElementById('connectedDevices').textContent = data.connected_devices;
        document.getElementById('threatsDetected').textContent = data.threats_detected;
        document.getElementById('criticalAlerts').textContent = data.critical_alerts;
        document.getElementById('systemHealth').textContent = data.system_health + '%';
    } catch (error) {
        console.error(error);
    }
}

async function simulateAttack() {
    let attack = document.getElementById('attackType') ? document.getElementById('attackType').value : 'Phishing';
    let device = document.getElementById('targetDevice') ? document.getElementById('targetDevice').value : 'PLC Controller';

    try {
        let response = await fetch('/api/start_attack', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({attack: attack, device: device})
        });
        let data = await response.json();
        let resultBox = document.getElementById('result');
        if (!response.ok) {
            throw new Error(data.message || 'Attack request failed');
        }
        resultBox.innerHTML = `
            <h3>Simulation Result</h3>
            <p><strong>Attack:</strong> ${data.attack}</p>
            <p><strong>Target:</strong> ${data.device}</p>
            <p><strong>Status:</strong> ${data.status}</p>
            <p><strong>Risk Score:</strong> ${data.risk_score}</p>
            <p><strong>Recommendations:</strong></p>
            <ul>${data.recommendation.map(item => `<li>${item}</li>`).join('')}</ul>
        `;
    } catch (error) {
        document.getElementById('result').innerHTML = `<p style='color:red;'>${error.message}</p>`;
        console.error(error);
    }
}

async function loadThreats() {
    try {
        let response = await fetch('/api/threats');
        let data = await response.json();
        let list = document.createElement('ul');
        list.className = 'report-list';
        data.threats.forEach(item => {
            let li = document.createElement('li');
            li.innerHTML = `<strong>${item.device}</strong><span class='metric'>Level: ${item.level}</span><span class='metric'>Probability: ${item.probability}</span><span class='metric'>Recommendation: ${item.recommendation}</span>`;
            list.appendChild(li);
        });
        document.getElementById('threatList').appendChild(list);
    } catch (error) {
        console.error(error);
    }
}

async function loadDigitalTwin() {
    try {
        let response = await fetch('/api/digital_twin');
        let data = await response.json();
        let deviceContainer = document.getElementById('twinDevices');
        let sensorContainer = document.getElementById('twinSensors');

        data.devices.forEach(item => {
            let li = document.createElement('li');
            li.innerHTML = `<strong>${item.name}</strong><span class='metric'>${item.type} • ${item.ip}</span><span class='metric'>Status: ${item.status}</span><span class='metric'>Location: ${item.location}</span>`;
            deviceContainer.appendChild(li);
        });

        data.sensors.forEach(item => {
            let li = document.createElement('li');
            li.innerHTML = `<strong>${item.name}</strong><span class='metric'>${item.type} • ${item.value}${item.unit}</span><span class='metric'>Device: ${item.device}</span>`;
            sensorContainer.appendChild(li);
        });
    } catch (error) {
        console.error(error);
    }
}

async function loadReports() {
    try {
        let response = await fetch('/api/reports');
        let data = await response.json();
        let list = document.getElementById('reportList');
        data.reports.forEach(item => {
            let li = document.createElement('li');
            li.innerHTML = `<strong>${item.name}</strong><span class='metric'>Date: ${item.generated_on}</span><span class='metric'>Status: ${item.status}</span>`;
            list.appendChild(li);
        });
    } catch (error) {
        console.error(error);
    }
}

async function loadSettings() {
    try {
        let response = await fetch('/api/settings');
        let data = await response.json();
        let list = document.getElementById('settingsList');
        Object.entries(data).forEach(([key, value]) => {
            let li = document.createElement('li');
            li.innerHTML = `<strong>${key.replace(/_/g, ' ')}</strong><span class='metric'>${value}</span>`;
            list.appendChild(li);
        });
    } catch (error) {
        console.error(error);
    }
}

window.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.endsWith('dashboard.html')) {
        loadDashboardMetrics();
    }
    if (window.location.pathname.endsWith('attack.html')) {
        document.getElementById('startBtn').onclick = simulateAttack;
    }
    if (window.location.pathname.endsWith('threat_detection.html')) {
        loadThreats();
    }
    if (window.location.pathname.endsWith('DigitalTwin.html')) {
        loadDigitalTwin();
    }
    if (window.location.pathname.endsWith('Reports.html')) {
        loadReports();
    }
    if (window.location.pathname.endsWith('Settings.html')) {
        loadSettings();
    }
});
