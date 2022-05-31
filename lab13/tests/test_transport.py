import unittest
from transport.graph import GraphCreator
from transport.transport_network import BusNetwork, Stop


def populate_graph():
    # create empty graph
    g = GraphCreator.get_empty_graph()

    # create nodes dictionary that maps node name to IDs
    name_to_id = {
        "E": g.add_node("E"),
        "F": g.add_node("F"),
        "G": g.add_node("G"),
        "H": g.add_node("H")
    }

    # create_edges with weight
    g.add_edge("E->F", name_to_id["E"], name_to_id["F"])
    g.add_edge("E->G", name_to_id["E"], name_to_id["G"])
    g.add_edge("G->F", name_to_id["G"], name_to_id["F"])
    g.add_edge("F->H", name_to_id["F"], name_to_id["H"])
    g.add_edge("H->G", name_to_id["H"], name_to_id["G"])

    return g, name_to_id


class TestR1(unittest.TestCase):

    def setUp(self) -> None:
        self._graph, self._name_to_id = populate_graph()

    def test_repr(self):
        self.assertEqual(4, len(self._graph))

    def test_get_node(self):
        self.assertEqual("E", self._graph.get_node(self._name_to_id["E"]))
        self.assertEqual("F", self._graph.get_node(self._name_to_id["F"]))
        self.assertEqual("G", self._graph.get_node(self._name_to_id["G"]))
        self.assertEqual("H", self._graph.get_node(self._name_to_id["H"]))

    def test_get_connection(self):
        self.assertEqual("E->F", self._graph.get_edge(self._name_to_id["E"], self._name_to_id["F"]))
        self.assertEqual("E->G", self._graph.get_edge(self._name_to_id["E"], self._name_to_id["G"]))
        self.assertEqual("G->F", self._graph.get_edge(self._name_to_id["G"], self._name_to_id["F"]))
        self.assertEqual("F->H", self._graph.get_edge(self._name_to_id["F"], self._name_to_id["H"]))
        self.assertEqual("H->G", self._graph.get_edge(self._name_to_id["H"], self._name_to_id["G"]))

    def test_is_connected(self):
        self.assertTrue(self._graph.is_connected(self._name_to_id["E"], self._name_to_id["F"]))   # True
        self.assertFalse(self._graph.is_connected(self._name_to_id["F"], self._name_to_id["E"]))  # False
        self.assertFalse(self._graph.is_connected(self._name_to_id["H"], self._name_to_id["E"]))  # False


class TestR2(unittest.TestCase):

    def setUp(self) -> None:
        self._graph, self._name_to_id = populate_graph()

    def test_get_parents(self):
        parents = self._graph.get_parents(self._name_to_id["G"])
        self.assertTrue(self._name_to_id["E"] in parents)
        self.assertTrue(self._name_to_id["H"] in parents)
        self.assertEqual(2, len(parents))

    def test_get_children(self):
        children = self._graph.get_children(self._name_to_id["F"])
        self.assertTrue(self._name_to_id["H"] in children)
        self.assertEqual(1, len(children))

    def test_find_path(self):
        path = self._graph.find_path(self._name_to_id["H"], self._name_to_id["F"])
        self.assertEqual(["H", "G", "F"], [self._graph.get_node(node_id) for node_id in path])

    def test_empty_path(self):
        path = self._graph.find_path(self._name_to_id["H"], self._name_to_id["E"])
        self.assertFalse(path)


class TestR3(unittest.TestCase):

    def test_stop(self):
        s = Stop("fermata", 11.678234, 14.545661)
        self.assertEqual("fermata", s.name)
        self.assertEqual(11.678234, s.latitude)
        self.assertEqual(14.545661, s.longitude)

    def test_load_stops(self):
        bn = BusNetwork()
        bn.load_stops("./data/fermate.txt")
        stop = bn.get_stop("PORTA NUOVA")
        self.assertEqual("PORTA NUOVA", stop.name)
        self.assertEqual(45.062572, stop.latitude)
        self.assertEqual(7.677628, stop.longitude)

    def test_load_connections(self):
        bn = BusNetwork()
        bn.load_stops("./data/fermate.txt")
        bn.load_connections("./data/collegamenti.txt")
        self.assertEqual("24", bn.get_line("LAURO ROSSI EST", "SESIA"))


class TestR4(unittest.TestCase):

    def check_path(self, path, start_stop_name, end_stop_name):
        if path[0].split("->")[0].strip() != start_stop_name:
            print("Wrong first stop")
            return False
        if path[-1].split("->")[0].strip() != end_stop_name:
            print("Wrong last stop")
            return False
        for i in range(len(path) - 1):
            step = path[i].split("->")
            stop = step[0].strip()
            line = step[1].strip()
            next_stop = path[i + 1].split("->")[0].strip()
            if self._map[(stop, next_stop)] != line:
                print("Wrong bus line")
                return False
        last_line = path[-1].split("->")[1].strip()
        if last_line != "END":
            print("END missing")
            return False
        return True

    def setUp(self):
        self._bus_net = BusNetwork()
        self._bus_net.load_stops("./data/fermate.txt")
        self._bus_net.load_connections("./data/collegamenti.txt")

        # this is for the check
        self._map = {}
        with open("./data/collegamenti.txt", "r") as f:
            for line in f:
                line_lst = line.strip().split(",")
                bus_number = line_lst[0]
                start_node = line_lst[1]
                end_node = line_lst[2]
                self._map[(start_node, end_node)] = bus_number

    def test_find_itinerary(self):
        path = self._bus_net.compute_itinerary("PORTA NUOVA", "LINGOTTO")
        self.assertTrue(self.check_path(path, "PORTA NUOVA", "LINGOTTO"))