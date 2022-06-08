from chess.board import Board
from chess.competition import Player
from typing import List, Optional


class ChessManager:
    def __init__(self) -> None:
        pass

    # R2
    def add_board(self, board: Board) -> None:
        pass

    def get_board(self, name: str) -> Board:
        pass

    def add_player(self, player: Player) -> None:
        pass

    def get_player(self, name: str) -> Player:
        pass

    def add_player_to_board(self, player_name: str, board_name: str) -> None:
        pass

    def get_boards_of_player(self, name: str) -> List[Board]:
        pass

    # R3
    def create_tournament(self, name: str) -> None:
        pass

    def add_player_score(self, tournament_name: str, player_name: str, score: int) -> None:
        pass

    def get_leading_player(self, tournament_name: str) -> Optional[str]:
        pass

    # R5
    def fill_queens(self, board_name: str, board_size: int) -> Board:
        pass

    @staticmethod
    # METODO GIÀ FORNITO
    # controlla se è possibile inserire regina in posizione x, y:
    # - cella vuota
    # - non sotto attacco da altre regine
    def check_queen(board: Board, x: int, y: int) -> bool:
        # controllo riga-colonna
        for i in range(board.dim):
            if board.get_piece(i, y) is not None or board.get_piece(x, i) is not None:
                return False
        # controllo diagonale primaria
        x_pos = x - min(x, y)
        y_pos = y - min(x, y)
        while x_pos < board.dim and y_pos < board.dim:
            if board.get_piece(x_pos, y_pos) is not None:
                return False
            x_pos += 1
            y_pos += 1
        # controllo diagonale secondaria
        x_pos = x - min(x, board.dim - y - 1)
        y_pos = y + min(x, board.dim - y - 1)
        while x_pos < board.dim and y_pos >= 0:
            if board.get_piece(x_pos, y_pos) is not None:
                return False
            x_pos += 1
            y_pos -= 1
        return True















