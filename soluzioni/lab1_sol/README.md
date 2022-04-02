# Laboratorio 1
Questo laboratorio è un ripasso di ciò che è stato spiegato il primo anno nel corso di informatica.
Gli argomenti principali su cui riprendere confidenza sono:
- scrittura di semplici algoritmi
- controllo del flusso (if, for, while, ecc..)
- I/O da file e console
- manipolazione stringhe
- liste e tabelle
- strutture dati complesse (dizionari, set, tuple)
- funzioni

Dopo aver svolto gli esercizi, da casa, seguire la guida per la configurazione di git (guida git)
Al momento **NON E' POSSIBILE** eseguirla in lab per alcuni problemi di configurazione di rete.

## Esercizio 1
Scrivete un programma che legga una parola da console e visualizzi tutte le sue sottostringhe,
ordinate per lunghezza crescente.
Se, ad esempio, l’utente fornisce la stringa *“rum”*, il programma deve visualizzare:
```
r
u
m
ru
um
```

## Esercizio 2
Scrivete un programma che chieda all’utente di fornire due stringhe, per poi
visualizzare (evitando ripetizioni di caratteri nella stampa):
- i caratteri che compaiono in entrambe le stringhe;
- i caratteri che compaiono in una stringa ma non nell’altra;
- le lettere che non compaiono in nessuna delle due stringhe.

**Suggerimento**: trasformare una o più stringhe in un insieme (*set*) di caratteri.

## Esercizio 3
Scrivete un programma che legga tutte le righe di un file di testo (*input.txt*), le stampi su console, ne
inverta l’ordine e le scriva in un altro file (*output.txt*). Ad esempio, se il file *input.txt*
contiene queste righe:
```
Mary had a little lamb
Its fleece was white as snow
And everywhere that Mary went
The lamb was sure to go.
```
allora il file *output.txt* conterrà:
```
The lamb was sure to go.
And everywhere that Mary went
Its fleece was white as snow
Mary had a little lamb
```

## Esercizio 4
Scrivere un programma che chieda all'utente di inserire coppie di numeri positivi (*a*,*b*).
Quando l'utente inserisce (*-1*, *-1*), il programma termina.
Per ogni coppia (*a*,*b*) il programma ne calcola il [coefficiente binomiale](https://it.wikipedia.org/wiki/Coefficiente_binomiale),
dove è *n* è il valore maggiore della coppia, mentre *k* il minore.
Il programma deve usare due funzioni:
- la prima calcola il fattoriale di un intero positivo passato come parametro
- la seconda calcola il coefficiente binomiale della coppia (*a*, *b*), invocando la prima per calcolo dei fattoriali.


## Esercizio 5
Leggere una sequenza di numeri interi conclusa da una riga vuota.
Stampare la posizione dei massimi locali (numeri maggiori sia del valore precedente che di quello successivo),
se ce ne sono.
Altrimenti stampare il messaggio *“Non ci sono massimi locali”.*

## Esercizio 6
Stampare un a matrice *NxN*, dove *N* è un intero positivo fornito in input dall'utente.
La matrice deve contenere un 1 nella cella in alto a sinistra,
e ogni altra cella deve contenere la somma dei valori presenti nella cella sovrastante e in quella alla propria sinistra.

Per esempio, per *N=4*:

```bash
 1  1  1  1
 1  2  3  4
 1  3  6 10
 1  4 10 20
```


## Esercizio 7
Scrivete un programma che conti le occorrenze di ciascuna parola presente in un
file di testo, il cui nome è inserito da tastiera. Si assuma che il file contenga solo
caratteri alfabetici o di spaziatura.

Successivamente, migliorate il programma in
modo che visualizzi le 100 parole più comuni (in caso di parità alla posizione 100, è
indifferente quali parole si stampino).

Infine, testare il programma cercando le parole più ricorrenti nei *Promessi Sposi* (*promessi_sposi.txt*).
Migliorarlo per quanto possibile (rimuovere punteggiatura, parole vuote, ecc...)


