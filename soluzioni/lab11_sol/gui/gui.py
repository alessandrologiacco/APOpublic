from tkinter import *
from tkinter import ttk, messagebox
from diet.food import Food


# classe View eredita da TK
class View(Tk):
    def __init__(self, model, controller):
        super().__init__()
        # salvo model e controller
        self._model = model
        self._controller = controller

        # creo finestra
        self.title("Diet")
        self.minsize(500, 300)

        # configuro grid
        for i in range(7):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # creo StringVar per campi di input
        self._name = StringVar()
        self._cals = StringVar()
        self._proteins = StringVar()
        self._carbs = StringVar()
        self._fat = StringVar()

        # creo labels per campi in di input
        self._name_label = ttk.Label(self, text="Name: ")
        self._cals_label = ttk.Label(self, text="Calories: ")
        self._proteins_label = ttk.Label(self, text="Proteins: ")
        self._carbs_label = ttk.Label(self, text="Carbs: ")
        self._fat_label = ttk.Label(self, text="Fat: ")

        # creo campi di input per materia prima
        self._name_entry = ttk.Entry(self, textvariable=self._name)
        self._cals_entry = ttk.Entry(self, textvariable=self._cals)
        self._proteins_entry = ttk.Entry(self, textvariable=self._proteins)
        self._carbs_entry = ttk.Entry(self, textvariable=self._carbs)
        self._fat_entry = ttk.Entry(self, textvariable=self._fat)

        # posiziono labels
        self._name_label.grid(column=0, row=0, sticky=(N, S, W, E))
        self._cals_label.grid(column=0, row=1, sticky=(N, S, W, E))
        self._proteins_label.grid(column=0, row=2, sticky=(N, S, W, E))
        self._carbs_label.grid(column=0, row=3, sticky=(N, S, W, E))
        self._fat_label.grid(column=0, row=4, sticky=(N, S, W, E))

        # posiziono campi di input
        self._name_entry.grid(column=1, row=0, sticky=(N, S, W, E))
        self._cals_entry.grid(column=1, row=1, sticky=(N, S, W, E))
        self._proteins_entry.grid(column=1, row=2, sticky=(N, S, W, E))
        self._carbs_entry.grid(column=1, row=3, sticky=(N, S, W, E))
        self._fat_entry.grid(column=1, row=4, sticky=(N, S, W, E))

        # aggiungo bottoni, callback evento è un metodo del controller
        self._b1 = ttk.Button(self, text="Add element", command=self._controller.add_raw_material)
        self._b2 = ttk.Button(self, text="Get elements", command=self._controller.get_raw_materials)
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
    def cals(self):
        return self._cals.get()

    @property
    def proteins(self):
        return self._proteins.get()

    @property
    def carbs(self):
        return self._carbs.get()

    @property
    def fat(self):
        return self._fat.get()


class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    # handler bottone per aggiunta raw material
    def add_raw_material(self):
        try:
            # modifico modello aggiungendo material prima
            self._model.define_raw_material(
                self._view.name,
                float(self._view.cals),
                float(self._view.proteins),
                float(self._view.carbs),
                float(self._view.fat)
            )
            # stampo messaggio conferma tramite view
            self._view.show_message_box(title="Done", message="Elemento aggiunto")
        except ValueError as e:
            # stampo messaggio errore tramite view (materia prima duplicata, campi non corretti)
            self._view.show_message_box(title="Insertion error", message=str(e))

    # handler bottone per richiesta materie prime
    def get_raw_materials(self):
        # accedo al modello per ottenere informazioni
        raw_materials = self._model.raw_materials
        # uso la view per visualizzarle
        msg_str = "\n".join([material.name for material in raw_materials])
        self._view.show_message_box(title="Raw materials", message=msg_str)


def main():
    # come modello uso la classe food
    m = Food()
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

