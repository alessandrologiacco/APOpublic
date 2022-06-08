def recursive_sum(n: int):
    if n > 1:
        return n + recursive_sum(n-1)
    return 1


def main():
    print("Somma ricorsiva primi 10 numeri: {}".format(recursive_sum(10)))


if __name__ == "__main__":
    main()
