from typing import Optional


class ChessException(Exception):
    pass


class Piece:
    KING = "KING"
    QUEEN = "QUEEN"
    BISHOP = "BISHOP"
    KNIGHT = "KNIGHT"
    ROOK = "ROOK"
    PAWN = "PAWN"


class Board:
    def __init__(self, name: str, dim: int) -> None:
        self._name = name
        self._board = [dim*[None] for i in range(dim)]

    @property
    def name(self) -> str:
        return self._name

    @property
    def dim(self) -> int:
        return len(self._board)

    def add_piece(self, piece: Optional[str], x: int, y: int) -> None:
        try:
            self._board[x][y] = piece
        except IndexError as e:
            raise ChessException("Invalid board position: {}, {}".format(x, y))

    def get_piece(self, x: int, y: int) -> Optional[str]:
        try:
            return self._board[x][y]
        except IndexError as e:
            raise ChessException("Invalid board position: {}, {}".format(x, y))
