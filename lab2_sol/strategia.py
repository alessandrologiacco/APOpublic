FILE_SCHIERAMENTO = "./data/schieramento.txt"


# cerca numero maggiore di uno intorno and una cella contenente un uno
# e ritorna la direzione di conseguenza, None se non è possibile stabilirlo
def find_direction(schieramento, riga, colonna):
    direction = None
    if riga > 0 and schieramento[riga - 1][colonna] > 1:
        direction = "Sud"
    elif riga < len(schieramento) - 1 and schieramento[riga + 1][colonna] > 1:
        direction = "Nord"
    elif colonna > 0 and schieramento[riga][colonna - 1] > 1:
        direction = "Est"
    elif colonna < len(schieramento[riga]) - 1 and schieramento[riga][colonna + 1] > 1:
        direction = "Ovest"
    return direction


def main():
    # carica schieramento in una tabella
    schieramento = []
    with open(FILE_SCHIERAMENTO) as file:
        for line in file:
            # rimuove newline a fine stringa
            line = line.strip()
            row = []
            for c in line:
                row.append(int(c))
            schieramento.append(row)
    # inizializza valori
    larghezza = 0
    idx_riga = 0
    num_file = 0
    direction = None
    # dizionario che mappa numeri maggiori di zero (chiave) al numero di volte che appaiono (valore)
    num_in_fila = {}
    for riga in schieramento:
        idx_colonna = 0
        for posizione in riga:
            # larghezza schieramento si trova contando gli uno
            if posizione == 1:
                larghezza += 1
            # numero di file è uguale al numero più alto nella tabella
            if posizione > num_file:
                num_file = posizione
            # aggiorna il conteggio di quante vote appare ciascun numero
            if posizione != 0:
                if posizione not in num_in_fila:
                    num_in_fila[posizione] = 1
                else:
                    num_in_fila[posizione] += 1
            # se cella contiene un uno controlla le celle intorno per capire direzione
            if posizione == 1 and direction is None:
                direction = find_direction(schieramento, idx_riga, idx_colonna)
            idx_colonna += 1
        idx_riga += 1

    # trova numero com massimo numero di occorrenze
    min_in_fila = larghezza
    for k, v in num_in_fila.items():
        if v < min_in_fila:
            min_in_fila = v
            fila_minore = k

    print("Larghezza: {}".format(larghezza))
    print("Numero di file: {}".format(num_file))
    print("Direzione: {}".format(direction))
    print("Fila con più buchi: {}".format(fila_minore))


if __name__ == "__main__":
    main()
