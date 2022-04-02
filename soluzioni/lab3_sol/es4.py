from tkinter import *
from tkinter import ttk


def set_increment(*args):
    spin_box["increment"] = float(increment_box.get())


# crea finestra principale
root = Tk()
root.title("Contatore a step")
root.resizable(True, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# crea frame che contiene tutto
frame = ttk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(column=0, row=0, sticky=(N, S, W, E))

# configura dimensione relativa di colonne e righe
frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# variabili delle spinbox
start_value = 0
increment_values = [1, 2, 4, 8]
value = StringVar(value=start_value)
increment = StringVar(value=increment_values[0])

# label per spinbox contente valore
val_label = ttk.Label(frame, text="VALUE: ")
val_label.grid(column=0, row=0, sticky=(N, S, W, E))

# label per spinbox contente incremento
increment_label = ttk.Label(frame, text="INCREMENT: ")
increment_label.grid(column=0, row=1, sticky=(N, S, W, E))

# spinbox con valore
spin_box = ttk.Spinbox(frame, from_=start_value, to=100, textvariable=value, increment=increment_values[0], wrap=True)
spin_box.grid(column=1, row=0, sticky=(N, S, W, E))
spin_box.state(["readonly"])

# spinbox con incremento
increment_box = ttk.Spinbox(frame, values=increment_values, textvariable=increment, command=set_increment)
increment_box.grid(column=1, row=1, sticky=(N, S, W, E))
increment_box.state(["readonly"])

root.mainloop()

