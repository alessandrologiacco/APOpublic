from tkinter import *
from tkinter import ttk


def change_color(*args):
    l1["background"] = label_color.get()


# crea finestra principale
root = Tk()
root.title("Selettore colore")
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# crea frame che contiene tutto
frame = ttk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(column=0, row=0, sticky=(N, S, W, E))
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

# aggiunge label, e bottoni
label_color = StringVar(value="red")
l1 = ttk.Label(frame, text="Color", anchor=CENTER, background=label_color.get())
r = ttk.Radiobutton(frame, text='Rosso', variable=label_color, value='red', command=change_color)
y = ttk.Radiobutton(frame, text='Giallo', variable=label_color, value='yellow', command=change_color)
b = ttk.Radiobutton(frame, text='Blu', variable=label_color, value='blue', command=change_color)

# posiziona label e bottoni nella griglia del frame
l1.grid(column=0, row=0, rowspan=3, sticky=(N, S, W, E))
r.grid(column=1, row=0)
y.grid(column=1, row=1)
b.grid(column=1, row=2)


# avvia l'event loop
root.mainloop()
