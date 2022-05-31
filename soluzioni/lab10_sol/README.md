# Laboratorio 10
Gli obiettivi principali di questo laboratorio sono:
- *args e **kwargs
- classi astratte (ABC)
- staticmethod, classmethod e property
- funzioni lambda
- callable classes (\_\_call\_\_) 
- inner functions, closure e closure factory
- second order functions e decorators

# Esercizio 1
Sviluppare la classe astratta *Shape* che eredita da *ABC*, rappresentante una figura geometrica.
Il costruttore accetta come unico parametro il nome che si vuole associare alla figura.
(ad es., "figura1", "la mia forma", etc...)
Il nome deve essere ottenibile tramite opportuno getter.
La classe possiede due metodi astratti che restituiscono, rispettivamente, il perimetro e l'area della figura.

La classe *Triangle*, rappresentante un triangolo, eredita da *Shape*.
Il suo costruttore, oltre al nome del triangolo,
accetta la lunghezza della base e un numero variabile di lunghezze degli altri lati.
Se viene fornita solo la lunghezza della base il triangolo è equilatero,
se viene fornita la lunghezza di un altro lato il triangolo è isoscele, altrimenti è scaleno.

Implementare i metodi astratti che della classe padre che restituiscono area e il perimetro.
Per il calcolo dell'area in modo generico si può utilizzare la
[formula di Erone](https://it.wikipedia.org/wiki/Formula_di_Erone).

La classe *Square* eredita da *Shape* e rappresenta un quadrato.
Il suo costruttore, oltre a nome del quadrato, accetta la lunghezza del lato.
Implementare i metodi astratti della classe padre che restituiscono l'area e il perimetro.

# Esercizio 2
Sviluppare la classe *Thermostat* rappresentate un termostato.
Il costruttore accetta come parametri la temperatura target da mantenere
e un valore booleano che esprime se l'utente vuole usare gradi Celsius o Fahrenheit.
La classe presenta due metodi statici (*staticmethod*)
che trasformano gradi Celsius in Fahrenheit e viceversa.

Sviluppare un metodo di classe (classmethod) che restituisce una nuova istanza della classe *Thermostat*,
copia di quella passata come parametro (questo è similare al costruttore di copia trovato in altri linguaggi).

Sia la temperatura target che il valore booleano devono essere ottenibili
e settabili tramite properties (usare gli appositi decoratori).
Se la temperatura impostata supera i 30 Celsius (o equivalente Fahrenheit)
limitarla a 30 Celsius (o equivalente Fahrenheit).

Per la temperatura ricordare che viene sia fornita che restituita nel formato (Celsius o Fahrenheit)
definito in quel momento. Inoltre, cambiare il formato non deve cambiare la temperatura target impostata.

**SUGGERIMENTO**: Per gestire i formati Celsius o Fahrenheit
è conveniente sceglierne uno solo per rappresentazione interna alla classe e poi fare le dovute conversioni
nei getter e setter (in questo caso definiti tramite properties).

# Esercizio 3
Sviluppare la classe *SortableCouple*, rappresentante una coppia di valori floating point *(a, b)*.
Il costruttore accetta come parametri i due valori della coppia.
Questi sono anche ottenibili, ma **NON** settabili, tramite properties.

La classe implementa il metodo ```__repr__(self) -> str``` e il metodo ```__lt__(self, other) -> bool```.
Il secondo confronta le coppie secondo la somma dei valori *a* e *b*. 
Scrivere un main che crei una lista di *SortableCouple* e la riordini tramite il metodo sort.

Successivamente passare come parametro *key* del metodo sort una funzione lambda che,
preso come parametro una *SortableCouple*, restituisca il prodotto *a\*b*.
Questa specifica un altro metodo di confronto delle *SortableCouple*,
usando come valore di confronto il prodotto dei valori contenuti.
Verificare il nuovo ordinamento.

Scrivere una classe *CoupleSorter* che contenga unicamente il metodo ```__call__(self, elm: SortableCouple) -> float``` che,
ricevuto come parametro una *SortableCouple*, restituisca il la differenza *a - b*.

Nel main, creare un'istanza di questa classe e passarla come parametro *key* del metodo sort che riordina la lista.
Similmente a prima, il metodo sort userà ```__call__(self, elm: SortableCouple) -> float``` sulle *SortableCouple*
per ottenere il valore con cui confrontarle.
Verificare il nuovo ordinamento.

# Esercizio 4
Sviluppare la classe *WeightedSorter* per definire un nuovo ordinamento delle *SortableCouple*.
Il costruttore accetta come parametro un valore floating point compreso nel'intervallo [0, 1],
rappresentante il peso (*weight*).
Esso è ottenibile e settabile tramite property.
Il metodo ```__call__(self, elm: SortableCouple) -> float```, restituisce un valore di confronto della *SortableCouple*
definito come segue:
``` python
a * weight + b * (1 - weight)
```
Nel main creare una lista di *SortableCouple*
e un'istanza della classe *WeightedSorter* da passare come parametro *key* del metodo sort della lista.
Come si può notare è possibile personalizzare il tipo di ordinamento
creando istanze apposite della classe *WeightedSorter*.

Definire una closure factory (funzione di secondo ordine) che, preso il peso *weight* come parametro,
restituisca una seconda funzione (closure). 
La funzione restituita accetta una *SortedCouple* come parametro
e restituisce lo stesso valore di confronto definito precedentemente, tramite l'utilizzo del peso *weight*.
Equivalentemente al caso precedente è possibile personalizzare il tipo di ordinamento
fornendo valori diversi di *weight* alla closure factory.

Verificare che in entrambi i casi si ottiene il medesimo ordinamento della lista.

# Esercizio 5
Scrivere due decoratori per funzioni con argomenti sconosciuti (*args, **kwargs).
Il primo decoratore, ```repeat_ten_times(f)```, fa in modo che la funzione decorata sia invocata 10 volte.
Il secondo decoratore, ```time_execution(f)```,
stampa il tempo di esecuzione della funzione decorata, espresso in nanosecondi, dopo averla invocata.

Sviluppare la classe *Greet*, il cui costruttore accetti come parametro il nome della persona da salutare.
Il metodo ```say_hello(self) -> None``` stampa a schermo la scritta *"Hello"* seguita dal nome della persona
(ad es., *"Hello Pietro"*)

Il metodo ```say_good(self, time_of_day: str) -> None``` 
accetta come parametro un stringa contente il periodo della giornata (ad es., *"morning"*, *"afternoon"*, ecc...),
e stampa a schermo la scritta *"Good"* seguita dal periodo della giornata e il nome della persona
(ad es., *"Good evening Pietro"*).

Decoratore i due metodi con entrambi i decoratori, usandoli in ordine opposto.
Scrivere un main che testi i due metodi e notare le differenze dovute all'ordine dei decoratori.

**SUGGERIMENTO**: per calcolare il tempo di esecuzione di una funzione, importare *time*
e chiamare ```time.perf_counter_ns()``` prima e dopo averla invocata.
La differenza dei valori restituiti da ```time.perf_counter_ns()``` è il tempo di esecuzione in nanosecondi.
















