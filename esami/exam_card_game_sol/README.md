# Card Game
Si scriva un programma che sia in grado di rappresentare un gioco di carte collezionabili.

I moduli e le classi vanno sviluppati nel package *games*.
Non spostare o rinominare moduli e classi esistenti e non modificare le signature dei metodi.

L'interfaccia grafica deve essere sviluppata nel package *gui*.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Esso mostra esempi di uso dei metodi principali ed esempi dei controlli richiesti.

Tutte le eccezioni, se non altrimenti specificato, sono di tipo *GameException*.


## R1: Carte
Ogni personaggio del gioco ha un propria carta, rappresentata dalla classe *Card*.
Il costruttore ``` __init__(self, name: str, attack: int, life_points: int, mana_cost: int)```
accetta quattro parametri: il nome della carta, che la identifica univocamente,
i suoi punti di attacco, i suoi punti vita e il costo in mana (una particolare valuta)
per poterla giocare.

Tutte i parametri passati al costruttore possono essere ottenuti tramite property:
```name(self) -> str```, ```attack(self) -> int```,
```life_points(self) -> int``` e ```mana_cost(self) -> int```.

Il metodo ```is_dead(self) -> bool``` restituisce *False* se i punti vita sono superiori a zero,
altrimenti restituisce *True*.

L'override del metodo ```__repr__(self) -> str``` restituisce la rappresentazione in stringa della carta,
composta dall'elenco delle sue property.
Separare i valori con **UNO** spazio e usare lo stesso ordine con cui sono fornite al costruttore
(name, attack, life_points e mana_cost).
Esempio: *"Golem 10 5 3"*.

Il metodo statico ```fight(card1: "Card", card2: "Card") -> None```
riceve come parametri due carte e simula il loro combattimento.
Quando due carte combattono l'attacco di una viene scalato dai punti vita dell'altra e viceversa.
Dopo l'applicazione del metodo sulle due carte, esse devono riflettere queste modifiche (riduzione punti vita).
I punti vita possono andare in negativo.


## R2: Giocatori
La classe *Player* rappresenta un giocatore.
Il costruttore ```__init__(self, name: str) -> None``` riceve come parametro il nome del giocatore.

La classe presenta le seguenti property: 
```name(self) -> str```, ```field(self) -> List[Card]```, ```hand(self) -> List[Card]```,
```mana(self) -> int```.
Esse devono restituire, rispettivamente, il nome del giocatore, la lista di carte che ha messo in campo,
la lista di carte che ha in mano, e il mana (valuta) che ha a disposizione per giocare le carte.

Inizialmente il giocatore non ha carte in mano o sul campo (```hand``` e ```field``` sono liste vuote)
e il suo mana è pari a zero.
La property  ```mana``` deve permettere di settare il valore del mana del giocatore.

Il metodo  ```draw(self, card: Card) -> None``` permette al giocatore di "pescare" la carta passata come parametro
e di aggiungerla a quelle che ha in mano.

Il metodo ```play(self, card_name: str) -> None``` permette di mettere il campo una carta dalla mano del giocatore,
il cui nome viene passato come parametro.
Questo evento si deve rispecchiare sulle properties ```field``` e ```hand```.
Considerare che *NON* sia possibile avere due carte con lo stesso nome in mano.

Ogni volta che viene giocata una carta
il suo costo in mana viene scalato da quello a disposizione del giocatore.
Il metodo lancia un'eccezione se il giocatore non ha mana sufficiente per giocare la carta.


## R3: Tornei
La classe *Tournament* rappresenta un torneo.
Il suo costruttore ```__init__(self) -> None``` non presenta parametri.

Il metodo ```add_player(self, player) -> None``` permette di aggiungere un giocatore al torneo.
Lancia un'eccezione se un giocatore con lo stesso nome è già stato aggiunto.

Il metodo ```add_card(self, card) -> None``` permette di aggiungere un carta a quelle utilizzabili nel torneo.

Il metodo ```player_uses_card(self, player_name, card_name) -> None``` specifica che il giocatore *player_name*,
userà la carta *card_name* nel torneo.

Il metodo ```get_cards_of_player(self, player_name, sort_res=False) -> List[Card]```,
restituisce la lista di carte usate dal giocatore il cui nome è passato come parametro.
Come secondo parametro è possibile specificare
se la lista di carte debba essere ordinate alfabeticamente per nome (*True*)
oppure non avere un ordine specifico (*False*).

```get_players_of_card(self, card_name) -> List[str]``` restituisce una lista contente i nomi dei giocatori
che usano la carta *card_name* nel torneo.


## R4: Interfaccia grafica
Creare un'interfaccia grafica che permetta all'utente di creare nuove carte,
fornendo gli attributi necessari (nome, attacco, punti vita e costo in mana).
Dato l'elevato numero di attributi, **È SUFFICIENTE CHIEDERNE DUE ALL'UTENTE** e gli altri lasciarli sempre uguali
e definiti dal programmatore.

Permettere all'utente di ottenere le informazioni di tutte le carte che ha creato.

Le classi dell'interfaccia devono trovarsi nel package *gui*.
Scrivere un main che lanci l'interfaccia grafica.

## R5: Doppia giocata
Il metodo ```find_best_two(self) -> List[str]``` del giocatore restituisce i nomi delle due migliori carte da giocare
tra quelle che ha in mano (**NON** quelle che usa nel torneo), dato il mana posseduto.

La bontà della giocata è stabilita in base al valore di attacco delle due carte.
La prima carta va scelta con l'attacco maggiore possibile,
tale che ci sia mana sufficiente per giocare una seconda carta.
La seconda carta va scelta con attacco maggiore possibile 
tra quelle che è ancora possibile giocare dato il mana rimanente.

Se non è possibile giocare due carte, restituire una lista vuota.


