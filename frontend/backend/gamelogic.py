import random

ROLES = ["Raja", "Mantri", "Chor", "Sipahi"]
POINTS = {"Raja": 1000, "Mantri": 800, "Sipahi": 500, "Chor": 0}

def assign_roles(players):
    random.shuffle(ROLES)
    for p, r in zip(players, ROLES):
        p.role = r
        p.points = POINTS[r]

def evaluate_guess(players, guessed_id):
    chor = next(p for p in players if p.role == "Chor")
    if chor.id == guessed_id:
        return "Correct Guess"
    else:
        chor.points += 1300
        return "Wrong Guess"
