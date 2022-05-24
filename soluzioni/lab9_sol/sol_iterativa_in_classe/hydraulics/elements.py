from typing import List, Optional
from abc import ABC
import abc


class Element(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._next = {0: None}

    def get_name(self) -> str:
        return self._name

    def connect(self, elm: "Element") -> None:
        self._next[0] = elm

    def get_output(self) -> Optional["Element"]:
        return self._next[0]

    @abc.abstractmethod
    def simulate(self, inflow, sim_list):
        pass


class Source(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._flow = 0

    def set_flow(self, flow: float) -> None:
        self._flow = flow

    def simulate(self, inflow, sim_list):
        sim_list.append("Source {} {:.3f} {:.3f}".format(self._name, 0, self._flow))
        return [(self._next[0], self._flow)]


class Tap(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._open = False

    def set_status(self, to_open: bool = True) -> None:
        self._open = to_open

    def simulate(self, inflow, sim_list):
        if self._open:
            outflow = inflow
        else:
            outflow = 0
        sim_list.append("Tap {} {:.3f} {:.3f}".format(self._name, inflow, outflow))
        return [(self._next[0], outflow)]


class Sink(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def connect(self, elm: "Element") -> None:
        pass

    def simulate(self, inflow, sim_list):
        sim_list.append("Sink {} {:.3f} {:.3f}".format(self._name, inflow, 0))
        return []


class Split(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._next[1] = None

    def connect_at(self, elm: Element, pos: int) -> None:
        self._next[pos] = elm

    def get_outputs(self) -> List[Optional[Element]]:
        return [self._next[0], self._next[1]]

    def simulate(self, inflow, sim_list):
        sim_list.append("Split {} {:.3f} {:.3f} {:.3f}".format(self._name, inflow, inflow/2, inflow/2))
        return [(self._next[0], inflow/2), (self._next[1], inflow/2)]
