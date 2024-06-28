# CLI Multiplayer Chess Game

This project is a CLI-based multiplayer chess game that allows two players to play against each other over a network.

## Requirements

- Python 3.6 or higher
- Flask
- Flask-SocketIO
- python-socketio

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/chess_game.git
    cd chess_game
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Game

### Server

1. Navigate to the `server` directory:
    ```sh
    cd server
    ```

2. Run the server:
    ```sh
    python server.py
    ```

### Client

1. Navigate to the `client` directory:
    ```sh
    cd client
    ```

2. Run the client:
    ```sh
    python client.py
    ```

## How to Play

- The game will prompt each player to enter their command.
- Commands:
  - `D`: Display the board
  - `Q`: Quit the game (the other player wins)
  - `M`: Make a move (e.g., `A2 B4` to move the piece from A2 to B4)
- The game alternates turns between the two players.

## Additional Notes

- This implementation includes basic move validation and board display. The game logic is simplified for demonstration purposes.
