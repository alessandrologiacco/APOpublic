from tkinter import *
from tkinter import ttk

# set to change starting player (-1 OR 1)
STARTING_PLAYER = 1


# disegnare celle tris nel canvas e inizializzare tabella
#  O -> cella vuota
#  1 -> simbolo X
# -1 -> simbolo O
def reset_table(canvas):
    canvas.delete("all")
    table = []
    for i in range(3):
        row = []
        for j in range(3):
            # calcolo coordinate vertici cella e la disegno
            pos_x = edge_padding + i * (cell_size + padding)
            pos_y = edge_padding + j * (cell_size + padding)
            cell = canvas.create_rectangle((pos_x, pos_y, pos_x + cell_size, pos_y + cell_size), fill="white", outline="red")
            # registro callback (lambda function) per l'evento click sulla cella
            # lambda usa la funzione button pressed (3 parametri)
            # ma il callback (lambda) deve poter essere chiamato con uno
            # quindi faccio lambda con 4 parametri (_ , cell, x, y), e setto il default degli ultimi 3 a quello mi serve
            canvas.tag_bind(cell, "<Button-1>", lambda _, cell=cell, x=i, y=j: button_pressed(cell, x, y))
            row.append(0)
        table.append(row)
    return table


def draw_x(canvas, cell):
    # ottengo coordinate del quadrato (cella)
    coords = canvas.coords(cell)

    # disegno linee che collegano vertici opposti per fare la "X"
    canvas.create_line(coords[0], coords[1], coords[2], coords[3])
    canvas.create_line(coords[0], coords[3], coords[2], coords[1])


def draw_o(canvas, cell):
    # ottengo coordinate del quadrato (cella)
    coords = canvas.coords(cell)

    # disegno ovale inscritto nel quadrato della cella
    canvas.create_oval(coords[0], coords[1], coords[2], coords[3])


def test_winner(table, turn):
    # somme diagonali
    diag1_sum = 0
    diag2_sum = 0
    # vincitore se somma = -3 o 3
    winner = None
    i = 0
    while i < 3 and winner is None:
        # somma riga i
        row_sum = 0
        # somma colonna i
        col_sum = 0
        # calcolo somma riga colonna
        j = 0
        while j < 3:
            row_sum += table[i][j]
            col_sum += table[j][i]
            j += 1
        # controllo se vincitore su riga o colonna i
        if abs(row_sum) == 3:
            winner = row_sum / 3
        elif abs(col_sum) == 3:
            winner = col_sum / 3
        # aggiorno somma diagonali
        diag1_sum += table[i][i]
        diag2_sum += table[i][2 - i]
        i += 1
    # controllo vincitore sulle due diagonali
    if abs(diag1_sum) == 3:
        winner = diag1_sum/3
    if abs(diag2_sum) == 3:
        winner = diag2_sum/3
    # controllo pareggio
    if turn == 9 and winner is None:
        winner = 0
    return winner


def button_pressed(cell, x, y):
    # global variables
    global current_player
    global table
    global canvas
    global turn
    # controllo se cella ha già simbolo e nel caso ignoro il click
    if table[x][y] != 0:
        return
    # aggiorno tabella
    table[x][y] = current_player
    # disegno simbolo
    if current_player == 1:
        draw_x(canvas, cell)
    else:
        draw_o(canvas, cell)
    # controllo se c'è vincitore
    winner = test_winner(table, turn)
    if winner is not None:
        # se c'è stato un vincitore o pareggio lo segnalo
        if winner == 1:
            print('Player "X" wins')
        elif winner == -1:
            print('Player "O" wins')
        else:
            print("DRAW")
        # resetto partita
        current_player = STARTING_PLAYER
        table = reset_table(canvas)
        turn = 1
    else:
        # cambio giocatore e turno
        current_player = -current_player
        turn += 1
        
# creo finestra principale
root = Tk()
root.title("TicTacToe")

# dimensioni dei componenti su canvas
cell_size = 120
padding = 20
edge_padding = 20

# calcolo dimensioni finestra in base a componenti
window_height = cell_size*3 + padding*2 + edge_padding*2
window_width = window_height

# fissare dimensioni finestra e disabilitare resize
root.geometry("{}x{}".format(window_width, window_height))
root.resizable(False, False)

# configurare griglia di root
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# creare canvas e inserirla nella griglia di root
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))


# faccio iniziare giocatore STARTING PLAYER
table = reset_table(canvas)
current_player = STARTING_PLAYER
turn = 1

# avvio event loop
root.mainloop()

