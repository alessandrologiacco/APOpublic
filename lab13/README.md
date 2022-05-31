# Laboratorio 13
In questo laboratorio viene richiesto di sviluppare un programma complesso sui grafi.

# Trasporto Pubblico
Sviluppare un'applicazione che permetta di rappresentare e interrogare
la rete di trasporti pubblici della città di Torino.
L'applicazione deve essere in grado di calcolare un itinerario
data la fermata di partenza e quella di arrivo.

I moduli e le classi vanno sviluppati nel package *transport*.
Non spostare o rinominare le classi esistenti e non modificare le signature dei metodi.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Questo verrà fornito all'esame.

Nella package *tests* vengono forniti dei test simili a quelli che valuteranno la vostra prova d'esame.
Questi non verranno forniti all'esame ma saranno disponibili solamente per la correzione a casa.

## R1: Grafo
Viene fornita la classe astratta *Graph*
che definisce l'interfaccia per l'implementazione di un generico grafo **DIRETTO** e **PESATO**.

La classe *GraphCreator*, non istanziabile,
permette di ottenere un oggetto implementante la classe astratta *Graph*
tramite il metodo statico ```get_empty_graph() -> Graph```.

Creare un classe che implementi la classe astratta *Graph*,
utilizzando la metodologia preferita (matrice o lista adiacenze).
Il metodo ```add_node(self, value: Any) -> int``` permette di creare un nodo
il cui contenuto viene passato come parametro.
Esso restituisce un identificativo per il nodo aggiunto.

Il metodo ```add_edge(self, value: Any, from_id: int, to_id: int) -> None```
permette di aggiungere un ramo direzionale dato l'identificativo del nodo di partenza e quello di arrivo.
Le informazioni (peso) associate al ramo sono passate come primo parametro. 
Un nodo può essere connesso a se stesso.

È possibile ottenere il contenuto di un nodo e il peso di un ramo
tramite i metodi ```get_node(self, node_id: int) -> Any``` 
e ```get_edge(self, from_id: int, to_id: int) -> Any```,
fornendo rispettivamente l'identificativo del nodo e gli identificativi degli estremi del ramo.

Il metodo ```is_connected(self, from_id: int, to_id: int) -> bool```
restituisce *True* se è presente un collegamento tra due nodi, altrimenti restituisce *False*.
Gli identificativi nodi dei sono passati come parametri nell'ordine definito dalla direzione del collegamento.

Implementare ```__len__(self) -> int``` per restituire il numero di nodi.

**SUGGERIMENTO** al fine d'implementare il grafo può essere comodo sviluppare delle classi di supporto
rappresentati in nodi e i rami.

## R2: Esplorazione grafo
Il metodo ```get_children(self, node_id: int) -> Set[int]```, dato l'identificativo di un nodo,
restituisce gli identificativi di tutti i nodi a cui è connesso tramite un ramo uscente.

Il metodo ```get_parents(self, node_id: int) -> Set[int]```, dato l'identificativo di un nodo,
restituisce gli identificativi di tutti i nodi a esso connessi tramite un ramo entrante.

Il metodo ```find_path(self, from_id: int, to_id: int) -> List[int]``` 
implementa l'algoritmo di esplorazione Depth First Search
per trovare un percorso tra due nodi di dati identificativi.
Esso restituisce un lista contente l'elenco degli identificativi dei nodi del percorso in ordine di percorrenza.
Se nessun percorso è presente restituisce una lista vuota.

**SUGGERIMENTO**: l'algoritmo di Depth First Search si presta a un'implementazione ricorsiva.


## R3: Rete trasporti
La classe *TransportNetwork* rappresenta la rete di trasporto pubblico di una città.
La rete può essere schematizzata da un grafo in cui in nodi sono le fermate e i rami i collegamenti tra di esse.

Le fermate, rappresentate dalla classe *Stop*, sono descritte da nome della fermata e dalle sue coordinate (properties).
I collegamenti tra fermate sono descritti da una stringa che definisce il nome della linea.
Si assuma per semplicità che solamente una linea può connettere le stesse due fermate.

Il caricamento delle fermate avviene tramite il metodo ```load_stops(self, f_name: str) -> None```
della classe *TransportNetwork*, 
che riceve come parametro il nome di un file.
Nel file delle fermate, ogni riga è composta dal nome della fermata (che può contenere spazi)
e dalle sue coordinate (due valori floating point).
I tre elementi di ogni riga sono separati da una virgola.

Il caricamento delle connessioni avviene tramite il metodo ```load_connections(self, f_name: str) -> None```
della classe *TransportNetwork*, che riceve come parametro il nome di un file.
Nel file delle connessioni, ogni riga è composta dal nome della linea, la fermata di partenza e quella di arrivo
(le connessioni sono **DIREZIONALI**).
Tutti e tre i campi sono stringhe che possono contenere spazi.

Il metodo ```get_stop(self, stop_name: str) -> Stop``` restituisce la fermata (*Stop*) dato il nome.

Il metodo ```get_line(self, from_stop_name: str, to_stop_name: str) -> str```
restituisce il nome della linea che connette due fermate i cui nomi vengono passati come parametro.
L'ordine della connessione è quello dei parametri.

**ATTENZIONE**: Si consideri unicamente il caso di una lettura ordinata dei due file (prima fermate e poi connessioni).


## R4: Itinerario

Il metodo ```compute_itinerary(self, start_stop: str, end_stop: str) -> List[str]```
una lista rappresentante l'itinerario tra due fermate passate come parametri. 

Ogni stringa della lista è composta dai nomi della fermata e della linea da prendere alla fermata, 
separati da una freccetta (trattino + segno minore) preceduta e seguita da uno spazio: " -> ". 
Per l'ultima fermata usare *END* come nome della linea.