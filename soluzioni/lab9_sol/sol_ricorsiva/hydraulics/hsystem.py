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
        info_list = []
        # scorro elementi
        for elm in self._elements:
            # controllo se è una sorgente
            if isinstance(elm, Source):
                # inizio simulazione dalla sorgente
                # la sorgente simulerà l'elemento successivo e così via...
                # ogni elemento aggiungerà la sua stringa si simulazione alla info_list
                elm.simulate(flow_in=0, info_list=info_list)
        return info_list


