from transport.graph import GraphCreator
from transport.transport_network import BusNetwork


# this function crates a simple graph
def populate_graph():
    # create empty graph
    g = GraphCreator.get_empty_graph()

    # create nodes dictionary that maps node name to IDs
    name_to_id = {
        "A": g.add_node("A"),
        "B": g.add_node("B"),
        "C": g.add_node("C"),
        "D": g.add_node("D")
    }

    # create_edges with weight
    g.add_edge("A->B", name_to_id["A"], name_to_id["B"])
    g.add_edge("A->C", name_to_id["A"], name_to_id["C"])
    g.add_edge("C->B", name_to_id["C"], name_to_id["B"])
    g.add_edge("B->D", name_to_id["B"], name_to_id["D"])
    g.add_edge("D->C", name_to_id["D"], name_to_id["C"])

    return g, name_to_id


def check_path(bus_network, path, start_stop_name, end_stop_name):
    if path[0].split("->")[0].strip() != start_stop_name:
        print("Wrong first stop")
        return
    if path[-1].split("->")[0].strip() != end_stop_name:
        print("Wrong last stop")
        return
    for i in range(len(path)-1):
        step = path[i].split("->")
        stop = step[0].strip()
        line = step[1].strip()
        next_stop = path[i+1].split("->")[0].strip()
        if bus_network.get_line(stop, next_stop) != line:
            print("Wrong bus line")
            return
    last_line = path[-1].split("->")[1].strip()
    if last_line != "END":
        print("END missing")
        return
    print("PATH OK")


def main():
    print("--------- R1 ----------")
    g, name_to_id = populate_graph()
    print(len(g))  # 4

    print(g.get_node(name_to_id["A"]))  # A
    print(g.get_node(name_to_id["B"]))  # B
    print(g.get_node(name_to_id["C"]))  # C
    print(g.get_node(name_to_id["D"]))  # D

    print(g.get_edge(name_to_id["A"], name_to_id["B"]))  # A->B
    print(g.get_edge(name_to_id["A"], name_to_id["C"]))  # A->C
    print(g.get_edge(name_to_id["C"], name_to_id["B"]))  # C->B
    print(g.get_edge(name_to_id["B"], name_to_id["D"]))  # B->D
    print(g.get_edge(name_to_id["D"], name_to_id["C"]))  # D->C

    print(g.is_connected(name_to_id["A"], name_to_id["B"]))  # True
    print(g.is_connected(name_to_id["B"], name_to_id["A"]))  # False
    print(g.is_connected(name_to_id["D"], name_to_id["A"]))  # False

    print("--------- R2 ----------")
    print([g.get_node(node_id) for node_id in g.get_parents(name_to_id["B"])])  # ['A', 'C']
    print([g.get_node(node_id) for node_id in g.get_children(name_to_id["A"])])  # ['B', 'C']

    print([g.get_node(node_id) for node_id in g.find_path(name_to_id["A"], name_to_id["D"])])   # ['A', 'B', 'D'] oppure
                                                                                                # ['A', 'C', 'B', 'D']

    print([g.get_node(node_id) for node_id in g.find_path(name_to_id["D"], name_to_id["A"])])   # []

    print("--------- R3 ----------")
    bn = BusNetwork()
    bn.load_stops("./data/fermate.txt")
    bn.load_connections("./data/collegamenti.txt")

    stop = bn.get_stop("STATI UNITI")
    print(stop.name)        # STATI UNITI
    print(stop.latitude)    # 45.063184
    print(stop.longitude)   # 7.668556

    print(bn.get_line("STATI UNITI", "GALILEO FERRARIS"))

    print("--------- R4 ----------")
    path = bn.compute_itinerary("VITTORIO VENETO", "POLITECNICO")
    print(path)  # ... uno dei percorsi ....
    check_path(bn, path, "VITTORIO VENETO", "POLITECNICO")    # PATH OK


if __name__ == "__main__":
    main()
