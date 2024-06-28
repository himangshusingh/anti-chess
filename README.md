# CLI Multiplayer Chess Game

  

This project is a CLI-based multiplayer anti-chess game that allows two players to play against each other over a network. 

  

## Requirements

  
They are mentioned in the requirements.txt file

  

## Installation

  

1. Clone the repository:

```
git clone https://github.com/yourusername/chess_game.git

cd anti-chess
```

   

  

2. Install the dependencies:

```
  
    pip install -r requirements.txt

```

  

## Running the Game

  

### Server

  

1. Navigate to the `server` directory:

```sh

    cd server

```

  

2. Run the server:

```

    python server.py

```

  

### Client

  

1. Navigate to the `client` directory:

```

    cd client

```

  

2. Run the client:

```

    python client.py

```

  

## How to Play

  

- The game will prompt each player to enter their command.

- Commands:

  - `D`: Display the board

  - `Q`: Quit the game (the other player wins)

  - `M`: Make a move (e.g., `A2 B4` to move the piece from A2 to B4)

- The game alternates turns between the two players.


## Note:

I any error occurs, best way to solve it at this point is to restart the server
