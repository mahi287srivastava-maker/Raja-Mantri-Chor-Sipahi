from fastapi import FastAPI, HTTPException
from models import Room, Player
from game_logic import assign_roles, evaluate_guess

app = FastAPI()
rooms = {}

@app.post("/room/create")
def create_room(name: str):
    room = Room()
    player = Player(name)
    room.players.append(player)
    rooms[room.id] = room
    return {"roomId": room.id, "playerId": player.id}

@app.post("/room/join")
def join_room(roomId: str, name: str):
    room = rooms.get(roomId)
    if not room or len(room.players) >= 4:
        raise HTTPException(400, "Room invalid or full")
    player = Player(name)
    room.players.append(player)
    return {"playerId": player.id}

@app.post("/room/assign/{roomId}")
def assign(roomId: str):
    room = rooms.get(roomId)
    if len(room.players) != 4:
        raise HTTPException(400, "Need exactly 4 players")
    assign_roles(room.players)
    room.roles_assigned = True
    return {"status": "Roles assigned"}

@app.get("/role/me/{roomId}/{playerId}")
def my_role(roomId: str, playerId: str):
    room = rooms[roomId]
    for p in room.players:
        if p.id == playerId:
            return {"role": p.role}
    raise HTTPException(404)

@app.post("/guess/{roomId}")
def guess(roomId: str, guessedPlayerId: str):
    room = rooms[roomId]
    return {"result": evaluate_guess(room.players, guessedPlayerId)}

@app.get("/result/{roomId}")
def result(roomId: str):
    room = rooms[roomId]
    return [{"name": p.name, "role": p.role, "points": p.points} for p in room.players]
