# Chess Manager
Si scriva un programma che sia in grado di gestire delle partite a scacchi.
La classe principale è *ChessManager*.

I moduli e le classi vanno sviluppati nel package *chess*.
Non spostare o rinominare moduli e classi esistenti e non modificare le signature dei metodi.

L'interfaccia grafica deve essere sviluppata nel package *gui*.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Esso mostra esempi di uso dei metodi principali ed esempi dei controlli richiesti.

Tutte le eccezioni, se non altrimenti specificato, sono di tipo *ChessException*.


## R1: Scacchiera
La classe *Board* rappresenta una scacchiera quadrata.
Il costruttore ```__init__(self, name: str, dim: int) -> None```
accetta due parametri: il nome della scacchiera, che la identifica univocamente,
e la sua dimensione (numero celle su un lato).

Il nome e la sua dimensione possono essere ottenuti con properties
```name(self) -> str``` e ```dim(self) -> int```.

La classe *Piece* definisce come costanti le stringe rappresentanti i pezzi.

Il metodo ```add_piece(self, piece: Optional[str], x: int, y: int) -> None```
permette di aggiungere un pezzo alla scacchiera in posizione (x, y).
Passando *None* come primo parametro è possibile rimuovere, se presente, il pezzo in posizione (x, y).

Il metodo ```get_piece(self, x: int, y: int) -> Optional[str]```,
restituisce il pezzo il posizione (x, y). Se nessun pezzo è presente il metodo restituisce *None*.

Gli indici delle celle partono da **ZERO**.
Entrambi i metodi lanciano un'eccezione se la posizione fornita non è valida.

## R2: Giocatori
La classe *Player* rappresenta un giocatore.
Il costruttore ```__init__(self, name: str, nationality: str, age: int) -> None```
riceve come parametri il nome del giocatore, la sua nazionalità e la sua età.

La classe deve implementare ```__repr__(self) -> str```,
che restituisce queste informazioni separate da virgole.
**NON** inserire spazi se non già presenti nel nome o nella nazionalità.
Esempio: *"Edoardo,Italian,29"*.

Il metodo ```add_board(self, board: Board) -> None```
permette di aggiungere una scacchiera al *ChessManager*.

Il metodo ```get_board(self, name: str) -> Board```
restituisce la scacchiera dato il nome.

Il metodo ```add_player(self, player: Player) -> None``` permette di aggiungere un giocatore al *ChessManager*.

Il metodo ```get_player(self, name: str) -> Player``` restituisce il giocatore dato il nome.

Il metodo ```add_player_to_board(self, player_name: str, board_name: str) -> None```
specifica che il giocatore *player_name* sta giocando sulla scacchiera *board_name*.


Il metodo ```get_boards_of_player(self, name: str) -> List[Board]```
restituisce una lista di scacchiere su cui sta giocando il giocatore *player_name*.

## R3: Tornei
Il metodo ```create_tournament(self, name: str) -> None```
crea un torneo identificato univocamente dal suo nome.
Lancia un'eccezione se un torneo con lo stesso nome è già stato creato.

Il metodo ```add_player_score(self, tournament_name: str, player_name: str, score: int) -> None```
registra il punteggio (*score*) del giocatore *player_name* al torneo *tournament_name*.
Lancia un'eccezione se il giocatore *player_name* non è stato definito.

Il metodo ```get_leading_player(self, tournament_name: str) -> Optional[str]```
restituisce il nome del giocatore con il punteggio più alto nel torneo e il suo punteggio,
separati da due punti (":").
Esempio: *"Edoardo:51"*.
Restituire *None* se il torneo non ha giocatori.

**NON** inserire spazi se non già presenti nel nome.
Considerare che **NON** ci siano situazioni di parità.

## R4: Interfaccia
Creare un'interfaccia grafica che,
inizializzata con una scacchiera già popolata,
permetta di ottenere il pezzo, se presente, data la sua posizione (x, y).

Permettere inoltre di rimuovere un pezzo data la sua posizione (x, y).

Gestire le *ChessException* che si scatenano, in entrambe le operazioni,
quando la posizione fornita non è valida.
In questi casi mostrare un messaggio di errore all'utente.

Le classi dell'interfaccia devono trovarsi nel package *gui*.
Scrivere un main che inizializzi una scacchiera e lanci l'interfaccia grafica.

## R5: N Regine
Il metodo ```fill_queens(self, board_name: str, board_size: int) -> Board```
restituisce una scacchiera di nome *board_name* e grandezza *board_size* contenente unicamente regine,
in numero uguale alla dimensione della scacchiera.

Le regine devono essere posizionate di modo che nessuna regina possa essere sotto attacco dalle altre.
Si ricorda che una regina può attaccare le altre
muovendosi di un numero di celle a piacere in orizzontale, verticale o diagonale.

Il metodo statico già **FORNITO** ```check_queen(board: Board, x: int, y: int) -> bool```
restituisce *True* se è possibile inserire una regina in una cella (x, y)
controllando che la cella sia vuota e che la regina, se posizionata nella casella,
non sia sotto attacco dalle altre.
Altrimenti restituisce *False*.

Testare con dimensioni ridotte (da 3 a 10), data la complessità del problema.

 In *main.py* è fornita la funzione
 ```print_board(b: Board) -> None``` che permette stampare a schermo la scacchiera.

 Si consiglia di usare la funzione ```check_queen``` per effettuare i controlli d'inserimento.