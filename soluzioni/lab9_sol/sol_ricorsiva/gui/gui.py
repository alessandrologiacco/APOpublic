from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from hydraulics.hsystem import HSystem
from hydraulics.elements import Source, Tap, Sink, Split


# gestisco aggiunta studente
def add_element(win, name, elm_type):
    # creo elemento del tipo voluto
    if elm_type == "Source":
        element = Source(name)
    elif elm_type == "Tap":
        element = Tap(name)
    elif elm_type == "Split":
        element = Split(name)
    elif elm_type == "Sink":
        element = Sink(name)

    # lo aggiungo, segnalo successo, chiudo finestra
    hsys.add_element(element)
    messagebox.showinfo(title="Success!", message="{} {} added".format(elm_type, name))
    # chiudo finestra
    win.destroy()


def show_add_element_window():
    # creo finestra
    win = Toplevel(root)
    win.title('Add element')
    win.minsize(500, 100)

    # configuro griglia
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    win.rowconfigure(3, weight=1)
    win.rowconfigure(4, weight=1)
    win.rowconfigure(5, weight=1)
    win.rowconfigure(6, weight=1)
    win.rowconfigure(7, weight=1)

    # creo label
    l1 = ttk.Label(win, text="Nome: ")
    l1.grid(column=0, row=0, sticky=(N, S, W, E))

    # creo entry
    name = StringVar()
    name_entry = ttk.Entry(win, textvariable=name)
    name_entry.grid(column=0, row=1, sticky=(N, S, W, E))

    # creo radio buttons
    elm_type = StringVar()
    source = ttk.Radiobutton(win, text='Source', variable=elm_type, value='Source')
    tap = ttk.Radiobutton(win, text='Tap', variable=elm_type, value='Tap')
    split = ttk.Radiobutton(win, text='Split', variable=elm_type, value='Split')
    sink = ttk.Radiobutton(win, text='Sink', variable=elm_type, value='Sink')

    # posiziono radio buttons
    source.grid(column=0, row=2, sticky=(N, S, W, E))
    tap.grid(column=0, row=3, sticky=(N, S, W, E))
    split.grid(column=0, row=4, sticky=(N, S, W, E))
    sink.grid(column=0, row=5, sticky=(N, S, W, E))

    # creo bottone conferma
    b = ttk.Button(win, text="Aggiungi", command=lambda: add_element(win, name.get(), elm_type.get()))
    b.grid(column=0, row=6, sticky=(N, S, W, E))


def show_elements():
    # creo messaggio con tipo e nome elementi
    elm_str = "\n".join(["{} {}".format(type(element).__name__, element.get_name()) for element in hsys.get_elements()])
    messagebox.showinfo(title="Elements", message=elm_str)


# creo oggetto university
hsys = HSystem()

# finestra principale
root = Tk()
root.title("Sistema Idraulico")
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# aggiungo bottoni
b1 = ttk.Button(root, text="Add element", command=show_add_element_window)
b2 = ttk.Button(root, text="Get elements", command=show_elements)
b1.grid(column=0, row=0, sticky=(N, S, W, E))
b2.grid(column=0, row=1, sticky=(N, S, W, E))

# avvio event loop
root.mainloop()
