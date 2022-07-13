import unittest
from dungeon_crawl.game_manager import DungeonCrawlGame, DungeonCrawlException


class TestR1(unittest.TestCase):

    def setUp(self) -> None:
        self._game = DungeonCrawlGame()

    def test_get_non_present(self):
        self.assertRaises(DungeonCrawlException, self._game.get_action_or_effect, "Effetto 567")

    def test_get_effect(self):
        self._game.add_effect("Effetto 1", "Descr. 1", "X")
        self.assertEqual("X: Descr. 1", self._game.get_action_or_effect("Effetto 1"))

    def test_get_action(self):
        self._game.add_action("Azione 1", "Descr. 1")
        self.assertEqual("Azione 1: Descr. 1", self._game.get_action_or_effect("Azione 1"))

    def test_get_action_and_effects(self):
        self._game.add_effect("Effetto 1", "Descr. 1", "X")
        self._game.add_action("Azione 1", "Descr. 1")
        self.assertEqual("Azione 1: Descr. 1", self._game.get_action_or_effect("Azione 1"))
        self.assertEqual("X: Descr. 1", self._game.get_action_or_effect("Effetto 1"))

    def test_get_action_and_effects_multiple(self):
        self._game.add_effect("Effetto 1", "Descr. 1", "X")
        self._game.add_action("Azione 1", "Descr. 1")
        self._game.add_effect("Effetto 2", "Descr. 2", "O")
        self._game.add_action("Azione 2", "Descr. 2")
        self.assertEqual("Azione 1: Descr. 1", self._game.get_action_or_effect("Azione 1"))
        self.assertEqual("X: Descr. 1", self._game.get_action_or_effect("Effetto 1"))
        self.assertEqual("Azione 2: Descr. 2", self._game.get_action_or_effect("Azione 2"))
        self.assertEqual("O: Descr. 2", self._game.get_action_or_effect("Effetto 2"))


class TestR2(unittest.TestCase):

    def setUp(self):
        self._game = DungeonCrawlGame()
        self._game.add_effect("Effetto 1", "Descr. 1", "X")
        self._game.add_action("Azione 1", "Descr. 2")
        self._game.add_effect("Effetto 2", "Descr. 3", "O")
        self._game.add_action("Azione 2", "Descr. 4")
        self._game.add_card("Carta A", 1)
        self._game.add_card("Carta B", 2)

    def test_get_card_effects(self):
        self._game.add_effect_to_card("Carta A", "Effetto 2")
        self._game.add_effect_to_card("Carta A", "Effetto 1")
        self.assertEqual(["Effetto 1", "Effetto 2"], self._game.get_card_effects("Carta A"))

    def test_get_card_effect_hard(self):
        self._game.add_effect_to_card("Carta A", "Effetto 2")
        self._game.add_effect_to_card("Carta A", "Effetto 1")
        self._game.add_action_to_card("Carta A", "Azione 1", value=1, action_range=2)
        self._game.add_action_to_card("Carta B", "Azione 2", value=3, action_range=4)
        self.assertEqual(["Effetto 1", "Effetto 2"], self._game.get_card_effects("Carta A"))

    def test_get_card_actions(self):
        self._game.add_action_to_card("Carta A", "Azione 1", value=1, action_range=2)
        self._game.add_action_to_card("Carta A", "Azione 2", value=3, action_range=4)
        actions = self._game.get_card_actions("Carta A")
        self.assertEqual(2, len(actions))
        self.assertTrue("Azione 1,1,2" in actions)
        self.assertTrue("Azione 2,3,4" in actions)

    def test_get_card_actions_hard(self):
        self._game.add_action_to_card("Carta A", "Azione 1", value=1, action_range=2)
        self._game.add_action_to_card("Carta A", "Azione 2", value=3, action_range=4)
        self._game.add_action_to_card("Carta B", "Azione 1", value=5, action_range=6)
        actions = self._game.get_card_actions("Carta A")
        self.assertEqual(2, len(actions))
        self.assertTrue("Azione 1,1,2" in actions)
        self.assertTrue("Azione 2,3,4" in actions)
        actions = self._game.get_card_actions("Carta B")
        self.assertEqual(["Azione 1,5,6"], actions)

    def test_get_effect_actions_empty(self):
        self.assertEqual([], self._game.get_card_effects("Carta A"))
        self.assertEqual([], self._game.get_card_actions("Carta B"))


class TestR3(unittest.TestCase):

    def setUp(self):
        self._game = DungeonCrawlGame()
        self._game.add_card("Carta A", 1)
        self._game.add_card("Carta B", 2)
        self._game.add_card("Carta C", 3)
        self._game.add_card("Carta D", 4)
        self._game.add_card("Carta E", 5)

        self._game.add_role("Ruolo 1", 1)
        self._game.add_role("Ruolo 2", 2)
        self._game.add_role("Ruolo 3", 3)

    def test_non_existent(self):
        self._game.add_card_to_role("Ruolo 1", "Carta A")
        self.assertRaises(DungeonCrawlException, self._game.add_card_to_role, "Ruolo 1", "Carta F")
        self.assertRaises(DungeonCrawlException, self._game.add_card_to_role, "Ruolo 7", "Carta A")

    def test_get_role_cards_all(self):
        self._game.add_card_to_role("Ruolo 1", "Carta A")
        self._game.add_card_to_role("Ruolo 1", "Carta B")
        self._game.add_card_to_role("Ruolo 2", "Carta B")
        self._game.add_card_to_role("Ruolo 2", "Carta C")

        cards = self._game.get_role_cards("Ruolo 1")
        self.assertEqual(2, len(cards))
        self.assertTrue("Carta A" in cards)
        self.assertTrue("Carta B" in cards)

        cards = self._game.get_role_cards("Ruolo 2")
        self.assertEqual(2, len(cards))
        self.assertTrue("Carta B" in cards)
        self.assertTrue("Carta C" in cards)

    def test_get_role_cards_level(self):
        self._game.add_card_to_role("Ruolo 1", "Carta A")
        self._game.add_card_to_role("Ruolo 1", "Carta B")
        self._game.add_card_to_role("Ruolo 1", "Carta C")
        self._game.add_card_to_role("Ruolo 1", "Carta D")

        cards = self._game.get_role_cards("Ruolo 1", max_level=3)
        self.assertEqual(3, len(cards))
        self.assertTrue("Carta A" in cards)
        self.assertTrue("Carta B" in cards)
        self.assertTrue("Carta C" in cards)

    def test_get_role_cards_empty(self):
        self._game.add_card_to_role("Ruolo 1", "Carta C")
        self.assertEqual([], self._game.get_role_cards("Ruolo 1", 2))
        self.assertEqual([], self._game.get_role_cards("Ruolo 2"))


class TestR5(unittest.TestCase):

    def setUp(self):
        self._game = DungeonCrawlGame()
        self._game.add_card("Carta A", 4)
        self._game.add_card("Carta B", 5)
        self._game.add_card("Carta C", 6)
        self._game.add_card("Carta D", 7)

        self._game.add_role("Ruolo 1", 2)
        self._game.add_role("Ruolo 2", 4)

        self._game.add_card_to_role("Ruolo 1", "Carta A")
        self._game.add_card_to_role("Ruolo 1", "Carta B")
        self._game.add_card_to_role("Ruolo 1", "Carta C")
        self._game.add_card_to_role("Ruolo 1", "Carta D")
        self._game.add_card_to_role("Ruolo 2", "Carta A")
        self._game.add_card_to_role("Ruolo 2", "Carta B")
        self._game.add_card_to_role("Ruolo 2", "Carta C")
        self._game.add_card_to_role("Ruolo 2", "Carta D")

        self._game.add_character("C1", "Ruolo 1", level=8)
        self._game.add_character("C2", "Ruolo 2", level=8)
        self._game.add_character("C3", "Ruolo 2", level=6)

    def test_play_cards_max_reached(self):
        self._game.play_cards("C1", "Carta A", "Carta B")
        self.assertRaises(DungeonCrawlException, self._game.play_cards, "C1", "Carta C", "Carta D")

    def test_play_cards_level_low(self):
        self._game.play_cards("C3", "Carta A", "Carta B")
        self.assertRaises(DungeonCrawlException, self._game.play_cards, "C3", "Carta C", "Carta D")

    def test_play_cards_duplicate(self):
        self._game.play_cards("C2", "Carta A", "Carta B")
        self.assertRaises(DungeonCrawlException, self._game.play_cards, "C2", "Carta B", "Carta C")




























