import abc
from typing import List, Optional
from abc import ABC


class Element(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        # dizionario che mappa uscita all'elemento collegato
        # elemento generico ha una sola uscita (inizializzata non collegata)
        self._next = {0: None}

    def get_name(self) -> str:
        return self._name

    def connect(self, elm: "Element") -> None:
        # collego elemento all'uscita salvandone il riferimento nel dizionario
        self._next[0] = elm

    def get_output(self) -> Optional["Element"]:
        # restituisco elemento collegato all'uscita
        return self._next[0]

    # metodo astratto per simulare elemento (ogni figlio lo implementerà diversamente)
    # flow_in è il flusso in ingresso fornito dall'elemento precedente
    # info_list è la lista contente le stringhe di simulazione, a cui ogni elemento aggiungerà la propria
    @abc.abstractmethod
    def simulate(self, flow_in: float, info_list: List[str]) -> None:
        pass

    # funzione che restituisce stringa di simulazione dati flussi in ingresso e in uscita
    def _info_string(self, flow_in: float, *flow_outs: float) -> str:
        str_out = " ".join(["{:.3f}".format(flow_out) for flow_out in flow_outs])
        return "{} {} {:.3f} {}".format(type(self).__name__, self.get_name(), flow_in, str_out)


class Source(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        # flusso in uscita sorgente
        self._flow = 0

    def set_flow(self, flow: float) -> None:
        # setto flusso in uscita sorgente per simulazione
        self._flow = flow

    # simulazione sorgente
    def simulate(self, flow_in: float, info_list: List[str]) -> None:
        # creo stringa simulazione e la aggiungo alla lista
        # flusso in ingresso pari a zero e in uscita pari a quello settato
        info_list.append(self._info_string(0, self._flow))
        # ottengo elemento connesso all'uscita
        next_elm = self.get_output()
        # lo simulo fornendo come flusso in ingresso l'uscita della sorgente
        if next_elm is not None:
            next_elm.simulate(self._flow, info_list)


class Tap(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        # stato rubinetto (chiuso/aperto)
        self._open = False

    def set_status(self, to_open: bool = True) -> None:
        # setto stato rubinetto per simulazione
        self._open = to_open

    # simulo rubinetto
    def simulate(self, flow_in: float, info_list: List[str]) -> None:
        # flusso in uscita pari e quello in ingresso se aperto, altrimenti zero
        flow_out = flow_in if self._open else 0
        # creo stringa simulazione e la aggiungo alla lista
        info_list.append(self._info_string(flow_in, flow_out))
        # ottengo elemento connesso all'uscita
        next_elm = self.get_output()
        if next_elm is not None:
            # lo simulo fornendo come flusso in ingresso l'uscita del rubinetto
            next_elm.simulate(flow_out, info_list)


class Sink(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    # override per permettere connessione
    def connect(self, elm: "Element") -> None:
        pass

    # simulo scarico
    def simulate(self, flow_in: float, info_list: List[str]) -> None:
        # creo stringa simulazione e la aggiungo alla lista
        # flusso in uscita nullo
        info_list.append(self._info_string(flow_in, 0))
        # non ci sono uscite quindi non continuo simulazione per questo ramo (condizione di terminazione)


class Split(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._next[1] = None

    def connect_at(self, elm: Element, pos: int) -> None:
        # collego elemento all'uscita pos salvandone il riferimento nel dizionario
        self._next[pos] = elm

    def get_outputs(self) -> List[Optional[Element]]:
        # restituisco elementi collegati alle due uscite
        return [self._next[0], self._next[1]]

    # simulo split a T
    def simulate(self, flow_in: float, info_list: List[str]) -> None:
        # creo stringa simulazione e la aggiungo alla lista
        # flusso in ingresso diviso in 2 sulle due uscite
        info_list.append(self._info_string(flow_in, flow_in/2, flow_in/2))
        # simulo elementi connessi alle uscite
        for next_elm in self.get_outputs():
            if next_elm is not None:
                next_elm.simulate(flow_in/2, info_list)









