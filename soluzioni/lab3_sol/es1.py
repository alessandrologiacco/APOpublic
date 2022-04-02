from tkinter import *
from tkinter import ttk


# callback del bottone premuto
def button_pressed():
    global color_index
    color_index += 1
    l1["background"] = color_list[color_index % len(color_list)]


# crea finestra principale
root = Tk()
root.title("Selettore colore")

# limita rimpicciolimento finestra altre limite
root.minsize(500, 300)

# crea frame che contiene tutto
frame = ttk.Frame(root, borderwidth=5, relief="ridge")

# posiziona frame nella griglia del padre (root) nella cella (0,0)
# sticky per adattare frame alla grandezza della cella
frame.grid(column=0, row=0, sticky=(N, S, W, E))

# permette a col 0 e riga 0 di root (e quindi alla cella 0,0) di ridimensionarsi se la finestra si ingrandisce
# anche il frame contenuto, essendo sticky, si ingrandisce
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# lista di colori per label
color_index = 0
color_list = ["red", "blue", "yellow"]

# aggiunge label, mette testo in centro e setta primo colore
l1 = ttk.Label(frame, text="Color", anchor=CENTER, background=color_list[color_index])

# aggiunge bottone che scorre i colori, e collega callback per quando viene premuto
b1 = ttk.Button(frame, text="Switch color", command=button_pressed)

# posiziona label e bottone nella griglia del frame
l1.grid(column=0, row=0, sticky=(N, S, W, E))
b1.grid(column=0, row=1, sticky=(N, S, W, E))

# fa sì che celle della griglia del frame si ingrandiscano con il frame
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)

# avvia l'event loop
root.mainloop()


