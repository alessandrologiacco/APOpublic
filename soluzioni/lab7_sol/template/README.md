# Laboratorio 7
In questo laboratorio viene chiesto di sviluppare un programma a oggetti più complesso ed esteso.

Pertanto gli obiettivi principali di questo laboratorio sono:
- capire come modellare a oggetti un problema complesso (molte classi e relazioni)
- fornire un'implementazione del programma richiesto
- organizzare il codice in moduli e pacchetti
- utilizzare il codice in ambiente grafico
- testare il codice tramite test automatici

# University
Progettare e implementare un programma che possa gestire corsi, studenti e il carico didattico per un ateneo.
Scrivere un package, chiamato *university*, che contenga tutte le classi.
Anche se in python è eccessivo, creare un file diverso per ogni classe per allenarsi con moduli e pacchetti.

La classe principale, i cui metodi definiscono l'interfaccia del package, è chiamata *University*.
Essa **deve essere importabile** tramite i seguenti due comandi:

``` python
from university import *
from university import University
```

Lo scheletro della classe principale viene fornito, contenente le signature dei metodi richiesti.
Per chiarezza, i tipi dei parametri e del valore restituito sono annotati tramite [type hinting](https://realpython.com/python-type-checking/)
(si possono considerare come semplici commenti).

È fornito un script *main.py* per testare le funzionalità base della classe University.
Un file simile verrà fornito anche all'esame, per semplificare lo sviluppo del codice.

Sono forniti i test, simili a quelli che verranno utilizzati per valutare la prova d'esame.
All'esame verranno forniti solo per la parte di correzione a casa della prova.
Pertanto è consigliato non considerarli nella fase di sviluppo del codice,
ma solo come controllo finale della propria implementazione.


## R1: Ateneo
La classe principale è *University* che riceve, come parametro del costruttore, il nome dell'ateneo.
Il nome dell'ateneo è leggibile tramite il metodo getter ```get_name(self) -> str```.

È possibile definire il nome del rettore di un ateneo tramite il metodo ```set_rector(self, name: str, surname: str) -> None``` che riceve come parametri nome e cognome del rettore.

Il metodo getter ```get_rector(self) -> str``` restituisce nome e cognome del rettore concatenati con uno spazio (" ") in mezzo.

## R2: Studenti
È possibile inserire le informazioni relative a un nuovo studente tramite il metodo ```add_student(self, name: str, surname: str) -> int``` della classe University,
che riceve come parametri il nome e il cognome dello studente

Il metodo restituisce il numero di matricola che è stato assegnato allo studente.
I numeri di matricola vengono assegnati, in maniera progressiva per ogni ateneo, a partire dal numero *10000*.

Per ottenere le informazioni relative a uno studente si utilizza il metodo ```get_student_info(self, student_id: int) -> str``` che riceve come parametro la matricola
e restituisce una stringa composta da numero di matricola, nome e cognome separati da spazi, es. *"10000 Giuseppe Verdi"*.

**Attenzione**: va bene, in questo caso, utilizzare proprietà di classe per aggiornare i numeri matricola?
Cosa succederebbe se si creassero più atenei (istanze della classe *University*)?

## R3: Corsi
Per definire un nuovo insegnamento si utilizza il metodo ```add_course(self, title: str, teacher: str) -> int``` che riceve come parametri il titolo del corso e il nome del docente titolare. 

Il metodo restituisce un intero che corrisponde al codice del corso. I codici vengono assegnati progressivamente a partire da *10*.

Per conoscere le informazioni relative a un corso si usa il metodo ```get_course_info(self, course_id: int) -> str``` che riceve come parametro il codice del corso
e restituisce una stringa contenente codice, titolo e titolare del corso, separati da virgole, es. *"10,Programmazione a Oggetti,James Gosling"*.

**Attenzione**: va bene, in questo caso, utilizzare proprietà di classe per aggiornare i numeri del corso?
Cosa succederebbe se si creassero più atenei (istanze della classe *University*)?

## R4: Iscrizione
Gli studenti possono essere iscritti agli insegnamenti tramite il metodo ```register_to_course(self, student_id: int, course_id: int) -> None``` che riceve come parametro la matricola dello studente e il codice del corso a cui iscriverlo.

Per ottenere l'elenco degli iscritti a un insegnamento è disponibile il metodo ```get_attendees(self, course_id: int) -> str``` che riceve come parametro il codice dell'insegnamento e restituisce una stringa contenente l'elenco degli studenti iscritti.

Gli studenti compaiono uno per riga secondo il formato descritto al punto R2.
Le righe sono separate da un carattere di a-capo ("\n").
**NON** deve essere presente un a-capo dopo l'ultima riga.

Data la matricola di uno studente, tramite il metodo ```get_study_plan(self, student_id: int) -> List[str]```, è possibile ottenere la lista d'insegnamenti a cui è iscritto.
Ciascun elemento della lista è una stringa che descrive l'insegnamento nel formato definito in R3.

## R5: Interfaccia grafica
Scrivere un'interfaccia grafica che permetta all'utente di aggiungere studenti e reperirne informazioni tramite numero di matricola.

Scrivere il codice dell'interfaccia grafica come sempre fatto (**NON** a oggetti),
e utilizzare la classe *University* per gestirne le funzionalità.

Il codice dell'interfaccia grafica **NON** deve trovarsi all'interno del package *university*.




