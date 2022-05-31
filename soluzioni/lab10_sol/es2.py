class Thermostat:
    def __init__(self, target_temp: float, fahrenheit: bool = False) -> None:
        self._target_temp = None
        self._fahrenheit = fahrenheit
        # uso setter per settare temperatura con controlli e conversione (uso celsius per salvarla)
        self.target_temp = target_temp

    @classmethod
    def from_thermostat(cls, other: "Thermostat") -> "Thermostat":
        return cls(other.target_temp, other.fahrenheit)

    @staticmethod
    def to_fahrenheit(temp: float) -> float:
        return temp * 1.8 + 32

    @staticmethod
    def to_celsius(temp: float) -> float:
        return (temp - 32)/1.8

    @property
    def target_temp(self) -> float:
        # converto valore to fahrenheit se necessario
        return self._target_temp if not self._fahrenheit else Thermostat.to_fahrenheit(self._target_temp)

        # --------- La forma contratta "if else" è equivalente a:
        # if not self._fahrenheit:
        #     return self._target_temp
        # return Thermostat.to_fahrenheit(self._target_temp)

    @target_temp.setter
    def target_temp(self, target_temp: float) -> None:
        # converto valore to celsius se fornito in fahrenheit
        target_temp = target_temp if not self._fahrenheit else Thermostat.to_celsius(target_temp)

        # --------- La forma contratta "if else" è equivalente a:
        # if not self._fahrenheit:
        #     target_temp = self._target_temp
        # else:
        #     target_temp = Thermostat.to_celsius(target_temp)

        if target_temp > 30:
            self._target_temp = 30
        else:
            self._target_temp = target_temp

    @property
    def fahrenheit(self) -> bool:
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit: bool) -> None:
        self._fahrenheit = fahrenheit


def main():
    # metodi statici
    print("0 Celsius in Fahrenheit: {:.3f}".format(Thermostat.to_fahrenheit(0)))
    print("0 Fahrenheit in Celsius: {:.3f}".format(Thermostat.to_celsius(0)))

    # metodo di classe (costruttore di copia)
    t1 = Thermostat(21.5, fahrenheit=False)
    t2 = Thermostat.from_thermostat(t1)
    print("Target temperature: {}".format(t2.target_temp))
    print("In Fahrenheit: {}".format(t2.fahrenheit))

    # cambio a fahrenheit
    t1.fahrenheit = True
    print("In Fahrenheit: {}".format(t1.fahrenheit))
    print("Target temperature: {} Fahrenheit".format(t1.target_temp))

    # setto temperatura in fahrenheit
    t1.target_temp = 32
    print("Target temperature: {} Fahrenheit".format(t1.target_temp))

    # setto temperatura in celsius sopra 30 Celsius
    t2.target_temp = 32
    print("Target temperature: {} Fahrenheit".format(t2.target_temp))


if __name__ == "__main__":
    main()

