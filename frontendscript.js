let roomId = "";
let playerId = "";

const API = "http://localhost:8000";

async function createRoom() {
  const name = document.getElementById("name").value;
  const res = await fetch(`${API}/room/create?name=${name}`, { method: "POST" });
  const data = await res.json();
  roomId = data.roomId;
  playerId = data.playerId;
  output(data);
}

async function joinRoom() {
  const name = document.getElementById("name").value;
  roomId = document.getElementById("roomId").value;
  const res = await fetch(`${API}/room/join?roomId=${roomId}&name=${name}`, { method: "POST" });
  const data = await res.json();
  playerId = data.playerId;
  output(data);
}

async function viewRole() {
  const res = await fetch(`${API}/role/me/${roomId}/${playerId}`);
  output(await res.json());
}

async function makeGuess() {
  const guessedId = document.getElementById("guessId").value;
  const res = await fetch(`${API}/guess/${roomId}?guessedPlayerId=${guessedId}`, { method: "POST" });
  output(await res.json());
}

async function getResult() {
  const res = await fetch(`${API}/result/${roomId}`);
  output(await res.json());
}

function output(data) {
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}
