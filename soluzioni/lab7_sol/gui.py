from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from university import *


# gestisco aggiunta studente
def add_student(win, name, surname):
    if name != "" and surname != "":
        s_id = uni.add_student(name, surname)
        messagebox.showinfo(title="Success!", message="Student {} added".format(s_id))
        win.destroy()


# gestisco finestra info
def get_student(win, s_id):
    if id != "":
        try:
            s_id = int(s_id)
            messagebox.showinfo(title="Student found!", message=uni.get_student_info(s_id))
            win.destroy()
        except ValueError:
            messagebox.showerror(title="Error", message="Invalid id")
        except Exception:
            messagebox.showerror(title="Error", message="Student not found")


def show_add_student_window():
    # creo finestra
    win = Toplevel(root)
    win.title('Add student')
    win.minsize(500, 100)
    # configuro griglia
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    # creo labels
    l1 = ttk.Label(win, text="Nome: ")
    l2 = ttk.Label(win, text="Cognome: ")
    l1.grid(column=0, row=0, sticky=(N, S, W, E))
    l2.grid(column=0, row=1, sticky=(N, S, W, E))
    # creo entries
    name = StringVar()
    surname = StringVar()
    name_entry = ttk.Entry(win, textvariable=name)
    surname_entry = ttk.Entry(win, textvariable=surname)
    name_entry.grid(column=1, row=0, sticky=(N, S, W, E))
    surname_entry.grid(column=1, row=1, sticky=(N, S, W, E))
    # creo bottone
    b = ttk.Button(win, text="Aggiungi", command=lambda: add_student(win, name.get(), surname.get()))
    b.grid(column=0, row=2, columnspan=2, sticky=(N, S, W, E))


def show_get_student_window():
    # creo finestra
    win = Toplevel(root)
    win.title('Add student')
    win.minsize(500, 100)
    # configuro griglia
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    # creo labels
    l1 = ttk.Label(win, text="Matricola: ")
    l1.grid(column=0, row=0, sticky=(N, S, W, E))
    # creo entries
    s_id = StringVar()
    id_entry = ttk.Entry(win, textvariable=s_id)
    id_entry.grid(column=1, row=0, sticky=(N, S, W, E))
    # creo bottone
    b = ttk.Button(win, text = "Cerca", command=lambda: get_student(win, s_id.get()))
    b.grid(column=0, row=1, columnspan=2, sticky=(N, S, W, E))


# creo oggetto university
uni = University("PoliTo")

# finestra principale
root = Tk()
root.title("University")
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# aggiungo bottoni
b1 = ttk.Button(root, text="Add student", command=show_add_student_window)
b2 = ttk.Button(root, text="Get student", command=show_get_student_window)
b1.grid(column=0, row=0, sticky=(N, S, W, E))
b2.grid(column=0, row=1, sticky=(N, S, W, E))

# avvio event loop
root.mainloop()
