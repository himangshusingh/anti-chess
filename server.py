import socketio
from chess_board import AntiChessBoard

sio = socketio.Server()
app = socketio.WSGIApp(sio)
board = AntiChessBoard()
players = []

@sio.event
def connect(sid, environ):
    if len(players) < 2:
        players.append(sid)
        role = 'white' if len(players) == 1 else 'black'
        sio.emit('assign_role', {'role': role}, room=sid)
        print(f"Player {len(players)} connected: {sid} as {role}")
        if len(players) == 2:
            sio.emit('start_game', {'message': 'Game started!'}, room=players)
    else:
        sio.disconnect(sid)

@sio.event
def disconnect(sid):
    if sid in players:
        players.remove(sid)
        print(f"Player disconnected: {sid}")
        if players:
            remaining_player = players[0]
            sio.emit('game_over', {'message': 'The other player has disconnected. You win!'}, room=remaining_player)
        else:
            print("No players left in the game.")

@sio.event
def move(sid, data):
    print(f"Move received from client: {data}")  # Debugging print
    start, end = data[:2], data[2:]
    if board.is_valid_move(start, end):
        board.move_piece(start, end)
        winner = board.check_winner()
        if winner:
            sio.emit('game_over', {'message': f"{winner} wins!"}, room=players)
        else:
            sio.emit('move', {'move': data, 'turn': board.get_current_turn()}, room=players)
    else:
        sio.emit('invalid_move', {'message': 'Invalid move. Try again.'}, room=sid)

if __name__ == '__main__':
    import eventlet
    import eventlet.wsgi
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
