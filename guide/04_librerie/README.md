# Installazione librerie
Una delle potenzialità maggiori di python è la presenza di un'infinità di librerie non-standard, utili a fare praticamente qualsiasi cosa. Alcune delle più utilizzate sono:
- [numpy](https://numpy.org/) (vettori e matrici multidimensionali)
- [pandas](https://pandas.pydata.org/) (data analysis)
- [scipy](https://scipy.org/) (scientific computing)
- [scikit-learn](https://scikit-learn.org) (machine learning)
- [matplotlib](https://matplotlib.org/) (grafici)
- [networkx](https://networkx.org/) (reti e grafi)
- [keras](https://keras.io/) (deep learning)
- [tensorflow](https://www.tensorflow.org/) (reti neurali)
- [flask](https://flask.palletsprojects.com/en/2.0.x/) (web development)

## Librerie Python
Per ora potete immaginarvi una libreria come un modulo o un package contenente moduli Python.
Possono essere importate come package e moduli scritti da voi, usando *import*.

Le librerie di python si dividono in 2 categorie: *system packages* e *site packages*.
I *system packages* sono le librerie standard di python (es. *asyncio*, *distutils*, *os*, *sys*, ecc..), mentre i *site packages* sono quelle installate dall'utente.


## Virtual environments
Prima d'installare delle librerie si è soliti creare un **virtual environment** (PyCharm lo fa di default alla creazione di un progetto).
Un virtual environment è essenzialmente una copia dell'installazione di Python del proprio sistema, isolata da quella principale.

Quando si installa una libreria, il suo package viene aggiunto alla cartella contenente i *site packages*.
Il problema, però sorge, quando si lavora parallelamente su diversi progetti che necessitano di versioni diverse della stessa libreria.
Non è infatti possibile installare contemporaneamente due versioni della stessa libreria.

Creando un virtual environment, oltre a copiare l'interprete, viene creata una zona nuova dove installare i *site packages* specifici per quell'environment.
Creando un environment diverso per ogni progetto, e possibile lavorare con versioni diverse di librerie di terze parti.
Per quanto riguarda i *system packages*, vengono usati quelli presenti nell'installazione principale.

Per creare un virtual environment usare il modulo python di sistema *venv*:

```python
python -m venv .my_env
```

Questo crea la cartella nascosta *.my_environment* contenete il virtual environment (potete usare il nome che preferite, anche non nascosta).

Successivamente attivare l'environment:
```bash
.my_env\Scripts\activate.ps1 # Windows
source .my_env/bin/activate # MacOS and Linux
```
Tutti i comandi python usati in questa sessione del terminale useranno il virtual environment invece dell'installazione principale.

Se si vuole disattivarlo, usare il comando:
```bash
deactivate
```
Per eliminarlo, invece, basta cancellare la cartella che lo contiene.

Se create il progetto in un repository git è fortemente consigliato aggiungere al *.gitignore* la cartella che contiene il vostro virtual environment.


## Installare dal Python Package Index (PyPI)
Il [Python Package Index](https://pypi.org/) è un repository software per Python.
Chiunque può caricare le librerie che sviluppa in questo repository, rendendole accessibili a chiunque li voglia usare.

Per installare e gestire le librerie si usa il modulo *pip*.
Creare un cartella principale. Creare un nuovo virtual environment e attivarlo.
Mostrare i *site packages* del virtual environment:

```bash
python -m pip freeze
```
Nulla è installato, quindi procedere a installare *matplotlib* e successivamente mostrare le librerie installate:

```bash
python -m pip install matplotlib
python -m pip freeze
```

Si vede ora che *matplotlib* è stato installato, insieme ad altre librerie che gli servono funzionare, chiamate dipendenze.
Provare a usarlo, creando un script che generi un semplice grafico:

```python
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1,23,2,4]
plt.plot(x, y)
plt.ylabel('some numbers')
plt.show()
```
Per rimuoverlo usare

```bash
python -m pip uninstall matplotlib
python -m pip freeze
```
Come si vede il modulo è stato rimosso ma le sue dipendenze sono ancora presenti.
Questo perché è possibile che quest'ultime siano utilizzate da altre librerie installate.

## Gestire le dipendenze
Se si crea un package o un software che utilizza delle librerie e si vuol permettere ad altri di usarlo, è necessario comunicare nome e versione delle dipendenze. 

Per farlo, è comune creare nella cartella principale un file, chiamato *requirements.txt*, in cui copiare l'output di pip freeze.

In questo modo, prima di usare il vostro software, l'utente può invocare il seguente comando per installare tutte le dipendenze:
``` bash
python -m pip install -r requirements.txt
```

Testarlo con il file *requirements.txt* fornito insieme alla guida.

## Python Wheel
Le librerie python, quando installate con pip, sembrano tutte uguali, ma in realtà nascondono molte differenze.

Un primo tipo di librerie sono quelle in *pure python*, ovvero il cui codice è composto solamente da moduli python.
Esistono però librerie, come ad esempio *numpy* e *scipy*, che contengono codice scritto in alti linguaggi come *Fortran*, *C* e *C++*.
Questo viene fatto per sfruttare la velocità dei linguaggi compilati nelle operazioni più intense.

Inoltre esistono librerie, come ad esempio *tkinter* e *h5py*, che non contengono la libreria in se, ma fanno da interfaccia verso una shared library installata indipendentemente sul sistema operativo (*tk* e *hdf5*).

Il primo caso non è di così difficile gestione, l'installazione consiste solamente nel copiare i file python e installare le dipendenze.
Il terzo, una volta installata indipendentemente la *shared library* e se la libreria di "interfaccia" è scritta un *pure python*, ricade nel primo.

Il caso di librerie con codice di altri linguaggi crea non pochi problemi.
Questo perché il codice, prima di essere eseguito, deve essere compilato nel linguaggio macchina specifico per l'architettura di processore usata.
E anche se questa è equivalente, il sistema operativo impone delle differenze nei formati dei file eseguibili (es. *.exe* su Windows, *ELF* in Linux e *Mach-O* in MacOS).

Chi sviluppa questo tipo di librerie fornisce diverse versioni, già compilate per la specifica architettura e sistema operativo.
Quando si invoca pip viene scaricata automaticamente la versione corretta per il sistema in uso.
Questi package binari sono chiamati *wheels* e la loro estensione è *.whl*.

Altrimenti è possibile compilarle da codice sorgente, ma in questo caso è necessario avere installato tutti i compilatori e le librerie dei linguaggi usati.
Cosa molto scomoda, che può richiede anche tempo se la libreria è vasta e rischia di fallire se il vostro sistema presenta anche leggere differenze da quello usato dagli sviluppatori.

Pertanto pip utilizza di default la versione wheel, quando questa è disponibile.


## Riferimenti
- [Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
- [Python Wheels](https://realpython.com/python-wheels/)










