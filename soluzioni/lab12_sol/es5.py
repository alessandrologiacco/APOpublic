# nodo della coda
class ListNode:
    def __init__(self, val):
        # valore elemento coda
        self._val = val
        # riferimento al prossimo nodo
        self._next_node = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node


class Queue:
    def __init__(self):
        # elemento fantoccio in testa (per semplicità)
        self._head = ListNode(None)
        # riferimento elemento in coda
        self._tail = self._head
        # lunghezza coda
        self._length = 0

    def append(self, val):
        # creo nodo per nuovo elemento
        new_node = ListNode(val)
        # collego nodo in coda al nuovo elemento
        self._tail.next_node = new_node
        # aggiorno nodo in coda
        self._tail = new_node
        # aggiorno lunghezza
        self._length += 1

    def pop(self):
        # controllo che coda non sia vuota
        if self._head.next_node is None:
            raise IndexError("Queue is empty")
        # ottengo nodo da rimuovere
        node = self._head.next_node
        # collego la testa all'elemento successivo di quello rimosso
        self._head.next_node = node.next_node
        # se nodo rimosso in coda aggiorno riferimento
        if node == self._tail:
            self._tail = self._head
        # aggiorno lunghezza coda
        self._length -= 1
        # ritorno valore del nodo rimosso
        return node.val

    def __getitem__(self, pos):
        # verifico che posizione sia valida
        if pos >= self._length:
            raise IndexError("Queue index out of range")
        # scorro coda fino al nodo cercato, complessità O(n)
        node = self._head
        for i in range(pos+1):
            node = node.next_node
        # ritorno valore nodo
        return node.val

    def __len__(self):
        return self._length

    def __repr__(self):
        # scorro coda e salvo valori
        str_repr = "["
        node = self._head
        for i in range(self._length):
            node = node.next_node
            if i != 0:
                str_repr += ", "
            str_repr += str(node.val)
        str_repr += "]"
        return str_repr


def main():
    # creo coda vuota
    q = Queue()
    print("Coda attuale: {}".format(q))

    # aggiungo elementi alla coda
    q.append("ciao")
    q.append("come")
    q.append("va")
    print("Coda attuale: {}".format(q))
    print("Lunghezza: {}".format(len(q)))

    # accedo elementi
    print("Elemento in posizione 1: {}".format(q[1]))

    # rimuovo elementi
    elm = q.pop()
    print("Elemento rimosso: {}".format(elm))
    print("Coda attuale: {}".format(q))
    print("Lunghezza: {}".format(len(q)))

    # eccezioni:
    try:
        print(q[3])
    except IndexError as e:
        print("Errore: {}".format(e))

    # rimuovo tutti elementi
    q.pop()
    q.pop()
    print("Coda attuale: {}".format(q))

    # eccezioni:
    try:
        q.pop()
    except IndexError as e:
        print("Errore: {}".format(e))


if __name__ == "__main__":
    main()
