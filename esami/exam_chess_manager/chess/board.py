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
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def dim(self) -> int:
        pass

    def add_piece(self, piece: Optional[str], x: int, y: int) -> None:
        pass

    def get_piece(self, x: int, y: int) -> Optional[str]:
        pass
