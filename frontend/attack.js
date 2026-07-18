document.getElementById("startBtn").onclick = async function () {
    let attack = document.getElementById("attackType").value;
    let device = document.getElementById("targetDevice").value;

    try {
        let response = await fetch("/api/start_attack", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                attack: attack,
                device: device
            })
        });

        if (!response.ok) {
            throw new Error("Attack API request failed");
        }

        let data = await response.json();

        document.getElementById("status").innerHTML = data.status;
        document.getElementById("risk").innerHTML = data.risk_score;

        let list = document.getElementById("recommendation");
        list.innerHTML = "";

        data.recommendation.forEach(function (item) {
            let li = document.createElement("li");
            li.innerHTML = item;
            list.appendChild(li);
        });
    } catch (error) {
        console.error(error);
        alert("Unable to launch simulation. Please try again later.");
    }
};
