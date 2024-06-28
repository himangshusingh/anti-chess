import socketio
from chess_board import AntiChessBoard

sio = socketio.Client()
board = AntiChessBoard()
player_role = None

@sio.event
def connect():
    print("Connected to the server")

@sio.event
def disconnect():
    print("Disconnected from the server")

@sio.event
def assign_role(data):
    global player_role
    player_role = data['role']
    print(f"You are playing as {player_role}")

@sio.event
def start_game(data):
    print(data['message'])
    board.display_board()
    if board.get_current_turn() == player_role:
        game_loop()

@sio.event
def move(data):
    print(f"Move received: {data['move']}")
    start, end = data['move'][:2], data['move'][2:]
    board.move_piece(start, end)
    board.display_board()
    if board.get_current_turn() == player_role:
        game_loop()

@sio.event
def invalid_move(data):
    print(data['message'])
    if board.get_current_turn() == player_role:
        game_loop()

@sio.event
def game_over(data):
    print(data['message'])
    sio.disconnect()

def game_loop():
    if board.get_current_turn() == player_role:
        print(f"{player_role.capitalize()}'s turn")
        command = input("Options: (D)isplay, (Q)uit, (M)ove\n").upper()
        if command == 'D':
            board.display_board()
            game_loop()
        elif command == 'Q':
            sio.disconnect()
        elif command == 'M':
            move = input("Enter your move (e.g., A2 A4): ").lower().replace(" ", "")
            if len(move) == 4 and board.is_valid_move(move[:2], move[2:]):
                sio.emit('move', move)
            else:
                print("Invalid move. Try again.")
                game_loop()
        else:
            print("Invalid command. Please enter D, Q, or M.")
            game_loop()
    else:
        print(f"Waiting for {board.get_current_turn()} to move...")

if __name__ == '__main__':
    try:
        sio.connect('http://localhost:5000')
        sio.wait()
    except socketio.exceptions.ConnectionError as e:
        print(f"Error connecting to server: {e}")
