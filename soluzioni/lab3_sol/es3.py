from tkinter import *
from tkinter import ttk

FILE = "./data/sabato.txt"
USE_LISTBOX = False  # settare a True per cambiare widget usato


# versione con Text
def text_version(frame, poesia):
    text_box = Text(frame)
    text_box.grid(column=0, row=0, sticky=(N, S, W, E))
    for line in poesia:
        text_box.insert(END, line + "\n")
    # aggiunge scrollbar verticale di fianco al testo,
    # e setta come callback il metodo yview della textbox che cambia cosa si vede nella textbox
    scroll_bar = ttk.Scrollbar(frame, orient=VERTICAL, command=text_box.yview)
    scroll_bar.grid(column=1, row=0, sticky=(N, S, W, E))

    # a sua volta la textbox, quando viene "scrollata",
    # chiama un callback (metodo set della scrollbar) che sposta la barra di scorrimento
    text_box['yscrollcommand'] = scroll_bar.set


# versione con Listbox
def listbox_version(frame, poesia):
    # crea listbox contenete poesia, trasformandola prima in StringVar
    text = StringVar(value=poesia)
    lst_box = Listbox(frame, listvariable=text, height=10)
    lst_box.grid(column=0, row=0, sticky=(N, S, W, E))

    # aggiunge scrollbar verticale di fianco alla lista,
    # e setta come callback il metodo yview della listbox che cambia cosa si vede nella lista
    scroll_bar = ttk.Scrollbar(frame, orient=VERTICAL, command=lst_box.yview)
    scroll_bar.grid(column=1, row=0, sticky=(N, S, W, E))

    # a sua volta, la listbox, quando viene "scrollata",
    # chiama un callback (metodo set della scrollbar), che sposta la barra di scorrimento
    lst_box['yscrollcommand'] = scroll_bar.set


# legge poesia da file e salva righe in una lista
poesia = []
with open(FILE, "r") as file:
    for line in file:
        poesia.append(line.strip())

# crea finestra principale e frame
root = Tk()
root.title("Lettore testo")
frame = ttk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(column=0, row=0, sticky=(N, S, W, E))

# configura griglia del frame e di root per ridimensionare righe e colonne se finestra viene ingrandita
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# in base al flag usa una listbox o text per contenere il testo
if USE_LISTBOX:
    listbox_version(frame, poesia)
else:
    text_version(frame, poesia)

# avvia l'event loop
root.mainloop()
