from typing import List


class GameException(Exception):
    pass


class Card:
    def __init__(self, name: str, attack: int, life_points: int, mana_cost: int) -> None:
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def attack(self) -> int:
        pass

    @property
    def life_points(self) -> int:
        pass

    @property
    def mana_cost(self) -> int:
        pass

    def is_dead(self) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    @staticmethod
    def fight(card1: "Card", card2: "Card") -> None:
        pass


class Player:
    def __init__(self, name: str) -> None:
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def field(self) -> List[Card]:
        pass

    @property
    def hand(self) -> List[Card]:
        pass

    @property
    def mana(self) -> int:
        pass

    @mana.setter
    def mana(self, mana) -> None:
        pass

    def draw(self, card: Card) -> None:
        pass

    def play(self, card_name: str) -> None:
        pass

    def find_best_two(self) -> List[str]:
        pass


class Tournament:
    def __init__(self) -> None:
        pass

    def add_player(self, player) -> None:
        pass

    def add_card(self, card) -> None:
        pass

    def player_uses_card(self, player_name, card_name) -> None:
        pass

    def get_cards_of_player(self, player_name, sort_res=False) -> List[Card]:
        pass

    def get_players_of_card(self, card_name) -> List[str]:
        pass

