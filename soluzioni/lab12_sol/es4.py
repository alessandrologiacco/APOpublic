def merge_sort(lst):
    # creo lista di appoggio
    w_lst = lst.copy()
    # ordino array con merge sort
    recursive_split_merge(lst, w_lst, 0, len(w_lst))


def recursive_split_merge(lst, w_lst, idx_start, idx_end):
    # se lista ha solo un elemento non faccio nulla
    if idx_end - idx_start < 2:
        return
    # trovo centro lista
    idx_middle = (idx_end - idx_start) // 2 + idx_start
    # ordino parte sinistra lista principale
    # scrivo risultato nella lista di appoggio
    recursive_split_merge(w_lst, lst, idx_start, idx_middle)
    # ordino parte destra lista principale
    # scrivo risultato nella lista di appoggio
    recursive_split_merge(w_lst, lst, idx_middle, idx_end)
    # unisco le metà ordinate nella lista di appoggio in quella principale
    merge(lst, w_lst, idx_start, idx_middle, idx_end)


def merge(lst, w_lst, idx_start, idx_middle, idx_end):
    # mi metto all'inizio delle due metà ordinate
    i = idx_start
    j = idx_middle
    # scorro posizioni lista principale in cui mettere valori ordinati
    for k in range(idx_start, idx_end):
        # prendo valore dalla prima metà se sono rimasti valori e se
        # - nella seconda metà non ci sono più valori
        # - oppure se valore della prima metà è più piccolo di quello nella seconda
        # mi sposto a destra nella prima metà
        if i < idx_middle and (j >= idx_end or w_lst[i] <= w_lst[j]):
            lst[k] = w_lst[i]
            i += 1
        # altrimenti prendo quello nella seconda
        # mi sposto a destra nella prima metà
        else:
            lst[k] = w_lst[j]
            j += 1


def main():
    my_list = [3, 10, 7, 1, 2, 3, 3, 9, 3, 4, 5, 4, 3, 2, 5]
    merge_sort(my_list)
    print(my_list)


if __name__ == "__main__":
    main()
