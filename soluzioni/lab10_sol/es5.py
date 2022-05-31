import time


def repeat_ten_times(f):
    def decorated(*argv, **args):
        for i in range(10):
            f(*argv, **args)
    return decorated


def time_execution(f):
    def decorated(*argv, **args):
        start = time.perf_counter_ns()
        f(*argv, **args)
        print("{} ns".format(time.perf_counter_ns() - start))
    return decorated


class GreetClass:
    def __init__(self, name):
        self._name = name

    @repeat_ten_times
    @time_execution
    def say_hello(self):
        print("Hello {}!".format(self._name))

    @time_execution
    @repeat_ten_times
    def say_good(self, time_of_day):
        print("Good {} {}!".format(time_of_day, self._name))


def main():
    g = GreetClass("Pietro")
    g.say_hello()
    g.say_good("morning")


if __name__ == "__main__":
    main()






