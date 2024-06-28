import chess

class AntiChessBoard:
    def __init__(self):
        self.board = chess.Board()
        self.current_turn = 'white'  # Initial turn is white

    def display_board(self):
        print("----------------")
        print("a b c d e f g h")
        print("----------------")
        print(self.board)
        print("----------------")
        print("a b c d e f g h")
        print("----------------")

    def move_piece(self, start, end):
        move = chess.Move.from_uci(f"{start}{end}")
        self.board.push(move)
        self.switch_turn()  # Switch turn after making a move
        print(f"Moved piece from {start} to {end}")
        self.display_board()

    def is_valid_move(self, start, end):
        move = chess.Move.from_uci(f"{start}{end}")
        legal_moves = list(self.board.legal_moves)
        # Check if there are any captures available
        captures = [m for m in legal_moves if self.board.is_capture(m)]
        if captures:
            # If captures are available, only those are valid
            return move in captures
        else:
            # If no captures are available, any legal move is valid
            return move in legal_moves

    def switch_turn(self):
        self.current_turn = 'black' if self.board.turn == chess.WHITE else 'white'
        print(f"Turn switched to {self.current_turn}")

    def get_current_turn(self):
        return 'white' if self.board.turn == chess.WHITE else 'black'

    def check_winner(self):
        if self.board.is_game_over():
            if self.board.result() == '1-0':
                return 'black'  # Black wins (white has no legal moves)
            elif self.board.result() == '0-1':
                return 'white'  # White wins (black has no legal moves)
            elif self.board.result() == '1/2-1/2':
                return 'draw'
        # Check if a player has no pieces left
        white_pieces = sum(1 for piece in self.board.piece_map().values() if piece.color == chess.WHITE)
        black_pieces = sum(1 for piece in self.board.piece_map().values() if piece.color == chess.BLACK)
        if white_pieces == 0:
            return 'white'
        elif black_pieces == 0:
            return 'black'
        return None