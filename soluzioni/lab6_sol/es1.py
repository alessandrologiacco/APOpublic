class ScoreLedger:

    def __init__(self):
        self._tot_buckets = 0
        self._teams = []
    
    def add_match(self, team, num_buckets):
        self._teams.append(team)
        self._tot_buckets += num_buckets

    def get_average(self):
        return self._tot_buckets/len(self._teams)

    def get_teams(self):
        return self._teams

    def get_summary(self):
        return "Num items: {}\nAverage price: {}".format(len(self._teams), self.get_average())


def main():
    s = ScoreLedger()
    s.add_match("Trieste", 32)
    s.add_match("Milano", 37)
    print(s.get_average())
    print(s.get_teams())
    print(s.get_summary())


if __name__ == "__main__":
    main()
