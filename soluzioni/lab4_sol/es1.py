from tkinter import *
from tkinter import ttk


# dimensione finestra
WINDOW_SIZE = 500
HORIZON_X = WINDOW_SIZE/2
HORIZON_Y = 0

# quando muovo con mouse premuto creo linea con pos corrente e orizzonte
def addLine(event):
    canvas.create_line((event.x, event.y, HORIZON_X, HORIZON_Y))


# creo finestra principale
root = Tk()
root.title("SketchPad")

# fissare dimensioni finestra e disabilitare resize
root.geometry("{}x{}".format(WINDOW_SIZE, WINDOW_SIZE))
root.resizable(False, False)

# configurare griglia di root
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# creare canvas e inserirla nella griglia di root
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# registro callback al movimento del mouse
canvas.bind("<B1-Motion>", addLine)

# avvio event loop
root.mainloop()