class TreeNode:
    def __init__(self, key):
        # valore (chiave) del nodo
        self._key = key
        # nodo a sinistra
        self._left = None
        # nodo a destra
        self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def key(self):
        return self._key


class BinaryTree:
    def __init__(self):
        self._root = None
        self._num_nodes = 0

    def add(self, key):
        # creo nodo da aggiungere
        new_node = TreeNode(key)
        # se albero è vuoto il nodo diventa la radice
        if self._root is None:
            self._root = new_node
        else:
            # parto dalla radice e scendo finché non trovo posto libero
            added = False
            current_node = self._root
            while not added:
                # se valore minore da aggiungere è minore di quello nel nodo considerato vado a sinistra
                if key <= current_node.key:
                    if current_node.left is None:
                        # se il posto è libero aggiungo nodo
                        current_node.left = new_node
                        added = True
                    else:
                        # altrimenti scendo ad analizzare il prossimo nodo
                        current_node = current_node.left
                # altrimenti vado a destra (e faccio cose equivalenti)
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        added = True
                    else:
                        current_node = current_node.right
        self._num_nodes += 1
        return self

    def min(self):
        # parto dalla radice
        minimum = None
        current = self._root
        # scendo andando sempre a sinistra finché non ci sono più nodi
        while current is not None:
            # aggiorno il minimo trovato finora
            minimum = current.key
            current = current.left
        return minimum

    @staticmethod
    def depth_first(current, key_list):
        # se manca il nodo termino l'esplorazione
        if current is None:
            return
        # esploro a sinistra (valori minori)
        BinaryTree.depth_first(current.left, key_list)
        # aggiunto nodo attuale alla lista
        key_list.append(current.key)
        # esploro a destra (valori maggiori)
        BinaryTree.depth_first(current.right, key_list)

    def __repr__(self):
        # inizializzo lista elementi ordinati
        key_list = []
        # esploro albero partendo dalla radice
        BinaryTree.depth_first(self._root, key_list)
        # creo rappresentazione in stringa lista elementi
        key_list = [str(key) for key in key_list]
        return "[{}]".format(",".join(key_list))

    def __len__(self):
        return self._num_nodes


def main():
    # creo albero vuoto e stamp
    b = BinaryTree()
    print(b)
    # aggiungo elementi all'albero
    keys = [3, 10, 7, 1, 2, 3, 3, 9, 3, 4, 5, 4, 3, 2, 5]
    for key in keys:
        b.add(key)
    # stampo albero in modo ordinato
    print(b)
    # trovo il minimo
    print(b.min())


if __name__ == "__main__":
    main()



