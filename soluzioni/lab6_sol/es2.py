class IdentityCard:

    _new_card_id = 0

    def __init__(self, name, surname, issue_year = 2022):
        self._name = name
        self._surname = surname
        self._issue_year = issue_year
        self._birth_year = None
        self._card_id = IdentityCard._new_card_id
        IdentityCard._new_card_id += 1
    
    def get_card_id(self):
        return self._card_id

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_issue_year(self):
        return self._issue_year

    def set_birth_year(self, year):
        if year >= self._issue_year:
            year = self._issue_year
        self._birth_year = year

    def get_birth_year(self):
        return self._birth_year


if __name__ == "__main__":
    print("-----------")
    c1 = IdentityCard("Mario", "Rossi", 2016)
    c1.set_birth_year(1996)
    print("N. documento: {}".format(c1.get_card_id()))
    print("Nome: {}".format(c1.get_name()))
    print("Cognome: {}".format(c1.get_surname()))
    print("Anno di nascita: {}".format(c1.get_birth_year()))
    print("Anno di rilascio: {}".format(c1.get_issue_year()))

    print("-----------")
    c1 = IdentityCard("Enrico", "Bianchi", 2019)
    c1.set_birth_year(2020)
    print("N. documento: {}".format(c1.get_card_id()))
    print("Nome: {}".format(c1.get_name()))
    print("Cognome: {}".format(c1.get_surname()))
    print("Anno di nascita: {}".format(c1.get_birth_year()))
    print("Anno di rilascio: {}".format(c1.get_issue_year()))

