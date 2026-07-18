function login(){

let user=document.getElementById("username").value;

let pass=document.getElementById("password").value;

if(user=="tamil" && pass=="velu"){

window.location="dashboard.html";

}

else{

alert("Invalid Login");

}

}

function simulateAttack(){

document.getElementById("result").innerHTML=`
<h3>Simulation Running...</h3>

<p>✔ Reconnaissance Completed</p>

<p>✔ Vulnerability Scan Completed</p>

<p>✔ AI Generated Attack Path</p>

<p>✔ Intrusion Detected</p>

<p style="color:red;">Response Activated</p>
`;

}