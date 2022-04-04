# Laboratorio 6
In questo laboratorio si sviluppano i primi programmi a oggetti.
Gli argomenti su cui prendere confidenza sono:
- costruttori
- proprietà (sia d'istanza che di classe) e metodi
- notazione pubblico/privato
- getters e setters
- overriding operatori
- semplici relazioni tra classi

# Esercizio 1
Scrivere una classe che tenga il conto dei canestri fatti da una squadra di basket.

Tramite il metodo *add_match* deve essere possibile registrare una partita, dato il nome della squadra avversaria e il numeri di canestri fatti.
Il metodo *get_average* deve restituire la media di canestri fatti per partita.
Il metodo *get_teams* deve restituire una lista contente i nomi delle squadre contro cui si ha giocato.
Il metodo *get_summary* deve restituire una stringa che riporti il numero totale di canestri e la media di canestri fatti per partita.

Scrivere una funzione *main* che testi le funzionalità della classe sviluppata.

**Suggerimento**: sviluppare un'unica classe

# Esercizio 2
Scrivere una classe che rappresenti un documento d'identità.

Il costruttore deve accettare come parametro il nome e il cognome dell'intestatario e opzionalmente l'anno in cui il documento è stato rilasciato.
Se non specificato usare *2022* come valore di default.

Scrivere i getters per nome, cognome e anno di rilascio.

Scrivere il metodo *set_birth_year* che permetta registrare l'anno di nascita.
Se l'anno di nascita è maggiore dell'anno di rilascio l'anno di nascita deve essere impostato uguale all'anno di rilascio.
Scrivere un getter per ottenere l'anno di nascita.

Il costruttore deve definire un ulteriore attributo, rappresentante il numero documento.
Il numero documento deve incrementare di uno per ogni nuovo documento.
Il numero documento deve essere ottenibile tramite getter.

Scrivere una funzione *main* che testi le funzionalità della classe sviluppata.

**Suggerimento**: per aggiornare il numero documento si può usare una proprietà di classe
che tiene conto di quante volte il costruttore viene chiamato.

# Esercizio 3
Creare la classe *Player* che rappresenti un giocatore.
Il costruttore deve ricevere nome, cognome ed età del giocatore.
Questi valori devono essere ottenibili tramite getters.

Creare la classe *Team* che rappresenti una squadra.
Il costruttore deve ricevere il nome della squadra e la città a cui appartiene.
Questi valori devono essere ottenibili tramite getters.

Il giocatore deve avere un metodo *set_team* che registra la squadra in cui gioca il giocatore.
Il metodo riceve come parametro un oggetto della classe *Team*.
Scrivere un getter della classe giocatore che restituisca il *Team* del giocatore.
Se una squadra non è registrata deve restituire *None*.

La squadra deve avere un metodo *add_player* che riceve un oggetto di tipo *Player* da aggiungere alla squadra.
Il metodo *get_players* della squadra restituisce la lista di *Players* che giocano nella squadra.

Scrivere una funzione *main* che testi le funzionalità delle classi, associando i giocatori alle squadre e viceversa.

# Esercizio 4
Scrivere la classe *Matrix* che rappresenti una matrice 2x2.

Il costruttore deve ricevere come unico argomento una tabella rappresentante la matrice.
Scrivere due getters che restituiscano il numero di righe e il numero di colonne.

Implementare gli operatori *\_\_add\_\_*, *\_\_sub\_\_*, *\_\_mul\_\_* di modo che effettuino la somma, differenza e prodotto riga-colonna di due matrici.
Scrivere l'operatore *\_\_eq\_\_* di modo che sia possibile verificare l'uguaglianza di due matrici.

Implementare il metodo *\_\_str\_\_* per fornire una rappresentazione in stringa della matrice.

Scrivere una funzione *main* esegua operazioni tra oggetti della classe *Matrix* (*+*, *-*, *\**).
Testare anche l'operatore di confronto (*==*) e la rappresentazione in *str* provando a stampare un oggetto *Matrix*.















