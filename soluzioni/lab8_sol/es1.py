class Room:
    def __init__(self, square_meters, n_windows, n_outlets):
        self._square_meters = square_meters
        self._n_windows = n_windows
        self._n_outlets = n_outlets

    def get_square_meters(self):
        return self._square_meters

    def get_n_windows(self):
        return self._n_windows

    def get_n_outlets(self):
        return self._n_outlets


class BathRoom(Room):
    def __init__(self, square_meters, n_windows, n_outlets, n_sinks, shower=True, tub=False, bidet=False):
        # chiamo costruttore classe padre e passo parametri
        super().__init__(square_meters, n_windows, n_outlets)
        self._n_sinks = n_sinks
        self._shower = shower
        self._tub = tub
        self._bidet = bidet

    def get_n_sinks(self):
        return self._n_sinks

    def has_shower(self):
        return self._shower

    def has_tub(self):
        return self._tub

    def has_bidet(self):
        return self._bidet


def main():
    # questo esempio mostra come classe figlio eredita metodo classe padre
    r1 = Room(square_meters=15, n_windows=2, n_outlets=5)
    r2 = BathRoom(square_meters=8, n_windows=1, n_outlets=3, n_sinks=2, shower=False, tub=True, bidet=True)

    print("Room square meters: {}".format(r1.get_square_meters()))
    print("BathRoom square meters: {}".format(r2.get_square_meters()))

    print("Room windows: {}".format(r1.get_n_windows()))
    print("BathRoom windows: {}".format(r2.get_n_windows()))

    print("Room outlets: {}".format(r1.get_n_outlets()))
    print("BathRoom outlets: {}".format(r2.get_n_outlets()))

    print("BathRoom sinks: {}".format(r2.get_n_sinks()))
    print("BathRoom shower: {}".format(r2.has_shower()))
    print("BathRoom tub: {}".format(r2.has_tub()))
    print("BathRoom bidet: {}".format(r2.has_bidet()))

    print("r2 is instance of Room: {}".format(isinstance(r2, Room)))
    print("r1 is instance of BathRoom: {}".format(isinstance(r1, BathRoom)))
    print("r2 is instance of BathRoom: {}".format(isinstance(r2, BathRoom)))


if __name__ == "__main__":
    main()
