from tkinter import *
from tkinter import ttk
import random
import collision

# dimensioni finestra
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500

# dimensioni navicella
SHIP_WIDTH = 30
SHIP_HEIGHT = 35

# velocità navicella
SHIP_STEP = 10

# dimensione asteriodi
ASTEROID_DIAM_MIN = 30
ASTEROID_DIAM_DIFF = 50

# velocità asteroidi
ASTEROID_STEP = 20

# timer grafici
SPAWN_TIME = 1000
MOVE_TIME = 500


# callback callback che muove la navicella
def move_ship(event):
    # trovo estremi navicella
    ship_coords = canvas.coords(ship)
    top = ship_coords[5]
    left = ship_coords[0]
    right = ship_coords[2]
    bottom = ship_coords[1]

    # controllo se sono al bordo e poi muovo navicella
    if event.keysym == "Left" and left - SHIP_STEP> 0:
        canvas.move(ship, -SHIP_STEP, 0)
    elif event.keysym == "Right" and right + SHIP_STEP < CANVAS_WIDTH:
        canvas.move(ship, SHIP_STEP, 0)
    elif event.keysym == "Up" and top - SHIP_STEP > 0:
        canvas.move(ship, 0, - SHIP_STEP)
    elif event.keysym == "Down"  and bottom + SHIP_STEP < CANVAS_WIDTH:
        canvas.move(ship, 0, SHIP_STEP)
    
    # dopo spostamento controllo se navicella ha colpito asteroide
    if collision.check_hit(canvas, ship, asteroid_set):
        reset_table()

def move_asteroid(asteroid, game):
    # variabili globali
    global score
    global asteroid_set

    # non muovo più se asteroide se di una vecchia partita
    if game != current_game:
        return

    # sposto asteroide
    canvas.move(asteroid, 0, ASTEROID_STEP)

    # controllo collisione
    if collision.check_hit(canvas, ship, asteroid_set):
        reset_table()
        return
    
    # se asteroide è uscita
    if canvas.coords(asteroid)[1] >= CANVAS_WIDTH:
        # la rimuovo dal canvas e dal set
        canvas.delete(asteroid)
        asteroid_set.remove(asteroid)
        #aggiorno punteggio  
        score += 100        
        print("Score: {}".format(score))        
    else:
        # altrimenti la sposto dopo timeout
        canvas.after(MOVE_TIME, lambda a = asteroid, g = game: move_asteroid(a,g))


def create_asteroid(game):
    # controllo se è un callback di una partita vecchia
    if game != current_game:
        return

    # dimensione e posizione random
    diam = round(ASTEROID_DIAM_MIN + ASTEROID_DIAM_DIFF* random.random())
    posx = random.randint(0, CANVAS_WIDTH - diam)
    posy = 0

    # aggiungo asteroide ad canvas
    asteroid = canvas.create_oval (
        posx, posy - diam,
        posx + diam, posy,
        fill="",
        outline="white",
        width = "2"
    )

    # aggiungo al set asteroidi
    asteroid_set.add(asteroid)

    # setto timer per nuova asteroide e movimento
    canvas.after(MOVE_TIME, lambda a = asteroid, g = current_game: move_asteroid(a,g))
    canvas.after(SPAWN_TIME, lambda g = current_game : create_asteroid(g))

    

# pulisco canvas e setto navicella in centro
def reset_table(first = False):
    # variabili globali
    global score
    global ship
    global asteroid_set
    global current_game

    # aggiorno numero partita
    current_game = 0 if first else current_game + 1

    # resetto punteggio
    score = 0
    asteroid_set = set()

    # pulisco canvas
    canvas.delete("all")
    x_center = CANVAS_WIDTH//2
    y_center = CANVAS_HEIGHT//2

    # creo navicella
    ship = canvas.create_polygon(
        x_center - SHIP_WIDTH // 2,
        y_center,
        x_center + SHIP_WIDTH // 2,
        y_center,
        x_center,
        y_center - SHIP_HEIGHT,
        fill="",
        outline="white",
        width = "4"
    )

    # registro callback che muove la navicella
    root.bind("<Left>", move_ship)
    root.bind("<Right>", move_ship)
    root.bind("<Up>", move_ship)
    root.bind("<Down>",  move_ship)
    
    # avvio creazione asteroidi
    create_asteroid(current_game)


# creo finestra principale
root = Tk()
root.title("Asteroid")

# fissare dimensioni finestra e disabilitare resize
root.resizable(False, False)

# configurare griglia di root
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# creare canvas e inserirla nella griglia di root
canvas = Canvas(root, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# create elements
reset_table(first = True)

# avvio event loop
root.mainloop()

