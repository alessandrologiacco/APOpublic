def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


def binomial_coefficient(n, k):
    return int(factorial(n)/factorial(k)/factorial(n-k))


def ask_input():
    a = int(input("Insert a: "))
    b = int(input("Insert b: "))
    return a, b


def main():
    a, b = ask_input()
    while a != -1 or b != -1:
        if a >= b:
            res = binomial_coefficient(a, b)
        else:
            res = binomial_coefficient(b, a)
        print("Binomial coefficient: {}".format(res))
        a, b = ask_input()
    print("exiting...")


if __name__ == "__main__":
    main()
