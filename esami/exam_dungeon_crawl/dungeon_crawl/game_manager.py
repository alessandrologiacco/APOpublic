from typing import List, Optional


class DungeonCrawlException(Exception):
    pass


class DungeonCrawlGame:

    def __init__(self):
        pass

    # R1
    def add_effect(self, effect_name: str, description: str, symbol: str) -> None:
        pass

    def add_action(self, action_name: str, description: str) -> None:
        pass

    def get_action_or_effect(self, name: str) -> str:
        pass

    # R2
    def add_card(self, card_name: str, level: int) -> None:
        pass

    def add_effect_to_card(self, card_name: str, effect_name: str) -> None:
        pass

    def add_action_to_card(self, card_name: str, action_name: str, value: int, action_range: int) -> None:
        pass

    def get_card_effects(self, card_name: str) -> List[str]:
        pass

    def get_card_actions(self, card_name: str) -> List[str]:
        pass

    # R3
    def add_role(self, role_name: str, num_card: int) -> None:
        pass

    def add_card_to_role(self, role_name: str, card_name: str) -> None:
        pass

    def get_role_cards(self, role_name: str, max_level: Optional[int] = None) -> List[str]:
        pass

    # R5
    def add_character(self, character_name: str, role_name: str, level: int) -> None:
        pass

    def play_cards(self, character_name: str, card_1_name: str, card_2_name: str) -> None:
        pass
