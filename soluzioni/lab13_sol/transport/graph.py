import abc
from abc import ABC
from typing import Any, Set, List


class Graph(ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add_node(self, value: Any) -> int:
        pass

    @abc.abstractmethod
    def add_edge(self, value: Any, from_id: int, to_id: int) -> None:
        pass

    @abc.abstractmethod
    def get_node(self, node_id: int) -> Any:
        pass

    @abc.abstractmethod
    def get_edge(self, from_id: int, to_id: int) -> Any:
        pass

    @abc.abstractmethod
    def is_connected(self, from_id: int, to_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_parents(self, node_id: int) -> Set[int]:
        pass

    @abc.abstractmethod
    def get_children(self, node_id: int) -> Set[int]:
        pass

    @abc.abstractmethod
    def find_path(self, from_id: int, to_id: int) -> List[int]:
        pass


class Edge:
    def __init__(self, node, value):
        self._node = node
        self._value = value

    @property
    def node(self):
        return self._node

    @property
    def value(self):
        return self._value


class Node:
    def __init__(self, value):
        self._value = value
        self._edges = {}

    @property
    def edges(self):
        return self._edges

    @property
    def value(self):
        return self._value

    def add_edge(self, node_id, edge):
        self._edges[node_id] = edge

    def remove_edge(self, to_id):
        del self._edges[to_id]


class AdjacencyGraph(Graph):

    def __init__(self):
        super().__init__()
        self._nodes = {}

    def add_node(self, value: Any) -> int:
        node_id = len(self._nodes)
        self._nodes[node_id] = Node(value)
        return node_id

    def add_edge(self, value: Any, from_id: int, to_id: int) -> None:
        edge = Edge(self._nodes[to_id], value)
        self._nodes[from_id].add_edge(to_id, edge)

    def get_node(self, node_id: int) -> Any:
        return self._nodes[node_id].value

    def get_edge(self, from_id: int, to_id: int) -> Any:
        return self._nodes[from_id].edges[to_id].value

    def is_connected(self, from_id: int, to_id: int) -> bool:
        return to_id in self._nodes[from_id].edges

    def get_parents(self, node_id: int) -> Set[int]:
        parents = set()
        for n_id, node in self._nodes.items():
            if node_id in node.edges:
                parents.add(n_id)
        return parents

    def get_children(self, node_id: int) -> Set[int]:
        return set(self._nodes[node_id].edges.keys())

    def find_path(self, from_id: int, to_id: int) -> List[int]:
        path_ids = [from_id]
        if from_id != to_id:
            visited = {from_id}
            start_node = self._nodes[from_id]
            if not self._depth_first(start_node, to_id, visited, path_ids):
                path_ids.pop()
        return path_ids

    def _depth_first(self, current_node, target_node_id, visited, path_ids):
        # scorro tutti nodi collegati
        for node_id, edge in current_node.edges.items():
            # controllo se è da visitare
            if node_id not in visited:
                # aggiungo nodo al percorso
                path_ids.append(node_id)
                # aggiungo nodo al set dei visitati
                visited.add(node_id)
                # se è il nodo di arrivo termino ricorsione ritornando True
                if node_id == target_node_id:
                    return True
                # se ho trovato un percorso non proseguo e segnalo alla funzione chiamante
                if self._depth_first(edge.node, target_node_id, visited, path_ids):
                    return True
                # rimuovo nodo esplorato dalla lista (non è il percorso giusto)
                path_ids.pop()
        # segnalo alla funzione chiamante che non ho trovato un percorso
        return False

    def __len__(self) -> int:
        return len(self._nodes)


class GraphCreator:
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def get_empty_graph() -> Graph:
        return AdjacencyGraph()


