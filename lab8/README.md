# Laboratorio 8
In questo laboratorio viene esplorata l'ereditarietà.

Pertanto gli obiettivi principali di questo laboratorio sono:
- creare classi figlio da una classe padre
- utilizzo di super() nei costruttori e nei metodi
- prendere confidenza con l'overriding dei metodi
- comprendere e sfruttare il polimorfismo

# Esercizio 1
Creare la classe *Room* rappresentate una generica stanza di un'abitazione.
I costruttore accetta come parametri il numero di metri quadri,
il numero di finestre e il numero di prese per la corrente.
Fornire un getter per ciascuna di queste proprietà.

Creare la classe *BathRoom* che eredita da *Room*.
Il costruttore, oltre ai parametri del padre,
accetta il numero di lavandini e tre valori booleani
indicanti la presenza della doccia, della vasca e del bidet.
Scrivere dei getter per questi parametri aggiuntivi.

Scrivere un main che crei delle istanze di queste classi.
Verificare che la classe figlio possieda i getter del padre
senza averli dovuti riscrivere.

# Esercizio 2
Creare la classe *File* rappresentante un generico file vuoto.
Il costruttore deve accettare come unico parametro il nome del file.

Creare tre getter: ```get_name(self)```, ```get_dim(self)``` e ```get_info(self)```.
Il primo restituisce il nome del file e il secondo la sua dimensione (zero in quanto vuoto).
```get_info(self)``` restituisce una stringa contenente sia il nome che la dimensione del file.
Per ottenerli **DEVE** usare i metodi ```get_name(self)``` e ```get_dim(self)```.

Scrivere il metodo ```__repr__(self)``` che restituisca in contenuto del file,
in questo caso una stringa vuota.

Creare la classe *TextFile* che eredita da *File*.
Il costruttore, come il padre, accetta come unico parametro il nome del file.
Scrivere il metodo ```add_line(self, str: line)``` che,
passata una stringa, la aggiunga come nuova riga del file.

Fare l'override dei metodi ```dim(self)``` e ```__repr(self)__``` per restituire, rispettivamente,
il numero di righe e una stringa rappresentante il contenuto del file.

Creare la classe *BitMap* che eredita da *File*.
Il costruttore accetta come parametri il nome del file e una tabella contenente numeri da 0 a 255
(non controllare correttezza) rappresentante i colori dell'immagine.

Fare l'override del metodo ```dim(self)``` per restituire un tupla contenente le dimensioni dell'immagine.
Fare l'override del metodo ```__repr__``` per restituire una stringa rappresentate l'immagine,
convertendo i numeri colore a esadecimale tramite la funzione ```hex()```.

Scrivere un main che crei almeno un'istanza per classe
e verificare che i metodi di cui è stato fatto l'override si comportino in modo diverso tra le classi.

Notare che anche il metodo ```get_info(self)``` cambia comportamento,
perché nonostante non venga fatto l'override esplicito, esso utilizza metodi di cui invece viene fatto.


# Esercizio 3
In questo esercizio utilizzeremo le classi sviluppate nell'esercizio precedente in modo polimorfico.

Creare la classe *Directory* rappresentante una cartella.
Il costruttore accetta come unico parametro il nome della directory.
Il metodo ```add_file(self, file)``` permette di aggiungere un file alla cartella.

Il metodo ```open_files(self)``` stampa a schermo il contenuto di tutti i file contenuti nella cartella.
Il metodo ```__repr__(self)``` stampa il nome della cartella e, sotto di esso, le informazioni (nome e dimensione)
di tutti i file che contiene (chiamando ```get_info(self)``` su di essi).

```
my_folder: 
        empty.info: 0
        myimage.bmp: (3, 2)
        mytext.txt: 3
```

Scrivere una main che, utilizzando le classi dell'esercizio precedente,
crei delle istanze di diversi tipi di file e li aggiunga a un oggetto *Directory*.

Notare che il codice che viene scritto per ```open_files(self)``` e ```__repr__(self)```
non è a conoscenza del tipo di file su cui opera,
ma si comporta lo stesso diversamente a secondo del tipo di file su cui sta agendo.
Questa è l'utilità del polimorfismo.

# Esercizio 4
Creare la classe *Ticket* rappresentate un biglietto per una coda.

Il costruttore accetta come parametri il nome del possessore e il numero.
Il metodo ```get_queue_pos(self)``` restituisce la posizione in coda, pari al numero del biglietto.
Il metodo ```__repr__(self)``` restituisce una stringa contenente il nome e il numero del biglietto.

Implementare il metodo ```__lt__(self, other)``` per confrontare i biglietti per posizione in coda.
**USARE** il metodo ```get_queue_pos(self)``` per ottenere la posizione.

Creare la classe *PriorityTicket* che eredita da *Ticket*, per rappresentare i biglietti prioritari.
Il costruttore accetta gli stessi parametri della classe padre,
più un numero intero che indica la priorità

Il metodo ```__repr__(self)``` restituisce una stringa 
contente le stesse informazioni del metodo di cui fa l'override
(usare il metodo padre per evitare la duplicazione di codice), più il valore della priorità.

Fare l'override di ```get_queue_pos(self)```, restituendo come posizione in coda il numero del biglietto
meno la priorità moltiplicata per 10.

Nel main creare una lista contenete diversi biglietti, prioritari e non, e ordinarla tramite il metodo ```sort()```.
Notare come avendo fornito un'implementazione di ```__lt__(self)``` sia possibile riordinare i biglietti per posizione.
Notare anche come l'override di ```get_queue_pos(self)```, usato da ``` __lt__(self, other)```,
abbia permesso di confrontare biglietti delle due diverse tipologie, tenendo conto della priorità.

# Esercizio 5 (Avanzato)
Modificare la classe *Directory* dell'esercizio 3 per ereditare da *File*.

Rimuovere il metodo ```get_name(self)``` in quanto già implementato dalla classe padre.
Fare l'override di ```get_dim(self)``` per restituire il numero di file nella cartella.

Spostare il contenuto del metodo ```__repr__(self)```
all'interno di un nuovo metodo ```get_info(self)``` (override di quello della classe padre).
Cambiare ```__repr__(self)``` di modo che restituisca il valore di ritorno di ```get_info()```.

Cosa succede ora se si aggiunge una directory a una directory tramite ```__add_file__(self, file)``` 
(diverse tra di loro) e la si stampa (ricordiamo che print usa il metodo ```__repr__(self)```)?
Dovrebbe venire stampato l'intero albero delle cartelle, perché?

Riuscite a formattare l'output con la giusta indentazione? Esempio:

```
my_folder: 0
        empty.info: 0
        myimage.bmp: (3, 2)
        mytext.txt: 3
        my_sub_folder: 0
                mytext.txt: 3
                myimage.bmp: (3, 2)
```

Cosa succede se aggiungo una cartella a se stessa?




























