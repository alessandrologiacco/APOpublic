from typing import List
from transport.graph import AdjacencyGraph


class Stop:
    def __init__(self, name, latitude, longitude):
        self._name = name
        self._latitude = latitude
        self._longitude = longitude

    @property
    def name(self):
        return self._name

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude


class BusNetwork:
    def __init__(self) -> None:
        self._network = AdjacencyGraph()
        self._name_to_id = {}

    def load_stops(self, f_name: str) -> None:
        with open(f_name, "r") as f:
            for line in f:
                line_lst = line.strip().split(",")
                new_stop = Stop(name=line_lst[0], latitude=float(line_lst[1]), longitude=float(line_lst[2]))
                self._name_to_id[new_stop.name] = self._network.add_node(new_stop)

    def load_connections(self, f_name: str) -> None:
        with open(f_name, "r") as f:
            for line in f:
                line_lst = line.strip().split(",")
                bus_number = line_lst[0]
                start_node_id = self._name_to_id[line_lst[1]]
                end_node_id = self._name_to_id[line_lst[2]]
                self._network.add_edge(bus_number, start_node_id, end_node_id)

    def get_stop(self, stop_name: str) -> Stop:
        return self._network.get_node(self._name_to_id[stop_name])

    def get_line(self, from_stop_name: str, to_stop_name: str) -> str:
        if not self._network.is_connected(self._name_to_id[from_stop_name], self._name_to_id[to_stop_name]):
            return None
        return self._network.get_edge(self._name_to_id[from_stop_name], self._name_to_id[to_stop_name])

    def compute_itinerary(self, from_stop_name: str, to_stop_name: str) -> List[str]:
        path_descr = []
        path_ids = self._network.find_path(self._name_to_id[from_stop_name], self._name_to_id[to_stop_name])
        for i in range(len(path_ids)-1):
            current_stop = self._network.get_node(path_ids[i])
            bus_number = self._network.get_edge(path_ids[i], path_ids[i+1])
            path_descr.append("{} -> {}".format(current_stop.name, bus_number))
        last_stop = self._network.get_node(path_ids[-1])
        path_descr.append("{} -> END".format(last_stop.name))
        return path_descr




