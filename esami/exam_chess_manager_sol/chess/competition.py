from chess.board import Board
from typing import List, Tuple


class Player:
    def __init__(self, name: str, nationality: str, age: int) -> None:
        self._name = name
        self._nationality = nationality
        self._age = age
        self._boards = []

    @property
    def name(self) -> str:
        return self._name

    def add_board(self, board: Board) -> None:
        self._boards.append(board)

    @property
    def boards(self) -> List[Board]:
        return self._boards

    def __repr__(self) -> str:
        return "{},{},{}".format(self._name, self._nationality, self._age)


class Tournament:
    def __init__(self, name: str):
        self._name = name
        self._matches = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def matches(self) -> List[Tuple[Player, str]]:
        return self._matches

    def add_match(self, player: Player, score: int) -> None:
        self._matches.append((player, score))

