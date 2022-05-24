from hydraulics.elements import Element, Source
from typing import List


class HSystem:
    def __init__(self) -> None:
        self._elements = []

    def add_element(self, elm: Element) -> None:
        self._elements.append(elm)

    def get_elements(self) -> List[Element]:
        return self._elements

    def simulate(self) -> List[str]:
        sim_list = []
        to_simulate = []
        for elm in self._elements:
            if isinstance(elm, Source):
                to_simulate += elm.simulate(None, sim_list)
        while to_simulate:
            #print(to_simulate)
            elm, inflow = to_simulate[-1]
            to_simulate = to_simulate[:-1]
            to_simulate += elm.simulate(inflow, sim_list)

        return sim_list



