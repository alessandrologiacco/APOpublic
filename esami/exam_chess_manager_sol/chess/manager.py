from chess.board import Board, ChessException, Piece
from chess.competition import Player, Tournament
from typing import List, Optional


class ChessManager:
    def __init__(self) -> None:
        self._boards = {}
        self._players = {}
        self._tournaments = {}

    # R2
    def add_board(self, board: Board) -> None:
        self._boards[board.name] = board

    def get_board(self, name: str) -> Board:
        return self._boards[name]

    def add_player(self, player: Player) -> None:
        self._players[player.name] = player

    def get_player(self, name: str) -> Player:
        return self._players[name]

    def add_player_to_board(self, player_name: str, board_name: str) -> None:
        player = self._players[player_name]
        board = self._boards[board_name]
        player.add_board(board)

    def get_boards_of_player(self, name: str) -> List[Board]:
        return self._players[name].boards

    # R3
    def create_tournament(self, name: str) -> None:
        if name in self._tournaments:
            raise ChessException("Tournament already defined")
        self._tournaments[name] = Tournament(name)

    def add_player_score(self, tournament_name: str, player_name: str, score: int) -> None:
        if player_name not in self._players:
            raise ChessException("Player does not exist")
        tournament = self._tournaments[tournament_name]
        player = self._players[player_name]
        tournament.add_match(player, score)

    def get_leading_player(self, tournament_name: str) -> Optional[str]:
        tournament = self._tournaments[tournament_name]
        matches = tournament.matches
        if not matches:
            return None
        matches.sort(key=lambda match: match[1])
        return "{}:{}".format(matches[-1][0].name, matches[-1][1])

    # R5
    def fill_queens(self, board_name: str, board_size: int) -> Board:
        board = Board(board_name, board_size)
        ret = self.recursive_fill(board)
        return board

    def recursive_fill(self, board: Board, x: int = 0, y: int = 0, depth: int = 0) -> bool:
        if depth >= board.dim:
            return True
        for i in range(x, board.dim):
            for j in range(y, board.dim):
                if ChessManager.check_queen(board, i, j):
                    board.add_piece(Piece.QUEEN, i, j)
                    if self.recursive_fill(board, i + (j + 1) // board.dim, (j + 1) % board.dim, depth + 1):
                        return True
                    board.add_piece(None, i, j)
            y = 0
        return False

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















