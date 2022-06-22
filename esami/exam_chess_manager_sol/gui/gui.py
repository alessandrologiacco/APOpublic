from tkinter import *
from tkinter import ttk, messagebox
from chess.board import Board, Piece, ChessException


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
        for i in range(4):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # creo StringVar per campi di input
        self._x_pos = StringVar()
        self._y_pos = StringVar()

        # creo labels per campi in di input
        self._x_pos_label = ttk.Label(self, text="x_pos: ")
        self._y_pos_label = ttk.Label(self, text="y_pos: ")

        # creo campi di input per posizioni pezzo
        self._x_pos_entry = ttk.Entry(self, textvariable=self._x_pos)
        self._y_pos_entry = ttk.Entry(self, textvariable=self._y_pos)

        # posiziono labels
        self._x_pos_label.grid(column=0, row=0, sticky=(N, S, W, E))
        self._y_pos_label.grid(column=0, row=1, sticky=(N, S, W, E))

        # posiziono campi di input
        self._x_pos_entry.grid(column=1, row=0, sticky=(N, S, W, E))
        self._y_pos_entry.grid(column=1, row=1, sticky=(N, S, W, E))

        # aggiungo bottoni, callback evento è un metodo del controller
        self._b1 = ttk.Button(self, text="Get", command=self._controller.get_piece)
        self._b2 = ttk.Button(self, text="Remove", command=self._controller.remove_piece)
        self._b1.grid(column=0, row=2, columnspan=2, sticky=(N, S, W, E))
        self._b2.grid(column=0, row=3, columnspan=2, sticky=(N, S, W, E))

    @staticmethod
    def show_message_box(title, message):
        messagebox.showinfo(title=title, message=message)

    # proprietà della view
    @property
    def x_pos(self):
        return self._x_pos.get()

    @property
    def y_pos(self):
        return self._y_pos.get()


class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    # handler bottone per rimozione pezzo
    def remove_piece(self):
        try:
            # modifico modello rimuovendo pezzo
            self._model.add_piece(None, int(self._view.x_pos), int(self._view.y_pos))
            # stampo messaggio conferma tramite view
            self._view.show_message_box(title="Done", message="Piece Removed")
        except ChessException as e:
            # mostro messaggio di eccezione
            self._view.show_message_box(title="Error", message=str(e))

    # handler bottone per ottenere pezzo
    def get_piece(self):
        try:
            # modifico modello aggiungendo carta
            piece = self._model.get_piece(int(self._view.x_pos), int(self._view.y_pos))
            # stampo messaggio con pezzo in posizione fornita
            self._view.show_message_box(title="Done", message=piece if piece else "Piece non present")
        except ChessException as e:
            # mostro messaggio di eccezione
            self._view.show_message_box(title="Error", message=str(e))


def main():
    # come modello uso la classe board
    m = Board("board_gui", 5)

    # popolo la board on pezzi
    m.add_piece(Piece.ROOK, 0, 0)
    m.add_piece(Piece.QUEEN, 2, 3)
    m.add_piece(Piece.KING, 3, 2)
    m.add_piece(Piece.PAWN, 1, 4)
    m.add_piece(Piece.BISHOP, 2, 4)
    m.add_piece(Piece.KNIGHT, 1, 1)

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

