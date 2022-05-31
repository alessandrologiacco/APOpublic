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


# implementare grafo


class GraphCreator:
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def get_empty_graph() -> Graph:
        # restituire nuova instanza grafo
        pass
