from typing import List, Optional
from abc import ABC


class Element(ABC):
    def __init__(self, name: str) -> None:
        pass

    def get_name(self) -> str:
        pass

    def connect(self, elm: "Element") -> None:
        pass

    def get_output(self) -> Optional["Element"]:
        pass


class Source(Element):
    def __init__(self, name: str) -> None:
        pass

    def set_flow(self, flow: float) -> None:
        pass


class Tap(Element):
    def __init__(self, name: str) -> None:
        pass

    def set_status(self, to_open: bool = True) -> None:
        pass


class Sink(Element):
    def __init__(self, name: str) -> None:
        pass


class Split(Element):
    def __init__(self, name: str) -> None:
        pass

    def connect_at(self, elm: Element, pos: int) -> None:
        pass

    def get_outputs(self) -> List[Optional[Element]]:
        pass
