import unittest
from games.card_game import Card, Player, GameException, Tournament


class TestR1(unittest.TestCase):

    def test_getters(self):
        card = Card("Sightless Watcher", 3, 2, 2)
        self.assertEqual(card.name, "Sightless Watcher")
        self.assertEqual(card.attack, 3)
        self.assertEqual(card.mana_cost, 2)

    def test_is_dead_false(self):
        card = Card("Sightless Watcher", 3, 2, 2)
        self.assertEqual(card.life_points, 2)
        self.assertEqual(card.is_dead(), False)

    def test_is_dead_true(self):
        card = Card("Sightless Watcher", 3, -2, 2)
        self.assertEqual(card.is_dead(), True)

        card = Card("Sightless Watcher", 3, 0, 2)
        self.assertEqual(card.is_dead(), True)

    def test_repr(self):
        card = Card("Sightless Watcher", 3, -2, 2)
        self.assertEqual(str(card.__repr__()), "Sightless Watcher 3 -2 2")

    def test_fight_card(self):
        card_1 = Card("Sightless Watcher", 3, 2, 2)
        card_2 = Card("Novice Engineer", 1, 1, 2)
        Card.fight(card_1, card_2)
        self.assertEqual(card_1.life_points, 1)
        self.assertEqual(card_2.life_points, -2)


class TestR2(unittest.TestCase):

    def test_simple_getters(self):
        player = Player("Jeffrey Shih")
        player.mana = 3
        self.assertEqual(player.name, "Jeffrey Shih")
        self.assertEqual(player.mana, 3)

    def test_draw(self):
        player = Player("Jeffrey Shih")
        card_1 = Card("Sightless Watcher", 3, 2, 2)
        card_2 = Card("Novice Engineer", 1, 1, 2)
        player.draw(card_1)
        player.draw(card_2)
        self.assertEqual(len(player.hand), 2)
        self.assertTrue(card_1 in player.hand)
        self.assertTrue(card_2 in player.hand)

    def test_play(self):
        player = Player("Jeffrey Shih")
        player.mana = 10
        card_1 = Card("Sightless Watcher", 3, 2, 2)
        card_2 = Card("Novice Engineer", 1, 1, 2)
        player.draw(card_1)
        player.draw(card_2)

        player.play(card_1.name)
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(len(player.field), 1)
        self.assertTrue(card_1 in player.field)
        self.assertTrue(card_2 in player.hand)

        player.play(card_2.name)
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(len(player.field), 2)
        self.assertTrue(card_1 in player.field)
        self.assertTrue(card_2 in player.field)

    def test_mana_update(self):
        player = Player("Jeffrey Shih")
        player.mana = 4
        card_1 = Card("Sightless Watcher", 3, 2, 2)
        player.draw(card_1)
        player.play(card_1.name)
        self.assertEqual(player.mana, 2)

    def test_not_enough_mana(self):
        player = Player("Jeffrey Shih")
        player.mana = 1
        card_1 = Card("Sightless Watcher", 3, 2, 2)
        player.draw(card_1)
        self.assertRaises(GameException, player.play, card_1.name)


class TestR3(unittest.TestCase):

    def setUp(self):
        self.torneo = Tournament()

        player1 = Player("Jeffrey Shih")
        player2 = Player("Disguised Toast")
        self.torneo.add_player(player1)
        self.torneo.add_player(player2)

        card_1 = Card("Sightless Watcher", 3, 2, 2)
        card_2 = Card("Novice Engineer", 1, 1, 2)
        card_3 = Card("Raid Leader", 2, 3, 3)
        card_4 = Card("Chillwind Yeti", 4, 5, 4)
        card_5 = Card("Boulderfist Ogre", 6, 7, 6)
        card_6 = Card("War Golem", 7, 7, 7)

        self.cards = {
            "Sightless Watcher": card_1,
            "Novice Engineer": card_2,
            "Raid Leader": card_3,
            "Chillwind Yeti": card_4,
            "Boulderfist Ogre": card_5,
            "War Golem": card_6,
        }

        self.torneo.add_card(card_1)
        self.torneo.add_card(card_2)
        self.torneo.add_card(card_3)
        self.torneo.add_card(card_4)
        self.torneo.add_card(card_5)
        self.torneo.add_card(card_6)

        self.torneo.player_uses_card("Jeffrey Shih", "Sightless Watcher")
        self.torneo.player_uses_card("Jeffrey Shih", "Novice Engineer")
        self.torneo.player_uses_card("Jeffrey Shih", "Chillwind Yeti")
        self.torneo.player_uses_card("Jeffrey Shih", "War Golem")

        self.torneo.player_uses_card("Disguised Toast", "Raid Leader")
        self.torneo.player_uses_card("Disguised Toast", "Boulderfist Ogre")
        self.torneo.player_uses_card("Disguised Toast", "Novice Engineer")

    def test_get_cards_of_player(self):
        cards_1 = self.torneo.get_cards_of_player("Jeffrey Shih")
        cards_2 = self.torneo.get_cards_of_player("Disguised Toast")

        self.assertEqual(len(cards_1), 4)
        self.assertEqual(len(cards_2), 3)

        self.assertTrue(self.cards["Sightless Watcher"] in cards_1)
        self.assertTrue(self.cards["Novice Engineer"] in cards_1)
        self.assertTrue(self.cards["Chillwind Yeti"] in cards_1)
        self.assertTrue(self.cards["War Golem"] in cards_1)
        self.assertTrue(self.cards["Raid Leader"] in cards_2)
        self.assertTrue(self.cards["Boulderfist Ogre"] in cards_2)
        self.assertTrue(self.cards["Novice Engineer"] in cards_2)

    def test_get_players_of_card(self):
        players_1 = self.torneo.get_players_of_card("Chillwind Yeti")
        players_2 = self.torneo.get_players_of_card("Novice Engineer")

        self.assertEqual(len(players_1), 1)
        self.assertEqual(len(players_2), 2)

        self.assertTrue("Jeffrey Shih" in players_1)
        self.assertTrue("Jeffrey Shih" in players_2)
        self.assertTrue("Disguised Toast" in players_2)

    def test_add_duplicate_player(self):
        torneo = Tournament()
        player1 = Player("Jeffrey Shih")
        player2 = Player("Disguised Toast")
        torneo.add_player(player1)
        torneo.add_player(player2)
        self.assertRaises(GameException, torneo.add_player, player2)

    def test_get_cards_of_player_sorted(self):
        cards_1 = self.torneo.get_cards_of_player("Jeffrey Shih", sort_res=True)
        self.assertEqual(len(cards_1), 4)

        self.assertEqual(self.cards["Chillwind Yeti"], cards_1[0])
        self.assertEqual(self.cards["Novice Engineer"], cards_1[1])
        self.assertEqual(self.cards["Sightless Watcher"], cards_1[2])
        self.assertEqual(self.cards["War Golem"], cards_1[3])


class TestR5(unittest.TestCase):

    def setUp(self):
        self.player = Player("Jeffrey Shih")
        card_1 = Card("Sightless Watcher", 3, 2, 2)
        card_2 = Card("Novice Engineer", 1, 1, 2)
        card_3 = Card("Raid Leader", 2, 3, 3)
        card_4 = Card("Chillwind Yeti", 4, 5, 4)
        card_5 = Card("Boulderfist Ogre", 6, 7, 6)
        card_6 = Card("War Golem", 7, 7, 7)
        self.player.draw(card_1)
        self.player.draw(card_2)
        self.player.draw(card_3)
        self.player.draw(card_4)
        self.player.draw(card_5)
        self.player.draw(card_6)

    def test_no_best_play(self):
        self.player.mana = 1
        self.assertEqual(self.player.find_best_two(), [])

    def test_easy_best_play(self):
        self.player.mana = 20
        best = self.player.find_best_two()
        self.assertEqual(len(best), 2)
        self.assertTrue("Boulderfist Ogre" in best)
        self.assertTrue("War Golem" in best)

    def test_hard_best_play(self):
        self.player.mana = 8
        best = self.player.find_best_two()

        self.assertEqual(len(best), 2)
        self.assertTrue("Sightless Watcher" in best)
        self.assertTrue("Boulderfist Ogre" in best)


