from tkinter import *
from tkinter import ttk, messagebox
from games.card_game import Card


# classe View eredita da TK
class View(Tk):
    def __init__(self, model, controller):
        super().__init__()
        # salvo model e controller
        self._model = model
        self._controller = controller

        # creo finestra
        self.title("Card Game")
        self.minsize(500, 300)

        # configuro grid
        for i in range(7):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # creo StringVar per campi di input
        self._name = StringVar()
        self._attack = StringVar()
        self._life_points = StringVar()
        self._mana_cost = StringVar()

        # creo labels per campi in di input
        self._name_label = ttk.Label(self, text="Name: ")
        self._attack_label = ttk.Label(self, text="Attack: ")
        self._life_points_label = ttk.Label(self, text="Life points: ")
        self._mana_cost_label = ttk.Label(self, text="Mana cost: ")

        # creo campi di input per carta
        self._name_entry = ttk.Entry(self, textvariable=self._name)
        self._attack_entry = ttk.Entry(self, textvariable=self._attack)
        self._life_points_entry = ttk.Entry(self, textvariable=self._life_points)
        self._mana_cost_entry = ttk.Entry(self, textvariable=self._mana_cost)

        # posiziono labels
        self._name_label.grid(column=0, row=0, sticky=(N, S, W, E))
        self._attack_label.grid(column=0, row=1, sticky=(N, S, W, E))
        self._life_points_label.grid(column=0, row=2, sticky=(N, S, W, E))
        self._mana_cost_label.grid(column=0, row=3, sticky=(N, S, W, E))

        # posiziono campi di input
        self._name_entry.grid(column=1, row=0, sticky=(N, S, W, E))
        self._attack_entry.grid(column=1, row=1, sticky=(N, S, W, E))
        self._life_points_entry.grid(column=1, row=2, sticky=(N, S, W, E))
        self._mana_cost_entry.grid(column=1, row=3, sticky=(N, S, W, E))

        # aggiungo bottoni, callback evento è un metodo del controller
        self._b1 = ttk.Button(self, text="Add element", command=self._controller.add_card)
        self._b2 = ttk.Button(self, text="Get elements", command=self._controller.get_cards)
        self._b1.grid(column=0, row=5, columnspan=2, sticky=(N, S, W, E))
        self._b2.grid(column=0, row=6, columnspan=2, sticky=(N, S, W, E))

    @staticmethod
    def show_message_box(title, message):
        messagebox.showinfo(title=title, message=message)

    # proprietà della view
    @property
    def name(self):
        return self._name.get()

    @property
    def attack(self):
        return self._attack.get()

    @property
    def life_points(self):
        return self._life_points.get()

    @property
    def mana_cost(self):
        return self._mana_cost.get()


class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    # handler bottone per aggiunta carta
    def add_card(self):

        # modifico modello aggiungendo carta
        card = Card(
            self._view.name,
            int(self._view.attack),
            int(self._view.life_points),
            int(self._view.mana_cost)
        )
        self._model.append(card)
        # stampo messaggio conferma tramite view
        self._view.show_message_box(title="Done", message="Card added")

    # handler bottone per richiesta carte
    def get_cards(self):
        # uso la view per visualizzarle
        msg_str = "\n".join([str(card) for card in self._model])
        self._view.show_message_box(title="Cards", message=msg_str)


def main():
    # come modello uso una lista di carte
    m = []
    # creo controller e passo il modello
    c = Controller(model=m)
    # creo view e passo model e controller
    v = View(model=m, controller=c)
    # passo la view al controller
    c.set_view(v)

    # avvio l'event loop
    v.mainloop()


if __name__ == "__main__":
    main()

