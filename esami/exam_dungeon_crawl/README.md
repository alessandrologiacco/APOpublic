# Dungeon Crawl
Si scriva un programma che sia in grado di rappresentare il gioco da tavolo e di carte Dungeon Crawl.

I moduli e le classi vanno sviluppati nel package *dungeon_crawl*.
Non spostare o rinominare moduli e classi esistenti e non modificare le signature dei metodi.

L'interfaccia grafica deve essere sviluppata nel package *gui*.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Esso mostra esempi di uso dei metodi principali ed esempi dei controlli richiesti.

Tutte le eccezioni, se non altrimenti specificato, sono di tipo *DungeonCrawlException*.

La classe *DungeonCrawlGame* permette di gestire il gioco.


## R1: Effetti e Azioni
La classe *DungeonCrawlGame* permette di definire azioni ed effetti,
identificati univocamente dal loro nome.
L'univocità dei nomi include entrambi
(un'azione e un effetto **NON** avranno mai lo stesso some).

Il metodo ```add_effect(self, effect_name: str, description: str, symbol: str) -> None```
permette di aggiungere un effetto.
Accetta come parametri il nome dell'effetto,
la sua descrizione e
una stringa di un solo carattere (*symbol*) che lo rappresenta graficamente.

Il metodo ```add_action(self, action_name: str, description: str) -> None```
permette di aggiungere un'azione.
Accetta come parametri il nome dell'azione e la sua descrizione.

Il metodo ```get_action_or_effect(self, name: str) -> str```
restituisce una stringa che rappresenta l'azione o l'effetto
di cui è passato il nome.
Il metodo lancia un'eccezione
se non sono presenti azioni o effetti con il nome specificato.

Nel caso di un effetto la stringa è composta
dal simbolo dell'effetto, 
dal carattere *":"*,
da uno spazio
e infine la descrizione.
Esempio: *"X: descrizione"*

Nel caso di un'azione la stringa è composta 
dal nome dell'azione, 
dal carattere *":"*,
da uno spazio
e infine la descrizione.
Esempio: *"Nome: descrizione"*


## R2: Carte
Il metodo ```add_card(self, card_name: str, level: int) -> None```
permette di aggiungere una carta.
*card_name* è una stringa che identifica univocamente la carta.
*level* è un intero che indica il livello di esperienza minimo poter usare la carta.

Ogni carta possiede una serie di azioni ed effetti.
Lo stesso effetto o azione può essere aggiunto a carte diverse.

Il metodo ```add_effect_to_card(self, card_name: str, effect_name: str) -> None``` 
permette di aggiungere un effetto alla carta.
Accetta come parametri il nome della carta e il nome dell'effetto da aggiungere.

Il metodo ```add_action_to_card(self, card_name: str, action_name: str, value: int, action_range: int) -> None```
permette di aggiungere un'azione a una carta.
Accetta come primi due parametri il nome della carta
e il nome dell'azione da aggiungere.
*value* e *action_range* identificano rispettivamente l'intensità dell'azione
e la distanza da cui può essere compiuta.
Questi ultimi sono valori specifici per la carta.
La stessa azione su carte diverse può avere *range* e *value* diversi.

Il metodo ```get_card_effects(self, card_name: str) -> List[str]```
accetta come parametro il nome di una carta e restituisce una lista
contenente i nomi di tutti gli **EFFETTI** presenti su di essa
**ORDINATI** alfabeticamente.

Il metodo ```get_card_actions(self, card_name: str) -> List[str]```
restituisce una lista contenente una stringa per ogni **AZIONE** aggiunta alla carta.
Ogni stringa deve contenere, in ordine, il nome dell'azione,
il *value* dell'azione e l'*action_range*,
tutti separati con virgole senza l'aggiunta di spazi.
Esempio: *"Attacco,3,10"*

```get_card_effects``` e ```get_card_actions```
restituiscono liste vuote se non sono presenti azioni o effetti.


## R3: Ruoli
Il metodo ```add_role(self, role_name: str, num_card: int) -> None```
permette di creare un nuovo ruolo.
Accetta come parametri il nome del ruolo che lo identifica univocamente,
e il numero massimo di carte un personaggio può giocare
se gli viene assegnato il ruolo
(Punto R5).

Il metodo ```add_card_to_role(self, role_name: str, card_name: str) -> None```,
permette di assegnare carte a un ruolo.
Accetta come parametri il nome del ruolo e il nome della carta da assegnarli.
Il metodo lancia un'eccezione se un ruolo o una carta con i nomi specificati non esistono.

Il metodo ```get_role_cards(self, role_name: str, max_level: Optional[int] = None)```
restituisce una lista contenente i nomi delle carte assegnate al ruolo *role_name*,
il cui livello sia inferiore o uguale a ```max_level```.

Nel caso in cui *max_level* non venga specificato,
restituire i nomi di tutte le carte associate al ruolo.
Se non sono presenti carte associate al ruolo
o nessuna carta soddisfa il requisito sul livello,
restituire una lista vuota.


## R4: Interfaccia grafica
Creare un'interfaccia grafica che permetta
aggiungere degli **EFFETTI** e ottenerne la rappresentazione
in stringa dato il nome.
Gestire le eccezioni *DungeonException* che si possono scatenare
dando un feedback all'utente.

Le classi dell'interfaccia devono trovarsi nel package *gui*.
Scrivere un main che lanci l'interfaccia grafica.

## R5: Personaggi e giocate
Il metodo ```add_character(self, character_name: str, role_name: str, level: int) -> None```
permette di aggiungere un personaggio, identificato univocamente dal suo nome.
*role_name* è il nome del ruolo da assegnare al personaggio,
mentre *level* indica il livello del personaggio.

Il metodo ```play_cards(self, character_name: str, card_1_name: str, card_2_name: str) -> None```,
accetta come parametri il nome del personaggio e i nomi di due carte da giocare
appartenenti al ruolo del personaggio.
Ignorare la richiesta e lanciare un'eccezione se:
- il livello di una delle due carte è maggiore di quello del personaggio
- se si supera il numero di carte giocabili indicato dal ruolo personaggio
- il personaggio gioca una carta che ha già giocato.

