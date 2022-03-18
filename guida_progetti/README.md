# Gestione progetti
In questa guida vengono introdotti i concetti base della gestione di progetti python,
ovvero la creazione di progetti con più file tramite 
e organizzazione in moduli e pacchetti.

Utilizzare un semplice editor di testo (come *blocco note*),
**NON** Pycharm.

## Moduli
Se il progetto su cui si lavora contiene molto codice,
è scomodo avere tutto i un unico file. 
Dividere il progetto su file diversi, chiamati moduli, aggiunge una suddivisione
fisica alla suddivisione logica del codice.

La modularizzazione rende il sorgente più facile da mantenere e modificare (maintainability),
e permette di riutilizzare una parte del codice senza doverlo duplicare (reusability).
Inoltre si evitano collisioni non volute degli identificatori
(per esempio sovrascrivere variabile che si credeva di non aver ancora introdotto).

### Creare e importare un modulo
Creare una cartella per contenere il progetto che verrà creato in questo tutorial.

Utilizzare un semplice editor di testo come blocco note (**NON** Pycharm)
per scrivere una funzione che, passato il nome dell'utente,
stampi un messaggio di saluto:

```python
def greet(name):
  print("Hello {}!".format(name))
```
Salvare il file come *greetings.py*.

Nella stessa cartella, creare il file *main_program.py*,
che importi il modulo e lo usi per salutare l'utente,
richiedendogli di inserire il proprio nome:

```python
import greetings
name = input("Insert your name: ")
greetings.greet(name)
```
Come si può vedere la keyword *import* permette d'importare un modulo
in un diverso sorgente python.

Aprire un terminale nella cartella e testare il programma.
```bash
python main_program.py
```

Ma non è finita qui, *main_program* è esso stesso un modulo
e può essere eseguito da python, in modo equivalente,
rendendolo esplicito tramite il flag *-m*:

```bash
python -m main_program
```

### Namespace e Symbol table
Ogni modulo definisce un proprio *namespace* locale,
ovvero una collezione dei nomi simbolici che sono stati definiti
(nomi variabili, nomi funzioni, etc...)
e le relative informazioni degli oggetti a cui questi simboli fanno riferimento.

I simboli appartenenti al namespace locale sono contenuti in una tabella dei simboli
locale (*symbol table*), ovvero visibile solo dal modulo stesso.

Aggiungere al file *greetings.py* la seguente linea di codice (al di fuori della funzione greet),
che stampa la tabella dei simboli locale del modulo.

```python
print('Symbol table of module "greetings" :\n {}'.format(dir()))
```

Eseguire il modulo *greetings*:
```bash
python -m greetings
```
Diversi simboli sono automaticamente definiti dall'interprete
(*\_\_name\_\_*, *\_\_builtins\_\_*, ecc...),
ma anche il simbolo della funzione *greet*,
definita dal programmatore.

### Diversi modi per importare
Analizzando il codice in *main_program.py* si vede che
per accedere alla funzione greet bisogna chiamare
``greetings.greet(...)`` invece di invocare direttamente
``greet(...)``. 

Questo perché ``import greetings``
aggiunge alla *symbol table* di *main_program*
solamente il simbolo *greeting* e non tutti i simboli del modulo importato.
Ciò è confermato se si aggiunge la seguente istruzione a *main_program*
e lo si esegue:

```python
print('Symbol table of module "main_program" :\n {}'.format(dir()))
```

E' tuttavia possibile rinominare il simbolo quando lo si importa:
```python
import greetings as grt
...
grt.greet(name)
```
Oppure aggiungere direttamente uno o più simboli da un modulo:
```python
from greetings import greet #, simbolo2, simbolo3
...
greet(name)
```
O aggiungere direttamente tutti i simboli 
(da usare con cautela per evitare collisioni).
I simboli che iniziano per *"\_"* non vengono importati.

```python
from greetings import *
...
greet(name)
```

### Import vs esecuzione
Prestando attenzione all'output di *main_program.py*
vi sarete resi conto che lasciando la linea ```print(...)```
all'interno di *greetings.py*, questa viene eseguita
non solo quanto si esegue direttamente il modulo,
ma anche quando questo viene importato.

Cio avviene perché, quando il modulo è importato,
l'interprete esegue tutte le istruzioni presenti nel file,
come in una normale esecuzione.

Quello che l'inteprete fa, però, è cambiare il valore associato
al simbolo *\_\_name\_\_*.
Questo viene settato a *"\_\_main\_\_"*
unicamente se il modulo è stato eseguito direttamente.
Con un semplice controllo, si può pertanto escludere del
codice dall'esecuzione quando il modulo viene importato.

Cambiare le seguenti linee in *greetings.py* 
e lanciare *main_program.py*
```python
if __name__ == "__main__":
    print('Symbol table of module "greetings" :\n {}'.format(dir()))
```
Ora la symbol table di *greetings* non viene più stampata
durante l'import, ma viene visualizzata se si lancia *greetings.py*.


## Pacchetti
Quando la grandezza del progetto cresce,
e conseguentemente anche il numero di moduli, 
è conveniente raggruppare quest'ultimi in pacchetti.
Un pacchetto è fondamentalmente una cartella che contiene più
moduli logicamente connessi.

### Creazione di pacchetti
Creare una cartella chiamata *salutations* in quella principale
e spostare il file *greetings.py* all'interno di essa.
Successivamente creare un altro file all'interno di *salutations*
chiamato *goodbye.py*.
All'interno del file aggiungere una funzione che saluta l'utente:
```python
def byebye(name):
  print("Bye bye {}!".format(name))
```

Modificare il *main_program.py* per supportare il cambiamento:
```python
import salutations.greetings
import salutations.goodbye

print('Symbol table of module "main_program" :\n {}'.format(dir()))

name = input("Insert your name: ")
salutations.greetings.greet(name)
salutations.goodbye.byebye(name)
```

E' anche possibile utilizzare la sintassi con *from* e *as*:
```python
from salutations.greetings import greet
from salutations.goodbye import byebye as bb
...
greet(name)
bb(name)
```

### Importare pacchetti con *\_\_init\_\_.py*
Modificare il *main_program.py*, nel seguente modo e vericare che **NON** funziona:
```python
import salutations
...
salutations.greetings.greet(name)
salutations.goodbye.byebye(name)
```
Comparando la symbol table con quella precedente (*import salutations.greetings*) si vede che non ci sono differenze: in entrambe è definito il simbolo *salutations*.

Però, se si stampano le proprietà
(verrano definite meglio quando verranno introdotti gli oggetti) associate a *salutation*, si vede che nessun simbolo è definito:
```python
import salutations
print('Symbol table of module "salutations" :\n {}'.format(dir(salutations)))
```
Se invece si fanno gli import "estesi", i simboli dei moduli appaiono:
```python
import salutations.greetings
import salutations.goodbye
print('Symbol table of module "salutations" :\n {}'.format(dir(salutations)))
```
Questo accade perchè *import salutation* definisce solo il simbolo,
ma non ha associato un modulo da eseguire che crei i simboli,
cosa che invece accade importanto un modulo. Esso viene eseguito
e i simboli delle variabili e funzioni creati.

E' però possibile associare un modulo da eseguire quando si esegue l'import del package.
Questo può fare l'import dei moduli al suo interno. 
Creare un file chiamato *\_\_init\_\_.py nella cartella *salutations*:

```python
import salutations.greetings, salutations.goodbye
```
Se ora si riesegue l'import di salutations i simboli vengono correttamente definiti.
```python
import salutations
print('Symbol table of module "salutations" :\n {}'.format(dir(salutations)))
```
E' anche possibile modificare *\_\_init\_\_.py* nel seguente modo:

```python
__all__ = ['greetings','salutations']
```
per permettere la seguente sintassi di import

```python
from salutations import *
...
salutations.greetings.greet(name)
salutations.goodbye.byebye(name)
```
In questo modo lo sviluppatore del modulo può controllare
cosa l'utilizzatore importa quando decide di importare "tutto".










