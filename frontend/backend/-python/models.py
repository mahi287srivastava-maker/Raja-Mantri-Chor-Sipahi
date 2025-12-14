import uuid

class Player:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.role = None
        self.points = 0

class Room:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.players = []
        self.roles_assigned = False
