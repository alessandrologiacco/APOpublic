class Ticket:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_queue_pos(self):
        return self._number

    def __repr__(self):
        return "{} {}".format(self._name, self._number)

    def __lt__(self, other):
        return self.get_queue_pos() < other.get_queue_pos()


class PriorityTicket(Ticket):
    def __init__(self, name, number, priority):
        super().__init__(name, number)
        self._priority = priority

    def get_queue_pos(self):
        return self._number - self._priority * 10

    def __repr__(self):
        return "{} p{}".format(super().__repr__(), self._priority)


def main():
    t1 = Ticket("Mario Rossi", 37)
    t2 = Ticket("Enrico Bianchi", 25)
    t3 = PriorityTicket("Luca Gialli", 43, 2)

    # coda non ordinata
    queue = [t1, t2, t3]
    print(queue)

    # coda ordinata usando __lt__() per confrontare elementi
    queue.sort()
    print(queue)

    # stessa cosa con sorted()
    queue = [t1, t2, t3]
    queue = sorted(queue)
    print(queue)


if __name__ == "__main__":
    main()




