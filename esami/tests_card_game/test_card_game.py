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






















# def populate_graph():
#     # create empty graph
#     g = GraphCreator.get_empty_graph()
#
#     # create nodes dictionary that maps node name to IDs
#     name_to_id = {
#         "E": g.add_node("E"),
#         "F": g.add_node("F"),
#         "G": g.add_node("G"),
#         "H": g.add_node("H")
#     }
#
#     # create_edges with weight
#     g.add_edge("E->F", name_to_id["E"], name_to_id["F"])
#     g.add_edge("E->G", name_to_id["E"], name_to_id["G"])
#     g.add_edge("G->F", name_to_id["G"], name_to_id["F"])
#     g.add_edge("F->H", name_to_id["F"], name_to_id["H"])
#     g.add_edge("H->G", name_to_id["H"], name_to_id["G"])
#
#     return g, name_to_id
#
#
# class TestR1(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self._graph, self._name_to_id = populate_graph()
#
#     def test_repr(self):
#         self.assertEqual(4, len(self._graph))
#
#     def test_get_node(self):
#         self.assertEqual("E", self._graph.get_node(self._name_to_id["E"]))
#         self.assertEqual("F", self._graph.get_node(self._name_to_id["F"]))
#         self.assertEqual("G", self._graph.get_node(self._name_to_id["G"]))
#         self.assertEqual("H", self._graph.get_node(self._name_to_id["H"]))
#
#     def test_get_connection(self):
#         self.assertEqual("E->F", self._graph.get_edge(self._name_to_id["E"], self._name_to_id["F"]))
#         self.assertEqual("E->G", self._graph.get_edge(self._name_to_id["E"], self._name_to_id["G"]))
#         self.assertEqual("G->F", self._graph.get_edge(self._name_to_id["G"], self._name_to_id["F"]))
#         self.assertEqual("F->H", self._graph.get_edge(self._name_to_id["F"], self._name_to_id["H"]))
#         self.assertEqual("H->G", self._graph.get_edge(self._name_to_id["H"], self._name_to_id["G"]))
#
#     def test_is_connected(self):
#         self.assertTrue(self._graph.is_connected(self._name_to_id["E"], self._name_to_id["F"]))   # True
#         self.assertFalse(self._graph.is_connected(self._name_to_id["F"], self._name_to_id["E"]))  # False
#         self.assertFalse(self._graph.is_connected(self._name_to_id["H"], self._name_to_id["E"]))  # False
#
#
# class TestR2(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self._graph, self._name_to_id = populate_graph()
#
#     def test_get_parents(self):
#         parents = self._graph.get_parents(self._name_to_id["G"])
#         self.assertTrue(self._name_to_id["E"] in parents)
#         self.assertTrue(self._name_to_id["H"] in parents)
#         self.assertEqual(2, len(parents))
#
#     def test_get_children(self):
#         children = self._graph.get_children(self._name_to_id["F"])
#         self.assertTrue(self._name_to_id["H"] in children)
#         self.assertEqual(1, len(children))
#
#     def test_find_path(self):
#         path = self._graph.find_path(self._name_to_id["H"], self._name_to_id["F"])
#         self.assertEqual(["H", "G", "F"], [self._graph.get_node(node_id) for node_id in path])
#
#     def test_empty_path(self):
#         path = self._graph.find_path(self._name_to_id["H"], self._name_to_id["E"])
#         self.assertFalse(path)
#
#
# class TestR3(unittest.TestCase):
#
#     def test_stop(self):
#         s = Stop("fermata", 11.678234, 14.545661)
#         self.assertEqual("fermata", s.name)
#         self.assertEqual(11.678234, s.latitude)
#         self.assertEqual(14.545661, s.longitude)
#
#     def test_load_stops(self):
#         bn = BusNetwork()
#         bn.load_stops("./data/fermate.txt")
#         stop = bn.get_stop("PORTA NUOVA")
#         self.assertEqual("PORTA NUOVA", stop.name)
#         self.assertEqual(45.062572, stop.latitude)
#         self.assertEqual(7.677628, stop.longitude)
#
#     def test_load_connections(self):
#         bn = BusNetwork()
#         bn.load_stops("./data/fermate.txt")
#         bn.load_connections("./data/collegamenti.txt")
#         self.assertEqual("24", bn.get_line("LAURO ROSSI EST", "SESIA"))
#
#
# class TestR4(unittest.TestCase):
#
#     def check_path(self, path, start_stop_name, end_stop_name):
#         if path[0].split("->")[0].strip() != start_stop_name:
#             print("Wrong first stop")
#             return False
#         if path[-1].split("->")[0].strip() != end_stop_name:
#             print("Wrong last stop")
#             return False
#         for i in range(len(path) - 1):
#             step = path[i].split("->")
#             stop = step[0].strip()
#             line = step[1].strip()
#             next_stop = path[i + 1].split("->")[0].strip()
#             if self._map[(stop, next_stop)] != line:
#                 print("Wrong bus line")
#                 return False
#         last_line = path[-1].split("->")[1].strip()
#         if last_line != "END":
#             print("END missing")
#             return False
#         return True
#
#     def setUp(self):
#         self._bus_net = BusNetwork()
#         self._bus_net.load_stops("./data/fermate.txt")
#         self._bus_net.load_connections("./data/collegamenti.txt")
#
#         # this is for the check
#         self._map = {}
#         with open("./data/collegamenti.txt", "r") as f:
#             for line in f:
#                 line_lst = line.strip().split(",")
#                 bus_number = line_lst[0]
#                 start_node = line_lst[1]
#                 end_node = line_lst[2]
#                 self._map[(start_node, end_node)] = bus_number
#
#     def test_find_itinerary(self):
#         path = self._bus_net.compute_itinerary("PORTA NUOVA", "LINGOTTO")
#         self.assertTrue(self.check_path(path, "PORTA NUOVA", "LINGOTTO"))
