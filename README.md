# Raja–Mantri–Chor–Sipahi Game

This project is a simple backend implementation of the
Raja–Mantri–Chor–Sipahi game. I worked on this as part of a coding club
selection task while I am still learning the basics of backend
development.

The main goal of this project was to understand how a game’s logic can
be handled using backend APIs rather than focusing on frontend design.

## What I Have Implemented
- Creating a game room
- Joining a room with a maximum of 4 players
- Randomly assigning roles once all players join
- Allowing each player to see only their own role
- Handling the Mantri’s guess
- Showing final roles and points

## Technologies Used
- Python with FastAPI (for backend APIs)
- HTML, CSS, and JavaScript (basic frontend for testing)
- In-memory data storage (no database)

## How It Works (Simple Explanation)
- One player creates a room and others join using the room ID.
- When four players join, the backend assigns roles randomly.
- Each player can request their role privately.
- The Mantri makes a guess for the Chor.
- The backend checks the guess and shows the final result.

## Limitations
- Only a single round is supported
- No real-time updates
- UI/UX is very basic

## What I Learned
- How APIs work and communicate with each other
- How to manage basic game logic on the backend
- How to structure a small project repository

## Future Improvements
- Adding multiple rounds
- Improving UI/UX
- Learning and adding database support

## Note
This project is still a learning exercise, and there may be areas where
the code can be improved. The focus was on understanding concepts rather
than writing perfect code.
