from tkinter import *
from tkinter import ttk

# dizionario che mappa giocatore a punteggio
score_dict = {}


# callback associato al bottone
def insert_player():
    # avoid adding player with empty name
    if player.get == "":
        return
    try:
        # add player if not present and update score
        score_dict[player.get().strip()] = float(score.get())
    except ValueError as err:
        # ignore if score is not a number
        return
    # creo lista tuple punteggio, giocatore e la ordino in modo decrescente
    score_list = [(score, player) for player, score in score_dict.items()]
    score_list.sort(reverse=True)
    # aggiorno lista giocatori della listbox
    leaderboard_box.delete(0, leaderboard_box.size() - 1)
    for s, p in score_list[:3]:
        leaderboard_box.insert(END, "{}: {}".format(p, s))


# crea finestra principale
root = Tk()
root.title("Classifica giocatori")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)

# crea frame che contiene tutto tranne classifica
frame1 = ttk.Frame(root, borderwidth=5, relief="ridge")
frame1.grid(column=0, row=0, sticky=(N, S, W, E))

# configura dimensione relativa di colonne e righe
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)

# crea frame che conterrà listbox giocatori
frame2 = ttk.Frame(root, borderwidth=5, relief="ridge")
frame2.grid(column=0, row=1, sticky=(N, S, W, E))

# configura dimensione relativa di colonne e righe
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

# variabili delle entry
player = StringVar()
score = StringVar()

# lista giocatori, punteggio della listbox
player_list = StringVar()

# entry con nome giocatore
player_entry = Entry(frame1, textvariable=player)
player_entry.grid(column=1, row=0, sticky=(N, S, W, E))

# entry con punteggio giocatore
score_entry = Entry(frame1, textvariable=score)
score_entry.grid(column=1, row=1, sticky=(N, S, W, E))

# label nome giocatore
player_label = ttk.Label(frame1, text="Nome: ")
player_label.grid(column=0, row=0, sticky=(N, S, W, E))

# label per punteggio
score_label = ttk.Label(frame1, text="Punteggio: ")
score_label.grid(column=0, row=1, sticky=(N, S, W, E))

# bottone per aggiungere punteggio
insert_button = ttk.Button(frame1, text="Inserisci", command=insert_player)
insert_button.grid(column=2, row=0, rowspan=2, sticky=(N, S, W, E))

# listbox con classifica giocatori
leaderboard = StringVar()
leaderboard_box = Listbox(frame2, listvariable=leaderboard, height=3)
leaderboard_box.grid(column=0, row=0, columnspan=3, sticky=(N, S, W, E))

root.mainloop()
