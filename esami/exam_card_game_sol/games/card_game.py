from typing import List, Dict, Set


class GameException(Exception):
    pass


class Card:
    def __init__(self, name: str, attack: int, life_points: int, mana_cost: int) -> None:
        self._name = name
        self._attack = attack
        self._life_points = life_points
        self._mana_cost = mana_cost
        self._players = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def life_points(self) -> int:
        return self._life_points

    @property
    def mana_cost(self) -> int:
        return self._mana_cost

    def is_dead(self) -> bool:
        return self._life_points <= 0

    def __repr__(self) -> str:
        return "{} {} {} {}".format(self._name, self._attack, self._life_points, self._mana_cost)

    @staticmethod
    def fight(card1: "Card", card2: "Card") -> None:
        card1._life_points -= card2._attack
        card2._life_points -= card1._attack

    def add_player(self, player) -> None:
        self._players.append(player)

    @property
    def players(self) -> List["Player"]:
        return self._players


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._mana = 0
        self._hand = {}
        self._field = {}
        self._cards = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def field(self) -> List[Card]:
        return list(self._field.values())

    @property
    def hand(self) -> List[Card]:
        return list(self._hand.values())

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, mana) -> None:
        self._mana = mana

    def draw(self, card: Card) -> None:
        self._hand[card.name] = card

    def play(self, card_name: str) -> None:
        to_play = self._hand[card_name]
        if to_play.mana_cost > self._mana:
            raise GameException("Not enough mana")
        self._field[card_name] = to_play
        self._hand.pop(card_name)
        self._mana -= to_play.mana_cost

    def add_card(self, card) -> None:
        self._cards.append(card)

    @property
    def cards(self) -> List[Card]:
        return self._cards

    def find_best_two(self) -> List[str]:
        sorted_hand = sorted(self._hand.values(), key=lambda x: x.attack, reverse=True)
        available_mana = self._mana
        best_play = []
        for i in range(len(sorted_hand)):
            first_card = sorted_hand[i]
            if available_mana >= first_card.mana_cost:
                best_play.append(first_card.name)
                available_mana -= first_card.mana_cost
                for j in range(i+1, len(sorted_hand)):
                    second_card = sorted_hand[j]
                    if available_mana >= second_card.mana_cost:
                        best_play.append(second_card.name)
                        return best_play
                available_mana += first_card.mana_cost
                best_play.pop()
        return []


class Tournament:
    def __init__(self) -> None:
        self._players = {}
        self._cards = {}

    def add_player(self, player) -> None:
        if player.name in self._players:
            raise GameException("Duplicated player")
        self._players[player.name] = player

    def add_card(self, card) -> None:
        self._cards[card.name] = card

    def player_uses_card(self, player_name, card_name) -> None:
        card = self._cards[card_name]
        player = self._players[player_name]
        player.add_card(card)
        card.add_player(player)

    def get_cards_of_player(self, player_name, sort_res=False) -> List[Card]:
        cards = self._players[player_name].cards
        if sort_res:
            cards = sorted(cards, key=lambda x: x.name)
        return cards

    def get_players_of_card(self, card_name) -> List[str]:
        return [player.name for player in self._cards[card_name].players]

