from es3 import SortableCouple


class WeightedSorter:
    def __init__(self, weight):
        self._weight = weight

    def __call__(self, elm):
        return elm.a * self._weight + elm.b * (1 - self._weight)


# closure factory
def create_sort_function(weight):
    # closure
    def weighted_sort(elm):
        return elm.a * weight + elm.b * (1 - weight)
    return weighted_sort


def main():
    a = SortableCouple(2, 2)
    b = SortableCouple(1, 3)
    c = SortableCouple(3, 1)

    couple_list = [a, b, c]

    sorter_cls = WeightedSorter(weight=0.2)
    sorter_fn = create_sort_function(weight=0.8)

    couple_list.sort(key=sorter_cls)
    print(couple_list)

    couple_list.sort(key=sorter_fn)
    print(couple_list)


if __name__ == "__main__":
    main()
