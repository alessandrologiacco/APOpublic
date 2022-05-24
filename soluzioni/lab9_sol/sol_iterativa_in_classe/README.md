# Laboratorio 9
In questo laboratorio viene chiesto di sviluppare un programma più complesso
che richiede l'utilizzo di concetti di ereditarietà.
La struttura del laboratorio segue quella di una prova d'esame.

# Sistema idraulico
Scrivere un software per la descrizione e simulazione di un sistema idraulico.
I moduli e le classi vanno sviluppati nel package *hydraulics*.
Non spostare o rinominare le classi esistenti e non modificare le signature dei metodi.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Questo verrà fornito all'esame.

Nella package *tests* vengono forniti dei test simili a quelli che valuteranno la vostra prova d'esame.
Questi non verranno forniti all'esame ma saranno disponibili solamente per la correzione a casa.

## R1: Sistema ed elementi
Un sistema idraulico è composto da elementi di vario tipo connessi tra loro.
Un sistema idraulico è rappresentato da un oggetto di classe *HSystem*,
mentre gli elementi dalla classe base *Element*.

È possibile aggiungere elementi al sistema tramite il metodo ```add_element(self, elm: Element) -> None``` di *HSystem*,
il quale riceve come parametro un oggetto di tipo *Element*
e lo aggiunge ai componenti che formano il sistema idraulico.

Tramite il metodo ```get_elements(self) -> List[Element]```
è possibile ottenere una lista contenente gli elementi presenti nel sistema.

Tutti gli elementi hanno un nome che può essere letto tramite il metodo ```get_name(self) -> str```.

**NOTA**: *Element* serve solo come classe "template" per i figli,
non verrà mai creato un oggetto di tipo *Element* e passato ad ```add_element()```.
Questo, come verrà spiegato a lezione, è il concetto di classe astratta.
Per renderlo esplicito nel codice, *Element* eredita da ABC (consideratelo solo come un'annotazione).


## R2: Elementi semplici
Sono definiti tre tipi di elementi semplici: sorgente, rubinetto e scarico,
che sono rispettivamente rappresentati dalle classi *Source*, *Tap* e *Sink* che ereditano da *Element*.

È possibile connettere l'uscita di un elemento all'ingresso di un altro
tramite il metodo ```connect(self, elm: "Element") -> None```
Il metodo riceve come parametro l'elemento al cui ingresso deve essere connessa l'uscita dell'elemento sui cui è invocato.
Ad esempio, *a.connect(b)* connette l'uscita di *a* all'ingresso di *b*.
Il metodo, se invocato su un oggetto *Sink*, non ha nessun effetto.

Dato un elemento semplice qualunque, è possibile sapere a quale altro elemento è connessa la sua uscita,
tramite il metodo ```get_output(self) -> Optional["Element"]``` che restituisce un oggetto di tipo *Element*.
Se nessun elemento è collegato alla sua uscita restituisce *None* 
(il type hint *Optional* serve proprio a indicare la possibilità di avere *None* come valore di ritorno).

## R3: Elementi complessi
Oltre agli elementi semplici, sopra descritti, è possibile utilizzare degli elementi complessi.
L'elemento a T, rappresentato dalla classe *Split*,
permette di suddividere l'ingresso in due flussi in uscita uguali tra loro.

Per tale classe il metodo  ```connect_at(self, elm: Element, pos: int) -> None``` riceve un ulteriore parametro,
di tipo intero, che indica il numero dell'uscita a cui connettere l'elemento.
Tale intero ha valore *0* per la prima uscita e *1* per la seconda.

Per sapere quali elementi sono connessi in uscita a un elemento a T,
è possibile utilizzare il metodo ```get_outputs(self) -> List[Optional[Element]]```,
che restituisce una lista con i due elementi connessi.
Se un'uscita non è connessa ad alcun elemento, inserire *None* nella lista al posto dell'elemento.

## R4: Interfaccia grafica
Sviluppare un'interfaccia grafica che,
utilizzando il package *hydraulics*,
permetta di aggiungere elementi al sistema idraulico
specificandone il tipo e il nome.

L'interfaccia deve permettere all'utente di visualizzare
l'elenco di elementi presenti nel sistema,
mostrandone tipo e nome.

## R5: Simulazione
Dato un sistema **CORRETTO**, ovvero un albero che ha come radice una sorgente
e in cui ogni percorso termina con uno scarico,
è possibile fare un calcolo delle portate e di come vengono ripartite nei vari elementi.

Il calcolo prevede due fasi: una prima fase (*setup*)
i cui si definiscono i parametri dei diversi elementi del sistema 
e una seconda fase (*simulazione*) in cui si avvia la simulazione.

Durante la fase si setup è possibile configurare il comportamento degli elementi:

- definire la portata per una sorgente (*Source*) con il metodo ```set_flow(self, flow: float) -> None```,
che riceve come parametro un numero reale che rappresenta i metri cubi al secondo erogati dalla sorgente

- impostare l'apertura dei rubinetti (*Tap*), tramite il metodo
```set_status(self, to_open: bool = True) -> None```, che riceve come parametro un boolean.
Se un rubinetto è aperto la portata in uscita è uguale a quell in ingresso,
altrimenti la portata in uscita è pari a *0*.

- Per i raccordi a T la portata in ingresso viene sempre ripartita equamente tra le due uscite.

Il metodo ```simulate(self) -> List[str]``` della classe HSystem effettua i calcoli di portata a partire da ogni sorgente e salva,
per ogni elemento: il nome e le portate in ingresso e in uscita.

Quando, durante la simulazione, sono noti i flussi in entrata e in uscita per un elemento,
deve essere creata un stringa contente il tipo di elemento (nome della classe),
il nome dell'elemento, il flusso in ingresso e i flussi in uscita (2 nel caso dello Split).
Il tutto deve essere separato da uno spazio, e i valori scritti su 3 cifre decimali e.g.,
*"Split Split_1 11.500 5.750 5.750"*

Il flussi in ingresso alle sorgenti e il flussi in uscita ai *Sink* devono essere pari a *0*.

Il metodo restituisce una lista contenente tutte queste stringhe.

**SUGGERIMENTO**: per capire di che classe (*Source*, *Tap*, *Split* o *Sink*) è un elemento si può utilizzare
la funzione ```isinstance(object, type)```.







