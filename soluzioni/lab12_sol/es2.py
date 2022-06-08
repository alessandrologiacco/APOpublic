from typing import List


def print_binary(n: int, num_list: List[str] = []):
    # controllo se ho altre cifre da aggiungere
    if n > 0:
        # aggiungo "0" in posizione n
        num_list.append("0")
        # aggiungo cifre mancanti
        print_binary(n - 1, num_list)
        # rimuovo "0" e aggiunto "1" in posizione n
        num_list.pop()
        num_list.append("1")
        # aggiungo cifre mancanti
        print_binary(n - 1, num_list)
        # rimuovo "1"
        num_list.pop()
    else:
        # stampo quanto ho tutte le cifre
        print("".join(num_list))
    return


def main():
    print_binary(5)


if __name__ == "__main__":
    main()
    