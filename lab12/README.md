# Laboratorio 12
Gli obiettivi principali di questo laboratorio sono:
- ricorsione
- algoritmi di sorting
- strutture dati


## Esercizio 1
Scrivere una funzione ricorsiva che accetti un intero *n* come parametro e restituisca la
somma di tutti gli interi da *1* a *n*. Esempio:
```
X: 4
Output: 10
Esercizio 2
```

## Esercizio 2
Scrivere una funzione ricorsiva che stampi tutti i numeri binari di lunghezza a scelta in
ordine crescente.
```
Esempio
Length: 3
Output: 000, 001, 010, 011, 100, 101, 110, 111
```

## Esercizio 3
Scrivere una funzione ricorsiva che sia in grado d'implementare una funzionalità simile a
quella del ”Paint Bucket” presente negli editor d'immagini.

Data una matrice (l’immagine), contenete interi (colori di ciascun pixel),
un intero (nuovo colore) e una posizione (pixel di partenza),
il programma deve cambiare il colore all’insieme di tutti i pixel contigui aventi lo
stesso colore del pixel di partenza (e contenente lo stesso).

I pixel confinanti in un vertice sono considerati contigui.

```python
Nuovo colore: 1
Posizione: (2,4) # (riga, colonna) partendo da 0

Immagine di partenza
5 2 3 2 1 4 
1 4 2 5 2 4 
2 3 2 2 2 5 
2 4 1 2 3 1

Immagine risultante
5 1 3 1 1 4 
1 4 1 5 1 4 
2 3 1 1 1 5 
2 4 1 1 3 1 
```

## Esercizio 4
Scrivere una funzione che ordini un lista in ordine crescente usando il merge sort
ricorsivo.
Scrivere un'implementazione dell'algoritmo che sia stabile.

## Esercizio 5
Scrivere una classe che implementi una coda FIFO.
**NON** usare le liste di python ma svilupparla implementando una linked list.

La classe deve permettere le seguenti operazioni:
- aggiunta elemento in coda (append)
- rimozione elemento in testa (pop)
- accesso agli elementi tramite posizione con operatore []
(fare override di *\_\_getitem\_\_(self, pos)*)

Fornire una rappresentazione in stringa dela lista
tramite override di *\_\_repr\_\_(self)*.

**SUGGERIMENTO:** creare due classi separate, una rappresentate la lista
e l'altra rappresentante i suoi nodi.
I nodi conterranno l'elemento e un riferimento al nodo successivo.

## Esercizio 6
Scrivere una classe che implementi un albero binario di ricerca.
La classe deve fornire le seguenti funzionalità:
- permettere l'inserimento di valori
- trovare il minimo dei valori inseriti
- avere una rappresentazione in stringa (\_\_repr\_\_(self))
che contenga i valori aggiunti in modo ordinato
(leggerli dall'albero in modo ordinato,
**NON** ordinarli tramite un algoritmo di sorting).

**SUGGERIMENTO:** creare due classi separate,
una rappresentate l'albero
e l'altra rappresentante i suoi nodi.
I nodi conterranno i valori aggiunti all'albero
e i riferimenti ai due nodi figlio.
