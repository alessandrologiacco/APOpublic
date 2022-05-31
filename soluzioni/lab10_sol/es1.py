import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Triangle(Shape):
    def __init__(self, name: str, base, *edges) -> None:
        super().__init__(name)
        # in base ai parametri forniti creo la lista di lati
        if not edges:
            self._edges = [base]*3
        elif len(edges) == 1:
            self._edges = [base, edges[0], edges[0]]
        else:
            self._edges = [base, edges[0], edges[1]]

    def get_area(self) -> float:
        # calcolo area con formula di Erone
        p = sum(self._edges)/2
        return math.sqrt(p*(p-self._edges[0])*(p-self._edges[1])*(p-self._edges[2]))

    def get_perimeter(self) -> float:
        return sum(self._edges)


class Square(Shape):
    def __init__(self, name: str, edge) -> None:
        super().__init__(name)
        self._edge = edge

    def get_area(self) -> float:
        return self._edge**2

    def get_perimeter(self) -> float:
        return self._edge*4


def main():
    # controllo che classe astratta non sia istanziabile
    try:
        s = Shape()
    except TypeError as e:
        print("Error: {}".format(e))

    # creo triangolo e testo override
    t = Triangle("Triangolo Scaleno", 2, 3, 4)
    print(t.get_name())
    print("\t - Perimetro: {:.3f}".format(t.get_perimeter()))
    print("\t - Area: {:.3f}".format(t.get_area()))

    # creo triangolo e testo override
    t = Triangle("Triangolo Isoscele", 2, 3)
    print(t.get_name())
    print("\t - Perimetro: {:.3f}".format(t.get_perimeter()))
    print("\t - Area: {:.3f}".format(t.get_area()))

    # creo triangolo e testo override
    t = Triangle("Triangolo Equilatero", 3)
    print(t.get_name())
    print("\t - Perimetro: {:.3f}".format(t.get_perimeter()))
    print("\t - Area: {:.3f}".format(t.get_area()))

    # creo rettangolo e testo override
    s = Square("Un Quadrato", 5)
    print(s.get_name())
    print("\t - Perimetro: {:.3f}".format(s.get_perimeter()))
    print("\t - Area: {:.3f}".format(s.get_area()))


if __name__ == "__main__":
    main()
