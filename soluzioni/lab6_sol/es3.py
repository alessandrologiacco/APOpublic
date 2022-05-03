class Team:

    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._players = []

    def get_name(self):
        return self._name

    def get_city(self):
        return self._city

    def add_player(self, player):
        self._players.append(player)        

    def get_players(self):
        return self._players


class Player:
    
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        self._team = None

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_age(self):
        return self._age

    def set_team(self, team):
        self._team = team
    
    def get_team(self):
        return self._team


if __name__ == "__main__":
    # creo giocatori e squadre
    t1 = Team("Juventus", "Torino")
    p1 = Player("Giorgio", "Chiellini", 37)
    p2 = Player("Juan", "Cuadrado", 33)

    # getters team
    print("---- Squadra ----")
    print(t1.get_city())
    print(t1.get_name())
    print(t1.get_players())

    # getters player
    print("---- Giocatori ----")
    print(p1.get_name())
    print(p1.get_surname())
    print(p2.get_age())
    print(p2.get_team())

    # creo associazione
    t1.add_player(p1)
    t1.add_player(p2)
    p1.set_team(t1)
    p2.set_team(t1)

    # verifico associazione squadra --> giocatori
    print("---- Giocatori della squadra ----")
    for p in t1.get_players():
        print(p.get_name(), p.get_surname())

    # verifico associazione giocatori --> squadra
    print("--- Squadre dei giocatori ---")
    print(p1.get_team().get_name())
    print(p2.get_team().get_name())


